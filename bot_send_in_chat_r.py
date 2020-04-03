#-------------------------------------------------------------------------------
# Name:        send message telegram channel
# Purpose:
#
# Author:      Admin
#
# Created:     04.02.2020
# Copyright:   (c) Admin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Name:        send message telegram channel
# Purpose:
#
# Author:      Admin
#
# Created:     04.02.2020
# Copyright:   (c) Admin 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
import telebot
from time import sleep
from bs4 import BeautifulSoup


bot = telebot.TeleBot('1018248796:AAE25EIuIoDqEU5iRvP7saI2Curb4UmQlQM')
channel = "@COVID_2019_R"

def main():
    url = "https://yandex.ru/covid19"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }

    r = requests.get(url, headers = headers)

    soup = BeautifulSoup(r.text, 'html5lib')
    table = soup.findChildren('b')

    date = []
    for i in table[0:4]:
        k = str(i)
        date.append(k[3:-4])

    valumes = {'confirmed': date[0], 'cured': date[1], 'deaths': date[2], 'test': date[3]}




    bot.send_message(channel, 'Заражено {} \U0001f3e5'.format(valumes['confirmed'])
    + '\n' + '\n' +
    'Погибло {} \U000026b0'.format(valumes['deaths'])
    + '\n' + '\n' +
    'Выздоровело {} \U0001f4aa'.format(valumes['cured'])
    + '\n' + '\n' +
    'Сделано тестов {} \U0001F52C'.format(valumes['test']))



if __name__ == '__main__':
    main()
    sleep(60*60*24)



