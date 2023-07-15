import os
import time
from mutagen.mp4 import MP4
from sys import argv

SEARCHED_FILES = ('.mp4', '.avi', '.mkw')


def move_files_in_current_dir():
    '''
    Move all video files that are in subfolders to the current directory.
    '''
    for root, dirs, files in os.walk(os.curdir):
        for file in files:
            full_path = os.path.join(root, file)
            if full_path.endswith(SEARCHED_FILES):
                os.replace(full_path, file)


def seconds_to_string_format(seconds):
    '''
    Convert the number of seconds to string format.
    '''
    time_string = time.strftime("%H-%M-%S", time.gmtime(seconds))
    time_string = time_string.lstrip('-0')
    return time_string


def change_bracket(file_name):
    '''
    Remove all information in brackets except for the resolution of the video file.
    '''
    brackets_start_position = file_name.rfind('(')
    brackets_end_position = file_name.rfind(')')
    file_quality_position = file_name.find('p', brackets_start_position, brackets_start_position + 7)
    if brackets_start_position != -1 and file_quality_position != -1:
        file_name = file_name[:file_quality_position + 1] + ')' + file_name[brackets_end_position + 1:]
    return file_name


answer = input('The file(s) will be renamed. Type "y" or Enter to continue: ')

if answer == 'y' or answer == '':
    list_video_files = []

    if '-dir' in argv:
        move_files_in_current_dir()

    if '-f' in argv:
        file_index = argv.index('-f') + 1
        while file_index < len(argv):
            list_video_files.append(argv[file_index])
            file_index += 1

    if not list_video_files:
        list_video_files = [
            item for item in os.listdir() if os.path.isfile(item) and item.endswith(SEARCHED_FILES)
        ]

    total_duration = 0
    for file in list_video_files:
        file_name = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]

        if '-c' in argv:
            file_name = file_name.capitalize()

        if '-b' in argv:
            file_name = change_bracket(file_name)

        file_duration_seconds = int(MP4(file).info.length)
        total_duration += file_duration_seconds

        # Add the duration of the file to the file name if it is not specified
        if not (file_name[-2:].isdigit() and file_name[-3:-2] == '-'):
            time_string = seconds_to_string_format(file_duration_seconds)
            new_file_name = f'{file_name} {time_string}{file_extension}'
            os.rename(file, new_file_name)

    total_duration_string = seconds_to_string_format(total_duration)
    print(f'Total time of video files: {total_duration_string}')
