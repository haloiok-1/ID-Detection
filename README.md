# PipeID-Detection
Fully written in Python.
This tool is written for [Minecraft](https://www.minecraft.net) and adapted for [Secretcraft](https://secretcraft.de/).

## Why did I write this programme?
Since I have been playing on this Minecraft server for some time now, I have noticed a few things that could be improved. Over the course of time, many things have been improved, but some are still the same as before. One example of this is picking out the PipeIDs from a list with over 1000 entries. When you set yourself the goal of building a storage, it can be quite annoying to find the right ID for so many chests and the respective item to be stored in this chest quickly and efficiently. I have set myself the goal to simplify this process a bit. This is what I came up with. 

Furthermore, this is my first real project that I have successfully completed and that works. 

## How does it work?
The programme uses Minecraft's DebugHUD and recognises via text recognition which block the player is currently looking at. It should be noted that it is not **100%** possible for the text recognition to detect the Minecraft font correctly. To compensate for this, I have specified that if no matching ID is found, the player is notified that the OCR was not successful. However, if something is recognised, the matching ID is immediately copied to the clipboard. This makes it immediately available to the player without having to have to leave the game. 

The key combination to start the identification is ALT+X. To end the application, the key combination ALT + Y is used. 

## Technical requirements.
Since the programme is written in Python, it is necessary that it is also installed. It is also necessary that all modules that are needed in the programme are installed. 

The modules that are needed are:
 - pyautogui
 - OpenCV
 - EasyOCR
 - Pillow

If you don't know how to install Python modules click here: [Python Dictonary](https://docs.python.org/3/installing/index.html)

For this script to work, Windows is required as the operating system. However, I am not sure whether it will also work under Windows 11 without major problems. 
Mac OS is not supported as far as I know, because I used a Windows own function for copying to the clipboard, which is probably not supported under Mac OS. 


