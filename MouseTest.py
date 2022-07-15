#calling the function to start
import threading
#macroing
import pydirectinput
import time
#taking inputs
from pynput import keyboard

#test mouse moves
def on_press(key):
    if key == keyboard.KeyCode(vk=None, char='f'):
        #pos = pydirectinput.position()
        #print(pos)
        #center = 960,527
        #pydirectinput.moveTo(x=960, y=0)
        #pydirectinput.click()
        pydirectinput.keyDown('numpad4')
        time.sleep(1)
        pydirectinput.keyUp('numpad4')
return
        
#runner
with keyboard.Listener(on_press=on_press) as listener: #setup the listener
    listener.join() #run the listener
    
#python AutoBarnFisher/MouseTest.py