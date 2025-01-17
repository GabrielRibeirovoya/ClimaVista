# ClimaVista

## Bem-vindo ao ClimaVista!

O **ClimaVista** é um sistema simples e intuitivo para monitoramento de clima, que utiliza a poderosa API da OpenWeatherMap para trazer informações sobre o clima em tempo real. Este programa permite consultar a temperatura atual, as temperaturas mínima e máxima do dia, a descrição do clima, a pressão atmosférica e a umidade do ar.

Com uma interface fácil de usar, o ClimaVista é ideal para quem deseja acompanhar as condições meteorológicas de forma prática e rápida.

## Funcionalidades

- **Monitoramento do Clima:** Verifique as condições climáticas do dia, incluindo:
  - Temperatura atual
  - Temperatura mínima e máxima
  - Descrição do clima
  - Pressão atmosférica
  - Umidade do ar

- **Seleção da Unidade de Temperatura:** O usuário pode escolher a unidade de medida para as temperaturas entre:
  - **Kelvin**
  - **Celsius**
  - **Fahrenheit**

- **Envio de E-mail Automático:** O ClimaVista oferece a opção de enviar um resumo das condições climáticas diretamente para o seu e-mail. O único requisito é informar o endereço de e-mail e o horário em que deseja receber as atualizações.

> **Atenção:** Para que o envio de e-mail aconteça de forma automática, o computador precisa estar ativo no momento do envio, pois o processo depende da execução do programa.

## Como Funciona

1. O usuário informa a sua localização (cidade) para consultar as condições climáticas.
2. O programa consulta a API da OpenWeatherMap para obter as informações em tempo real.
3. O usuário pode configurar a unidade de temperatura desejada (Kelvin, Celsius ou Fahrenheit).
4. O usuário também pode configurar o envio automático de e-mails com as informações climáticas, basta fornecer um horário e o endereço de e-mail de destino.
5. O ClimaVista realiza a coleta dos dados e envia o e-mail conforme solicitado.

## Requisitos

- **Python** O ClimaVista foi desenvolvido utilizando o versão 3.13.1.
- **PowerShell** Para criação dos serviços de envio automatico.
- **API Key da OpenWeatherMap:** Para usar a API de clima, será necessário registrar-se no [OpenWeatherMap](https://openweathermap.org/) e obter uma chave de API.

## Como Instalar

1. Faça o clone deste repositório para sua máquina local:
   ```bash
   git clone https://github.com/GabrielRibeirovoya/ClimaVista.git
