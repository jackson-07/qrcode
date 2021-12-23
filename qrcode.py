import pyqrcode
import os, shutil

file_name_png = "linkedin" + ".png"

url = pyqrcode.create("https://www.linkedin.com/in/jackson-raymond07/")

url.png(file_name_png, scale=8)
