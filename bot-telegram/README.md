## bot-telegram
ChatBot para o Telegram construído durante a sessão de Dojo da Squad Stranger Things.

## Pré-Requisitos - Software
Para a execução do programa, os seguintes itens deverão estar instalados na máquina.

* Python3: https://realpython.com/installing-python
Interpretador "raíz" da linguagem Python em sua versão 3.5

* Pip: https://automatetheboringstuff.com/appendixa
Gerenciador de dependências do python

## Pré-Requisitos - Autenticação APIS:
Para a execução do programa, são necessárias dois tokens de API para a comunicação com os serviços. Para obter as chaves de API, verifique os seguintes conteúdos:

- BotFather: https://core.telegram.org/bots#6-botfather
<br>O BotFather é um bot (feito pela equipe do Telegram) para você gerenciar seus próprios bots. A criação de um novo bot é feita diretamenta no Telegram através de interações com o BotFather.

- Giphy: https://developers.giphy.com/
<br>O Giphy é um serviço que indexa e pesquisa gifs animados. Acesse o site acima e crie um App que será utilizado pelo seu bot.

## Configuração do Ambiente

1. Na raíz do projeto, execute o comando `sudo pip3 install -r requirements.txt`.

2. Após a instalação das bibliotecas, crie duas variáveis de ambiente. Na linha de comando, digite:

* `export BOT_API_TOKEN="seu_token_telegram"`

* `export GIPHY_API_TOKEN="seu_token_giphy"`


## Execução
* Navegue para a pasta `src`
* Na linha de comando, digite `python3 pybot.py`

