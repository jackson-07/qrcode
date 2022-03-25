import pyqrcode
import os, shutil

file_name_png = "qrcode" + ".png"

url = pyqrcode.create("https://jackson-07.github.io/blog/")

url.png(file_name_png, scale=8)
