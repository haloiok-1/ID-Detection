import csv
from PIL import Image
import easyocr as ocr
import cv2
import pyautogui as pg
import numpy as np
import keyboard
import os

FILEPATH = os.getcwd()
IMG_NAME = "IDPhoto.png"
IMG_PATH = os.path.join(FILEPATH, "img", IMG_NAME)



mcIDpos = [1500, 280, 420, 20]
x1 = mcIDpos[0]
y1 = mcIDpos[1]
x2 = mcIDpos[0] + mcIDpos[2]
y2 = mcIDpos[1] + mcIDpos[3]

os.chdir("img")

def calc_xy(x, y, w, h):
    mcIDpos = [x, y, w, h]
    x1 = mcIDpos[0]
    y1 = mcIDpos[1]
    x2 = mcIDpos[0] + mcIDpos[2]
    y2 = mcIDpos[1] + mcIDpos[3]

    return x1, y1, x2, y2

def textdetection(Filepath=IMG_PATH):
        # Textdetetion
        reader = ocr.Reader(["en"], gpu= True)
        img = cv2.imread(IMG_PATH)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res = reader.readtext(gray)
        
        #Strip the Output for further processing
        Output = res[0][1]
        Output = Output[9:]

        return Output

def takescreenshot(Position=[x1, y1, x2, y2]):
        # Take Screenshot
        pg.screenshot(IMG_NAME)
        print("Screenshot taken")
        pg.sleep(1)
        
        #crop image to perfect size
        im = Image.open(IMG_PATH)
        im = im.crop((x1, y1, x2, y2))
        im.save(IMG_NAME)

def searchcsv(search_term):
    with open("IDs.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if search_term in row:
                print(row[3])
    return row[3] 

while True:

    #take Screenshot
    if keyboard.is_pressed("Alt+x"):
        
        takescreenshot(calc_xy(1500, 280, 420, 20))

        print(searchcsv(textdetection()))




        














    
