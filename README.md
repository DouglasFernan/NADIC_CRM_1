# Instalação do NADIC CRM parte 1

Este guia contém instruções para configurar e executar o NADIC CRM em seu ambiente local.

## Requisitos:

Python instalado  

Git instalado

## Passo 1: Clonar o Repositório

Abra o Visual Studio Code ou outra IDE de sua preferência e navegue até a pasta em seu computador onde deseja instalar o projeto. Em seguida, execute o seguinte comando no terminal:  

`git clone https://github.com/DouglasFernan/NADIC_CRM_1`


## Passo 2: Instalar Dependências

Após clonar o repositório, entre na pasta recém-clonada que contém o arquivo `requirements.txt`. No terminal, digite o seguinte comando:  

`pip install -r requirements.txt`


## Passo 3: Executar o Servidor Local

Agora, entre na pasta `nadic_crm`, onde está localizado o arquivo `manage.py`. No terminal da sua IDE, execute o seguinte comando:

`python manage.py runserver`


Pronto! O servidor local deve estar em execução, e o terminal do Visual Studio Code ou da sua IDE mostrará o caminho para acessá-lo.
