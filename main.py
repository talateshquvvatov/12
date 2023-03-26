import requests
from telebot import *
bot=TeleBot('6031138492:AAEDF2lmckNYA2ktszIxEVknbpZaggLCX74')


@bot.message_handler(func=lambda message: message.chat.type == 'private')
def main(msg: types.Message):
        res= requests.get(f"http://ip-api.com/json/{msg.text}")
        startt=f""""
👋 Assalomu alaykum {msg.from_user.full_name}
Ip aniqlovchi botga xush kelibsiz

🖥 Bot foydalanish uchun ip manzil yuboring!

📕 Namuna: 103.101.91.255
        
        """
        if msg.text.startswith("/start"):
            bot.send_message(msg.chat.id,startt)
        else:
            try:
                botinfo=bot.get_me()
                kb1=types.InlineKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
                btn1=types.InlineKeyboardButton("Botni guruhga qo'shish",url=f"t.me/{botinfo.username}?startgroup=new")
                btn2=types.InlineKeyboardButton("Bot Admini",url="t.me/Men1man")
                kb1.add(btn1)
                kb1.add(btn2)
                x=res.json()
                ip=f"""
✉️  Davlati: ({x['country']})
📖  Shaxari : ({x['regionName']})
📬  Zip code : ({x['zip']})
💎 Davlat codi : ({x['countryCode']})
🎩 Shaxar codi : ({x['region']})
⚙️ Vaqt mintaqasi : ({x['timezone']})
                
                
                
                """
                loc=bot.send_location(msg.chat.id,x['lat'],x['lon'])
                bot.send_message(msg.chat.id,ip,reply_markup=kb1,reply_to_message_id=loc.message_id)
            except:
                bot.send_message(msg.chat.id,"Bunday ip mavjud emas !!!")

bot.polling()
