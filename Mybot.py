import telegram
import time
bot_token = '1976663319:AAEjQ-w-owZ8D4JFSWewUwCTJQZ0_l2Txz0'
chat_id = '-1001385780804'

bot = telegram.bot(token=bot_token)

print(bot.get_me()) 

while True:
bot.send_message(chat_id=chat_id, text='Hola mundo, este es nuestro primer programa con la api de telegram')
time.sleep(5)
