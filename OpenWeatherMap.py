#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pyowm

print('OpenWeatherStreetMap')
owm = pyowm.OWM('064d738c6654705a34f871442c36f814')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()

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
print('Wind: ' + str(weather.get_wind()))


def whatiscloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'clear'

    if 10 < weather.get_clouds() <= 30:
        return 'mostly clear'

    if 30 < weather.get_clouds() <= 70:
        return 'mostly clouds'

    if 70 < weather.get_clouds() <= 100:
        return 'clouds'


def what_now_time():
    a = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(int(observation.get_reception_time('unix'))))
    return str(a)[17] + str(a)[18] + str(a)[19] + str(a)[20] + str(a)[21]


def whatiswind():
    try:
        if 355 <= weather.get_wind()['deg'] <= 5:
            return 'north'
        if 5 < weather.get_wind()['deg'] <= 85:
            return 'north west'
        if 85 < weather.get_wind()['deg'] <= 95:
            return 'west'
        if 95 < weather.get_wind()['deg'] <= 175:
            return 'south west'
        if 175 < weather.get_wind()['deg'] <= 185:
            return 'south'
        if 185 < weather.get_wind()['deg'] <= 265:
            return 'south east'
        if 265 < weather.get_wind()['deg'] <= 275:
            return 'east'
        if 275 < weather.get_wind()['deg'] < 355:
            return 'horth east'
    except:
        pass


"""Погода в городе Москва (Россия) на сегодня в 10:15 солнечная, облачность
составляет 5%, давление 760 мм рт. ст., температура 20 градусов Цельсия, ночью 8
днем 25 градусов Цельсия, ветер северо-западный, 5 м/с.

print('Weather in the ' + location.get_name() + '(' + location.get_country() + ')' +
      ' city, today at  ' + what_now_time() + str(whatiscloudness()) +
      ', oblachnost  ' + str(weather.get_clouds()) + '%, ' +
      'pressure' + str(weather.get_pressure()['press']) +
      ' mm. hg. st.  temperature ' + str(weather.get_temperature('celsius')['temp']) +
      'by celsius, wind ' + str(whatiswind()) + str(weather.get_wind()['speed']) + ' m/s')
"""

print(whatiswind())