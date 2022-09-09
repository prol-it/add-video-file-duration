## Add video file duration

### Краткое описание:

Переименовывает видеофайл путем добавления к названию файла его продолжительность.

### Стек:

Python

### Полное описание:

Скрипт переименовывает видеофайл(ы) - добавляет к названию файла его продолжительность в формате HH-MM-SS. К примеру:

`My video 1-23-06.mp4`

Передаваемые параметры:

| Параметр           | Описание                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| -f 'file1' 'file2' | Обрабатывает не все файлы в текущем каталоге (этот режим по умолчанию), а только указанные после ключа '-f'. |
| -c                 | Конвертирует название файла в вид: Первая буква заглавная, остальные строчные                                |
| -d                 | Переносит все файлы из вложенных папок в текущую директорию (откуда запустили скрипт)                        |

### Инструкция по запуску:

Перейти в папку со скриптом. Выполнить в терминале:

`python rn.py [параметры]`


### Для запуска скрипта из любой директории без указания команды python (инструкция для Linux):

1. Файл должен содержать корректную shebang строку на самом верху - путь до интерпретатора Python, например:

	`#!/usr/bin/python3`

	Чтобы найти путь к вашему интерпретатору python на вашем компьютере, вы можете запустить команду в терминале:

	`which python`

2. Файл должен находиться в одной из директорий, указанной в $PATH. Узнать путь можно выполнив в терминале:

	`$ echo $PATH`

3. Файл должен быть исполняемым. Выполняем в терминале:

	`$ chmod +x rn.py`
