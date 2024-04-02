# Avaliação 1 | Consumo de API: Consulta de Clãs do anime Naruto

Este projeto permite consultar informações sobre personagens de um clã específico no universo de Naruto, consumindo a [API fornecida pelo NarutoDB](https://narutodb.xyz/).

## Sobre a API NarutoDB

A [NarutoDB API](https://narutodb.xyz/docs) fornece uma base de dados abrangente referente ao anime e mangá Naruto. Com esta API, é possível acessar facilmente informações detalhadas sobre cada personagem, clã, vila, time e muito mais.

## Funcionalidades do arquivo .py

- Solicita ao usuário que digite o nome do clã desejado.
- Faz uma solicitação à API NarutoDB para obter informações sobre os personagens do clã especificado.
- Extrai os dados recebidos da API, incluindo os jutsus e os tipos de natureza de cada personagem.
- Organiza os dados em um DataFrame do pandas.
- Exibe os dados na forma de um DataFrame.
- Salva os dados em um arquivo Excel no formato `.xlsx`.

## Requisitos

- Python instalado.
- Bibliotecas `requests` e `pandas` instaladas (Arquivo "requirements.txt" disponível).

## Como Usar

1. Clone ou baixe o repositório em sua máquina local.
2. Abra o terminal e navegue até o diretório onde o código está localizado.
3. Execute o código Python (`python data_api_narutodb.py`).
4. Digite o nome do clã para consultar as informações.
5. Aguarde a conclusão do processo. Os dados serão exibidos no terminal e um arquivo Excel será gerado no mesmo diretório, contendo os dados dos personagens do clã consultado.

Este é um projeto desenvolvido para a disciplina de DW3 na FATEC Araras.
