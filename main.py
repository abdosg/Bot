import telebot 
import requests
bot=telebot.TeleBot('6394038471:AAFfVdEct477t-XDFry5ZZmqZO-km2zXfNU')
@bot.message_handler(commands=['start'])
def cc(message):
	bot.send_message(message.chat.id,'مرحبا بك')
@bot.message_handler(func=lambda messge:True)
def kk(message):
	mm=1
	if 'بحث' in message.text:
		try:
			m=message.text.split('بحث ')[1]
			gg=requests.get(f'https://api-quran.cf/quransql/index.php?text={m}&type=search').json()
			bot.send_message(message.chat.id,gg['result'])
		except:
			bot.reply_to(message,'يرجى كتابة اية بشكل صحيح')
	elif 'فسر' in message.text:
		try:
			m=message.text.split('فسر')[1]
			oo=requests.get(f'https://api-quran.cf/quransql/index.php?text={m}&type=tafser1').json()['result']
			bot.send_message(message.chat.id,oo)
		except:
			bot.reply_to(message,'يرجى كتابة اية بشكل صحيح')
		
		
		




bot.polling()
