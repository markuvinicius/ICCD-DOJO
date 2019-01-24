# encoding=utf8
import os
import logging.handlers
from telegram.ext import CommandHandler
from telegram.ext import Updater
import pygiphy
import weather


def start(bot, update):
    logger.info('start')
    bot.send_message(chat_id=update.message.chat_id, text="Tô aqui, amigão. Pode falar....")


def gif(bot, update):    
    logger.info("mensagem: " + update['message']['text'])
    query = pygiphy.get_query_string(update['message']['text'], pygiphy.get_token())    
    call = pygiphy.get_giphy_endpoint(query)
    animation = pygiphy.get_gif(call)    
    if animation is not None:
        bot.send_animation(update.message.chat_id, animation, disable_notification=False, timeout=20)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Foi mal aí, amigão. Não achei nenhum gif com essa frase bosta. Tenta outra :)")

    
def foaas(bot, update):
    logger.info('foaas - http://www.foaas.com/')


def tempo(bot, update):
    token = weather.get_token()
    print('Token - ' + token)
    query = weather.get_query_string(token)
    print('Query - ' + query)
    call = weather.get_endpoint(query)
    print('Endpoint - ' + call)
    message = weather.get_by_days(call)
    bot.send_message(chat_id=update.message.chat_id, text=message)
    logger.info(token)


if __name__ == "__main__":
    LOG_FILENAME = '../pybot.log'
    
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger = logging.getLogger('pybot')

    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=10737418240, backupCount=10)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.DEBUG)
    logger.info("Iniciando PyBot")

    updater = Updater(token=os.environ['BOT_API_TOKEN'])
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    gif_handler = CommandHandler('gif', gif)
    foaas_handler = CommandHandler('foaas', foaas)
    tempo_handler = CommandHandler('tempo', tempo)

    try:
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(gif_handler)
        dispatcher.add_handler(foaas_handler)
        dispatcher.add_handler(tempo_handler)

        updater.start_polling()
    except KeyboardInterrupt as e:
        logger.info("saindo")
