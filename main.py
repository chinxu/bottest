from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
 
def kimdong(update: Update, context: CallbackContext) -> None:
    kim_lich = requests.get("https://nxbkimdong.com.vn/blogs/lich-phat-hanh-sach-dinh-ky")
    soup_kimlich = BeautifulSoup(kim_lich.text,"html.parser")
    mydiv_kim = soup_kimlich.findAll('div',{'class':'article-title'})
    div_final = []
    for div in mydiv_kim:
        div1 = div.a.get('href')
        div2 = "https://nxbkimdong.com.vn" + div1
        div_final.append(div2)
    update.message.reply_text(f'Lịch phát hành nhà xuất bản Kim Đồng\n {div_final[0]} ')

updater = Updater('5276260976:AAEajvvhXvrfAyeeAzFg_hz7cD6llZjwnwE')


updater.dispatcher.add_handler(CommandHandler('kimdong', kimdong))

updater.start_polling()
updater.idle()