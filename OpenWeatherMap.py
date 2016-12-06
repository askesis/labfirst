#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pyowm

print('OpenWeatherStreetMap')
owm = pyowm.OWM('064d738c6654705a34f871442c36f814', language='ru')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

# pog = pyowm.webapi25.forecast.Forecast('3h', 1480962594, 'Rostov-on-Don, ru', 'Rostov-on-Don, ru')

pog = owm.daily_forecast_at_coords(47.1426, 39.4238)
tomorrow = owm.daily_forecast('Rostov-on-Don,ru').get_weather_at(observation.get_reception_time() + 86400)


"""""
print(owm)
print(observation)
print(weather)
print(location)



print('Country : ' + location.get_country())
print('City : ' + location.get_name())
print('Lon: ' + str(location.get_lon()))
print('Lat: ' + str(location.get_lat()))
print('Clouds: ' + str(weather.get_clouds()))
print('Status: ' + str(weather.get_detailed_status()))
print('Pressure: ' + str(weather.get_pressure()))
print('Rain: ' + str(weather.get_rain()))
print('Snow: ' + str(weather.get_snow()))
print('Time: ' + str(weather.get_reference_time('iso')))
print('Status: ' + str(weather.get_status()))
print('Sunrise time: ' + str(weather.get_sunrise_time('iso')))
print('Sunset time: ' + str(weather.get_sunset_time('iso')))
print('Temperature: ' + str(weather.get_temperature('celsius')))
print('Visibility distance: ' + str(weather.get_visibility_distance()))
print('Image: ' + str(weather.get_weather_icon_name()))
"""


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


"""Погода в городе Москва (Россия) на сегодня в 10:15 солнечная, облачность
составляет 5%, давление 760 мм рт. ст., температура 20 градусов Цельсия, ночью 8
днем 25 градусов Цельсия, ветер северо-западный, 5 м/с.
"""
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
