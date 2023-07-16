# Video File Renamer  

This script renames video files by adding their duration to the file name in the format HH-MM-SS.  
  
## Description  

The script renames video file(s) by appending their duration to the file name in the format HH-MM-SS. For example:  
  
`My video 1-23-06.mp4  `
  
Command-line options:  

| Option             | Description                                                                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -f 'file1' 'file2' | Processes only the specified files after the '-f' option instead of all files in the current directory.                                                                                                                          |
| -c                 | Converts the file name to title case (the first letter capitalized, the rest lowercase).                                                                                                                                         |
| -dir               | Moves all files from subfolders to the current directory (where the script is run from).                                                                                                                                         |
| -b                 | Removes unnecessary information in parentheses, leaving only the video quality information. For example, from <br/>'Django REST Framework (720p_25fps_H264-192kbit_AAC).mp4' it becomes <br/>'Django REST Framework (720p).mp4'. |


## Running the Project in Development Mode  

Clone the repository:  

```
git clone git@github.com:prol-it/add-video-file-duration.git  
```

Navigate to the project directory:  

```
cd add-video-file-duration  
```

Create and activate a virtual environment:

```
python3 -m venv venv  
source venv/bin/activate  
```  

Install the dependencies:

```
python3 -m pip install --upgrade pip  
pip install -r requirements.txt  
```  

Navigate to the script directory. Run the following command in the terminal:

```
python3 rn.py [options]  
```

## Making the Script Executable from Any Directory without Specifying the Python Command (Linux Instructions)  

1. The file should have a correct shebang line at the top, indicating the path to the Python interpreter, for example:
`#!/usr/bin/python3`
To find the path to your Python interpreter on your computer, you can run the following command in the terminal:
`which python`
2. The file should be located in one of the directories listed in $PATH. You can find the directories by executing the following command in the terminal:  
`$ echo $PATH`
The file should be executable. Run the following command in the terminal:
`$ chmod +x rn.py`
Feel free to modify and enhance the script to meet your specific needs!
