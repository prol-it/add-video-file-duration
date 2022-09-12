import os
import time
from mutagen.mp4 import MP4
from sys import argv

searched_files = ('.mp4', '.avi', '.mkw')
list_video_files = []


def move_files_in_current_dir():
    '''Перемещам все видеофайлы, которые находятся во вложенных папках в текущий каталог'''
    for adress, dirs, files in os.walk(os.curdir):
        for file in files:
            full = os.path.join(adress, file)
            if full.endswith(searched_files):
                os.replace(full, file)


def my_time_format(time_string):
    '''Отсекаем нули от строкового формата времени'''
    for i in time_string:
        if (i in '123456789') or (len(time_string) == 4):
            return time_string
        time_string = time_string[1:]


def file_contains_duration(file):
    '''Смотрим, может быть файл уже содержит продолжительность и его не нужно второй раз переименовывать'''

    if file[-6:-4].isdigit() and file[-7:-6] == '-':
        return True

    return False


if __name__ == "__main__":

    answer = input(
        'Будет произведено переименование файла(ов). Введите "у" или Enter чтобы продолжить: ')

    if answer == 'y' or answer == '':

        if '-d' in argv:
            move_files_in_current_dir()

        if '-f' in argv:
            current_item_index = argv.index('-f') + 1
            while current_item_index < len(argv):
                list_video_files.append(argv[current_item_index])
                current_item_index += 1

        if len(list_video_files) == 0:
            list_video_files = [item
                                for item in os.listdir()
                                if os.path.isfile(item) and item.endswith(searched_files)]

        for file in list_video_files:
            file_duration_seconds = int(MP4(file).info.length)
            time_string = time.strftime("%H-%M-%S", time.gmtime(file_duration_seconds))
            time_string = my_time_format(time_string)
            file_contains_duration(file)
            if not file_contains_duration(file):
                if '-c' in argv:
                    os.rename(file, file[:-4].capitalize() + ' ' + time_string + file[-4:])
                else:
                    os.rename(file, file[:-4] + ' ' + time_string + file[-4:])
