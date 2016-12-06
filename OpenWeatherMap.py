#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pyowm

print('OpenWeatherStreetMap')
owm = pyowm.OWM('064d738c6654705a34f871442c36f814', language='ru')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

pog = owm.daily_forecast_at_coords(47.1426, 39.4238)
tomorrow = owm.daily_forecast('Rostov-on-Don,ru').get_weather_at(observation.get_reception_time() + 86400)

def whatiscloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясно'

    if 10 < weather.get_clouds() <= 30:
        return 'переменная облачность'

    if 30 < weather.get_clouds() <= 70:
        return 'преимущественно облачно'

    if 70 < weather.get_clouds() <= 100:
        return 'облачно'


def what_now_time():
    a = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(int(observation.get_reception_time('unix'))))
    return str(a)[17] + str(a)[18] + str(a)[19] + str(a)[20] + str(a)[21]


def whatiswind():
    try:
        if 355 <= weather.get_wind()['deg'] <= 5:
            return 'северный'
        if 5 < weather.get_wind()['deg'] <= 85:
            return 'северо-восточный'
        if 85 < weather.get_wind()['deg'] <= 95:
            return 'восточный'
        if 95 < weather.get_wind()['deg'] <= 175:
            return 'юго-восточный'
        if 175 < weather.get_wind()['deg'] <= 185:
            return 'южный'
        if 185 < weather.get_wind()['deg'] <= 265:
            return 'юго-западный'
        if 265 < weather.get_wind()['deg'] <= 275:
            return 'западный'
        if 275 < weather.get_wind()['deg'] < 355:
            return 'северо-западный'
    except:
        pass

print('Погода в городе ' + location.get_name() + '(' + location.get_country() + ')' +
      ' на сегодня, в ' + what_now_time() + str(whatiscloudness()) + " " +
      ', облачность ' + str(weather.get_clouds()) + '%, ' +
      ' давление ' + str(weather.get_pressure()['press']) +
      ' мм.рт.ст, температура ' + str(weather.get_temperature('celsius')['temp']) +
      ' градусов Цельсия, ветер ' + str(whatiswind()) + ', ' + str(
    weather.get_wind()['speed']) + ' m/s' + '. Завтра утром ' + str(
    tomorrow.get_temperature('celsius')['morn']) + ', днем ' + str(
    tomorrow.get_temperature('celsius')['day']) + ', вечером ' + str(
    tomorrow.get_temperature('celsius')['eve']) + ', ночью ' + str(tomorrow.get_temperature('celsius')['night']))
