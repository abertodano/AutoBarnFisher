#screenshoting
import pyautogui 
#image processing
import os
from PIL import Image
from pytesseract import pytesseract
#calling the function to start
import threading
#macroing
import time
import pydirectinput
#taking inputs
from pynput import keyboard
#mouse movements require MouseKeys in OS, Controls -> Mouse Settings -> Raw Input: OFF

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#Define path to image
screenshot_path = r'screenshots/screen.png'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
#identify screen region containing subtitles
reg = (1693,856,1920,982)

def ReadScreen():
    #take screenshot with pyautogui
    sc = pyautogui.screenshot(region=reg)
    
    #sc.save(screenshot_path) #turns out saving+loading image not necessary, stored by pyautogui.screenshot and read by pytesseract in Python Imaging Library format. Use for debugging.
    #Open image with PIL
    #img = Image.open(screenshot_path)
    #Extract text from image
    
    text = pytesseract.image_to_string(sc)
    return text

#main loop
def fish():
    global running
    time.sleep(0.5) #so that shift doesn't take effect right away
    pydirectinput.keyDown('shift') #shift-walk forward the whole time to counteract knockback from sea creatures
    pydirectinput.keyDown('w')
    
    while running:
        
        
        pydirectinput.click(button='right') #cast fishing rod
        time.sleep(4) #wait for first "splashing" to fade out
        nosplash = True
        while nosplash: #continually read subtitles for splash
            text = ReadScreen()
            if "Splashing" in text: #if "splashing" found,continue to next part of loop
                nosplash = False
        pydirectinput.click(button='right') #retract fishing rod
        time.sleep(0.2) #wait a short time before casting again
     
    pydirectinput.keyUp('w')
    pydirectinput.keyUp('shift') #end shift-walking
    return

#function to check presses and toggle a thread with fish()
def on_press(key):
    global running
    if key == keyboard.KeyCode(vk=None, char='F'):
        running ^= True #toggle running on pressing 'F'
        if running: #start fish() if now running = True ( fish() stopped if now running = False by while statement in fish() )
            t = threading.Thread(target=fish)
            t.start()
    return
    
def on_release(key):
    return

#runner

running = False #default to off so you're not jumped when you start the script
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: #setup the listener
    listener.join() #run the listener, which itself toggles the script
    
#python AutoBarnFisher/Auto.py