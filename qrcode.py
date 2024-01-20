import pyqrcode
import os, shutil

file_name_png = "qrcode" + ".png"

url = pyqrcode.create("insert web page here")

url.png(file_name_png, scale=8) 
