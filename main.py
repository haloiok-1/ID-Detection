import csv
from PIL import Image
import easyocr as ocr
import cv2
import pyautogui as pg
import keyboard
import os


FILEPATH = os.getcwd()
IMG_NAME = "IDPhoto.png"
IMG_PATH = os.path.join(FILEPATH, "img", IMG_NAME)
debug = True

os.chdir("img")

def resize_img(Filepath, shortside, factor):
    # Resize Image
    #open image
    img = Image.open(Filepath)
    #set size
    size = (shortside * factor, shortside)
    #resize image
    img = img.resize((size), Image.ANTIALIAS)
    img = img.resize((size), Image.ANTIALIAS)
    #save image
    img.save(IMG_PATH)
    if debug:
        print("Image resized")
    return 1

def toclipboard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

def calc_xy(x, y, w, h):
    mcIDpos = [x, y, w, h]
    x1 = mcIDpos[0]
    y1 = mcIDpos[1]
    x2 = mcIDpos[0] + mcIDpos[2]
    y2 = mcIDpos[1] + mcIDpos[3]

    return x1, y1, x2, y2

def textdetection(Filepath=""):
        # Textdetetion
        reader = ocr.Reader(["en"])
        img = cv2.imread(Filepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res = reader.readtext(gray)
        print(res)
        
        #Strip the Output for further processing
        if not res:
            Output = -1
        else:
            Output = res[0][1]
            Output = Output[9:]
            
        #debug
        if debug:
            print(Output)

        return Output

def takescreenshot(Position=("", "", "", "")):
        # Take Screenshot
        pg.screenshot(IMG_NAME)
        if debug:
            print("Screenshot taken")
        pg.sleep(0.1)
        
        #crop image to perfect size
        im = Image.open(IMG_PATH)
        im = im.crop(Position)
        if debug:
            print("Image cropped")
        im.save(IMG_NAME)
        if debug:
            print("Image saved")

def searchcsv(search_term, Filepath=""):
    with open(Filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        if debug:
            print("Search in CSV")

        for row in csv_reader:
            if search_term in row:
                if debug:
                    print("Found in CSV")
                    print(row)
                return row[3]
        
        if search_term == -1:
            if debug:
                print("Not found in CSV")
            return -1
                    
            
if debug:
    print("Program started")

while keyboard.is_pressed('Alt+y') == False:
    pg.sleep(0.05)
    #take Screenshot
    if keyboard.is_pressed("Alt+x"):
        
        #take Screenshot and resize image
        takescreenshot(calc_xy(1500, 283, 420, 18))
        resize_img("IDPhoto.png", 300, 24)

        #detect text
        text =  textdetection(IMG_PATH)

        #search in CSV
        PipeId = searchcsv(text, "IDs.csv")
        print("PipeId= " + str(PipeId))
        

        if PipeId == -1:
            #debug
            if debug:
                print("PipeID not found")
        else:
            #debug
            if debug:
                print("PipeID copied to clipboard")

            #copy to clipboard
            toclipboard(str(PipeId))
        
if debug:
    print("Program ended")

