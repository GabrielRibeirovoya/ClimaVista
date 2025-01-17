# -----------------------------------------------
# Script PowerShell: Configurador de Tarefa Agendada
# Função: Ler configuração JSON, validar, criar ou atualizar a tarefa agendada.
# -----------------------------------------------

# Caminho para o diretório atual onde o script PowerShell está localizado
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Caminho do arquivo JSON de configuração
$ConfigFilePath = Join-Path -Path $ScriptDir -ChildPath "sender.json"

# Caminho do script Python dentro da subpasta "Sender"
$PythonScriptPath = Join-Path -Path $ScriptDir -ChildPath "sendEmail.py"

# Nome da tarefa agendada
$TaskName = "RunSenderEmailScript"

# Função para validar o JSON de configuração
function Validate-Config($Config) {
    if (-not $Config.Frequency -or ($Config.Frequency -notin @("Daily", "Weekly", "Monthly"))) {
        throw "O campo 'frequency' está ausente ou inválido no arquivo de configuração. Valores aceitos: 'Daily', 'Weekly' ou 'Monthly'."
    }

    if (-not $Config.StartTime) {
        throw "O campo 'startTime' está ausente no arquivo de configuração. Insira um horário no formato HHmm (ex: 0700 para 07:00)."
    }

    if ($Config.StartTime -notmatch "^\d{4}$") {
        throw "O campo 'startTime' está no formato incorreto. Ele deve ser um valor numérico de 4 dígitos, como 0700 para 07:00."
    }

    if (-not (Test-Path -Path $PythonScriptPath)) {
        throw "O script Python 'sendEmail.py' não foi encontrado no diretório 'Sender'."
    }

    return "OK"
}

# Função para criar ou atualizar a tarefa agendada
function CreateOrUpdate-ScheduledTask($Config) {
    # Converter o horário do formato HHmm para HH:mm
    $StartTime = $Config.StartTime.Insert(2, ":") # Exemplo: "0700" -> "07:00"

    # Configurar os argumentos da tarefa
    $Action = New-ScheduledTaskAction -Execute "python.exe" -Argument "`"$PythonScriptPath`""
    $Trigger = $null

    # Configurar o gatilho baseado na frequência
    switch ($Config.Frequency) {
        "Daily" {
            $Trigger = New-ScheduledTaskTrigger -Daily -At $StartTime
        }
        "Weekly" {
            $Trigger = New-ScheduledTaskTrigger -Weekly -At $StartTime
        }
        "Monthly" {
            $Trigger = New-ScheduledTaskTrigger -Monthly -At $StartTime
        }
    }

    # Verificar se a tarefa já existe
    $ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

    if ($ExistingTask) {
        # Se a tarefa já existir, comparar os detalhes e atualizar se necessário
        Write-Host "Tarefa existente encontrada. Verificando alterações..."
        
        # Coletar informações da tarefa existente
        $ExistingTrigger = $ExistingTask.Triggers | Select-Object -First 1
        $ExistingStartTime = $ExistingTrigger.StartBoundary.Substring(11, 5) # Extrai o horário (HH:mm)

        if ($ExistingStartTime -ne $StartTime -or $ExistingTrigger.ScheduleType -ne $Config.Frequency) {
            Write-Host "Atualizando a tarefa agendada..."
            Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
            Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Description "Tarefa atualizada para executar o script sendEmail.py" -Force
            Write-Host "Tarefa atualizada com sucesso!"
        } else {
            Write-Host "A tarefa já está atualizada. Nenhuma ação necessária."
        }
    } else {
        # Criar a tarefa se ela não existir
        Write-Host "Criando nova tarefa agendada..."
        Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Description "Tarefa para executar o script sendEmail.py" -Force
        Write-Host "Nova tarefa agendada criada com sucesso!"
    }
}

# -----------------------------------------------
# Etapa 1: Ler o arquivo de configuração JSON
# -----------------------------------------------
try {
    if (-not (Test-Path -Path $ConfigFilePath)) {
        throw "O arquivo de configuração 'sender.json' não foi encontrado no diretório do script."
    }

    # Ler o JSON e convertê-lo em um objeto PowerShell
    $Config = Get-Content -Path $ConfigFilePath | ConvertFrom-Json
    Write-Host "Configuração carregada com sucesso!"

    # -----------------------------------------------
    # Etapa 2: Validar os dados do JSON
    # -----------------------------------------------
    Validate-Config -Config $Config
    Write-Host "Configuração validada com sucesso!"

    # -----------------------------------------------
    # Etapa 3: Criar ou atualizar a tarefa agendada
    # -----------------------------------------------
    CreateOrUpdate-ScheduledTask -Config $Config

} catch {
    # Capturar e exibir mensagens de erro
    Write-Error "Erro: $_"
}
