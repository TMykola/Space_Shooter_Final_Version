pyinstaller --noconsole --onefile main.py -p function.py -p data.py --hidden-import pygame --hidden-import os --hidden-import random --add-data "image:image"
