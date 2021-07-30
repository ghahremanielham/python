from telegram.ext import Updater , CommandHandler , MessageHandler , Filters , CallbackQueryHandler
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore , Style
from password import username , password
import random
import os
import time
token = Updater('1863100350:AAFG0pG-P86ZDv9BE7lCd1sNa4rnxHnNTU4' , use_context=True)

def start(update , context):
    key = [[InlineKeyboardButton('وبسایت تک وان 24' , callback_data='1' ,'شماره تماس' , callback_data='3')] , [InlineKeyboardButton('کانال تک وان 24' , callback_data='2' ,'آدرس ما' , callback_data='4')
    key_2 = InlineKeyboardMarkup(key)
    context.bot.send_message(chat_id= update.message.chat_id , text='سلام به ربات تک وان 24 اومدید.')
    context.bot.send_message(chat_id= update.message.chat_id , text= 'دکمه مورد نظر خود را انتخاب نمایید',reply_markup=key_2)

def contact(update , context):
    options = webdriver.ChromeOptions()
    options.headless = True

    addresss = os.path.abspath(__file__)
    addresss = os.path.dirname(addresss)
    addresss = os.path.join(addresss, 'chromedriver.exe')

    driver = webdriver.Chrome(executable_path=addresss, options=options)

    os.system('cls')
    driver.get('https://techone24.com')

    time.sleep(2)

    t = driver.find_element_by_xpath('//*[@id="app"]/section[3]/div/div/div[1]/p[1]').text
    query = update.callback_query
    context.bot.send_message(chat_id=query.message.chat_id, text=t)
    

def send_location(update, context):
    chat_id = update.message.chat_id
    context.bot.sendLocation(chat_id, '37.213975', '50.001957')
def techone24_info(update , context):
    query = update.callback_query
    if (query.data == '1'):
        context.bot.send_message(chat_id=query.message.chat_id , text='https://techone24.com')
    if query.data == '2':
        context.bot.send_message(chat_id= query.message.chat_id , text= "@techone24")
    if query.data == '3':
        token.dispatcher.add_handler(CommandHandler('contact', contact)
    if query.data == '4':
        token.dispatcher.add_handler(CommandHandler('location', send_location))


token.dispatcher.add_handler(CommandHandler('start' , start))
token.dispatcher.add_handler(CallbackQueryHandler(techone24_info))
token.start_polling()
token.idle()