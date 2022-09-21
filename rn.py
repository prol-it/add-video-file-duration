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


def add_duration(file_name, time_string):
    '''Добавляем к названию файла его продолжительность, если она не указана'''

    if not (file_name[-2:].isdigit() and file_name[-3:-2] == '-'):
        file_name = file_name + ' ' + time_string

    return file_name


def change_bracket(file_name):
    '''Убираем всю информацию в круглых скобках за исключением качества видеофайла '''

    brackets_start_position = file_name.rfind('(')
    brackets_end_position = file_name.rfind(')')
    file_quality_position = file_name.find('p', brackets_start_position, brackets_start_position + 7)
    if brackets_start_position != -1 and file_quality_position != -1:
        file_name = file_name[:file_quality_position + 1] + ')' + file_name[brackets_end_position + 1:]

    return file_name


if __name__ == "__main__":

    answer = input(
        'Будет произведено переименование файла(ов). Введите "у" или Enter чтобы продолжить: ')

    if answer == 'y' or answer == '':

        if '-dir' in argv:
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
            file_name = file[:-4]
            file_extension = file[-4:]

            if '-c' in argv:
                file_name = file_name.capitalize()

            if '-b' in argv:
                file_name = change_bracket(file_name)

            file_name = add_duration(file_name, time_string)
            os.rename(file, file_name + file_extension)
