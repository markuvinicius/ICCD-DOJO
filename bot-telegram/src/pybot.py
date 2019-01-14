# encoding=utf8
import os
import logging
import logging.handlers
from telegram.ext import CommandHandler
from telegram.ext import Updater
import pygiphy


def start(bot, update):
    logger.info('start')
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def gif(bot, update):
    logger.info('gif')
    logger.info(update['message']['text'])
    query = pygiphy.get_query_string(update['message']['text'], pygiphy.get_token())
    logger.info(query)
    call = pygiphy.get_giphy_endpoint(query)
    animation = pygiphy.get_gif(call)
    logger.info(pygiphy.get_gif(call))
    bot.send_animation(update.message.chat_id, animation, disable_notification=False, timeout=20)

    
def foaas(bot,update):
    logger.info('foaas - http://www.foaas.com/')

def tempo(bot,update):
    logger.info('tempo - https://openweathermap.org/current')




if __name__ == "__main__":
    LOG_FILENAME = 'pybot.out'
    
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
    gif_handler   = CommandHandler('gif', gif)
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