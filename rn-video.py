'''Скрипт переименовывает видеофайлы в текущем каталоге: добавляет к названию файла его продолжительность.'''

import os
import time
from mutagen.mp4 import MP4


def my_time_format(time_string):
    '''Отсекаем нули от строкового формата времени'''
    for i in time_string:
        if i in '123456789':
            return time_string
        time_string = time_string[1:]


answer = input(
    'Будет произведено переименование файлов. Введите "у" или Enter чтобы продолжить: ')

if answer == 'y' or answer == '':
    list_video_files = [item
                        for item in os.listdir()
                        if os.path.isfile(item) and item.endswith(('.mp4', '.avi', '.mkw'))]

    for file in list_video_files:
        file_duration_seconds = int(MP4(file).info.length)
        time_string = time.strftime("%H-%M-%S", time.gmtime(file_duration_seconds))
        time_string = my_time_format(time_string)
        os.rename(file, file[:-4] + ' ' + time_string + file[-4:])
