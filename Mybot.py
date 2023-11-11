import telegram
import time
bot_token = ''
chat_id = ''

bot = telegram.bot(token=bot_token)

print(bot.get_me()) 

while True:
bot.send_message(chat_id=chat_id, text='Hola mundo, este es nuestro primer programa con la api de telegram')
time.sleep(5)
