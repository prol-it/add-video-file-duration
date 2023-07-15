import os
import time
from mutagen.mp4 import MP4
from sys import argv

searched_files = ('.mp4', '.avi', '.mkw')
list_video_files = []


def move_files_in_current_dir():
    '''Move all video files that are in subfolders to the current directory'''
    for adress, dirs, files in os.walk(os.curdir):
        for file in files:
            full = os.path.join(adress, file)
            if full.endswith(searched_files):
                os.replace(full, file)


def seconds_to_string_format(seconds):
    '''Convert the number of seconds to string format'''
    time_string = time.strftime("%H-%M-%S", time.gmtime(seconds))
    for i in time_string:
        if (i in '123456789') or (len(time_string) == 4):
            break
        time_string = time_string[1:]

    return time_string


def change_bracket(file_name):
    '''We remove all information in brackets except for the resolution of the video file'''
    brackets_start_position = file_name.rfind('(')
    brackets_end_position = file_name.rfind(')')
    file_quality_position = file_name.find('p', brackets_start_position, brackets_start_position + 7)
    if brackets_start_position != -1 and file_quality_position != -1:
        file_name = file_name[:file_quality_position + 1] + ')' + file_name[brackets_end_position + 1:]

    return file_name


answer = input(
    'The file(s) will be renamed. Type "y" or Enter to continue: ')

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

    sum_seconds = 0
    for file in list_video_files:
        file_name = file[:-4]
        file_extension = file[-4:]

        if '-c' in argv:
            file_name = file_name.capitalize()

        if '-b' in argv:
            file_name = change_bracket(file_name)

        file_duration_seconds = int(MP4(file).info.length)
        sum_seconds += file_duration_seconds

        # Add the duration of the file to the file name if it is not specified
        if not (file_name[-2:].isdigit() and file_name[-3:-2] == '-'):
            time_string = seconds_to_string_format(file_duration_seconds)
            os.rename(file, file_name + ' ' + time_string + file_extension)

    print(f'Total time of video files: {seconds_to_string_format(sum_seconds)}')
