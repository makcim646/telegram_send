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
import threading

from time import sleep



bot = telebot.TeleBot('1018248796:AAE25EIuIoDqEU5iRvP7saI2Curb4UmQlQM')

channel = "@virus_nCoV_2019"

def main():
    valumes = []



    urls = {"recovery":"https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Recovered%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true",
        "dead":"https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Deaths%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true",
        "confirm":"https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/ncov_cases/FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&outStatistics=%5B%7B%22statisticType%22%3A%22sum%22%2C%22onStatisticField%22%3A%22Confirmed%22%2C%22outStatisticFieldName%22%3A%22value%22%7D%5D&cacheHint=true"
        }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }


    for key, url in urls.items():
        r = requests.get(url, headers = headers)
        val = r.json()['features'][0]['attributes']['value']
        valumes.append({key:int(val)})

    print(valumes)


    with open('recovery', 'r+') as f:
        f.read()
        f.seek(0)
        f.write(str((valumes[0]['recovery'])))

    with open('dead', 'r+') as f:
        num_dead_old = int(f.readline())
        num_dead_new = int((valumes[1]['dead']))
        print(num_dead_old, num_dead_new)
        f.seek(0)
        if num_dead_old < num_dead_new:
            bot.send_message(channel, 'I killed {} more \U00002620'.format(num_dead_new - num_dead_old))
            sleep(5)
            bot.send_message(channel, 'Total Deaths {} \U000026b0'.format(str((valumes[1]['dead']))))
        f.write(str((valumes[1]['dead'])))

    with open('confirm', 'r+') as f:
        f.read()
        f.seek(0)
        f.write(str((valumes[2]['confirm'])))


def send_statistic_all():
    with open('recovery', 'r') as f:
        recovery = int(f.readline())
    with open('dead', 'r') as f:
        dead = int(f.readline())
    with open('confirm', 'r') as f:
        confirm= int(f.readline())

    print(channel, 'Total Confirmed {}'.format(confirm)
    + '\n' +
    'Total Deaths {}'.format(dead)
    + '\n' +
    'Total Recovered {}'.format(recovery))


    bot.send_message(channel, 'Total Confirmed {} \U0001f3e5'.format(confirm)
    + '\n' + '\n' +
    'Total Deaths {} \U000026b0'.format(dead)
    + '\n' + '\n' +
    'Total Recovered {} \U0001f4aa'.format(recovery))



if __name__ == '__main__':
    n = 0
    while True:
        sleep(60*15)
        e1 = threading.Event()
        if n%20 == 0:
            e2 = threading.Event()

        t1 = threading.Thread(target=main)
        if n%20 == 0:
            t2 = threading.Thread(target=send_statistic_all)

        t1.start()
        if n%20 == 0:
            t2.start()

        n += 1




