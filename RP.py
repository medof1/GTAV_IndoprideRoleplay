import pyautogui
import time
import keyboard
import pydirectinput
from playsound import playsound

right = 0
con, grey = 0.8, True #Confident
screen = (0,0,1920,1080) #Screen that will be processed
screen0 = screen
state,prevState = 0,0 #Switching between function
pos = None
prevPos = None
berak = False
birux, biruy = 0,0
x1,y1,x2,y2 = 0,0,0,0

#ADDITIONAL FUNCTION

def locate(image,cursor):
    global id, char, con, screen,grey,pos
    pos = pyautogui.locateCenterOnScreen(image, region= screen, grayscale= grey, confidence= con)
    if pos != None:
        if cursor == True:
            x, y = pos
            pyautogui.moveTo(x, y, 0.1) 
            if right == 1:
                pyautogui.mouseDown(button='right')
                time.sleep(.1)
                pyautogui.mouseUp(button='right')
            else:
                pyautogui.mouseDown()
                time.sleep(.1)
                pyautogui.mouseUp()
        return True
    else:
        return False

def printing():
    global state, prevState, id, char
    if state != prevState:
        if state == 0:
            print("all function Deadactived")
            playsound('asset/off.mp3')
        if state == 1:
            print("RP_Jahit Benang activated")
            playsound('asset/on.mp3')
        if state == 2:
            print("RP_Jahit Kain ranting activated")
            playsound('asset/on.mp3')
        if state == 3:
            print("RP_Jahit Kain daun activated")
            playsound('asset/on.mp3')
        if state == 6:
            print("RP_Jahit Kain akar activated")
            playsound('asset/on.mp3')
        if state == 5:
            print("RP_Jahit Pakaian activated")
            playsound('asset/on.mp3')
        if state == 6:
            print("RP_Tanam activated")
            playsound('asset/on.mp3')
        if state == 98:
            print("Ready to function")
        if state == 99:
            print("Function is completed")
            state = 0
        if state == 100:
            print("Function is under construction")
            state = 0
        prevState = state

def switch():
    global state
    if keyboard.is_pressed('ctrl+num 0') == True:
        state = 0   
        printing()  
    elif keyboard.is_pressed('ctrl+num 1') == True:
        state = 1 
        printing()    
    elif keyboard.is_pressed('ctrl+num 2') == True:
        state = 2    
        printing()    
    elif keyboard.is_pressed('ctrl+num 3') == True:
        state = 3
        printing()
    elif keyboard.is_pressed('ctrl+num 4') == True:
        state = 4
        printing()
    elif keyboard.is_pressed('ctrl+num 5') == True:
        state = 5
        printing()
    elif keyboard.is_pressed('ctrl+num 6') == True:
        state = 6
        printing()

def undercons():
    global state
    time.sleep(1)
    state = 100
    printing()

#MAIN FUNCTION    

def analog():
    global x1,y1,x2,y2,screen, screen0
    wasd = 0
    done = 0
    if locate('asset/w.png',False) == True or locate('asset/a.png',False) == True or locate('asset/s.png',False) == True or locate('asset/d.png',False) == True:
        wasd = 1
    if wasd != 0:
        while done == 0:
            x2 = []
            y2 = []
            pic = pyautogui.screenshot(region=(900,480,120,120))
            width, height = pic.size
            for x in range(0, width, 1):
                for y in range(0, height, 1):
                    r, g, b = pic.getpixel((x, y))
                    if r == 25 and g == 113 and b == 194 and x != x1 and y != y1:
                        x2.append(x)
                        y2.append(y)
                        x1 = x
                        y1 = y
            #print(x2,y2)
            tend = time.time() + 3
            while time.time() < tend:
                pic = pyautogui.screenshot(region=(900,480,120,120))
                for a in range(0, len(x2)):
                    x = x2[a]
                    y = y2[a]
                    r, g, b = pic.getpixel((x, y))
                    if r == 255 and g == 0 and b == 0:
                        pydirectinput.keyDown('w')
                        pydirectinput.keyDown('a')
                        pydirectinput.keyDown('s')
                        pydirectinput.keyDown('d') 
                        pydirectinput.keyUp('w')
                        pydirectinput.keyUp('a')
                        pydirectinput.keyUp('s')
                        pydirectinput.keyUp('d')
                        #print("MERAH SPOTTED", x,y) 
                        break
            done = 1

def benang():
    if locate('asset/membuat.png',False) == False and locate('asset/w.png',False) == False and locate('asset/a.png',False) == False and locate('asset/s.png',False) == False and locate('asset/d.png',False) == False:
        pydirectinput.keyDown('alt')
        pydirectinput.leftClick()
        locate('asset/proses.png',True)
        time.sleep(.01)
        locate('asset/benang.png',True)
        pydirectinput.keyUp('alt')
    #analog()

def kainranting():
    if locate('asset/membuat.png',False) == False and locate('asset/w.png',False) == False and locate('asset/a.png',False) == False and locate('asset/s.png',False) == False and locate('asset/d.png',False) == False:
        pydirectinput.keyDown('alt')
        pydirectinput.leftClick()
        locate('asset/proses.png',True)
        time.sleep(.01)
        locate('asset/kainranting.png',True)
        pydirectinput.keyUp('alt')
    #analog()

def kaindaun():
    if locate('asset/membuat.png',False) == False and locate('asset/w.png',False) == False and locate('asset/a.png',False) == False and locate('asset/s.png',False) == False and locate('asset/d.png',False) == False:
        pydirectinput.keyDown('alt')
        pydirectinput.leftClick()
        locate('asset/proses.png',True)
        time.sleep(.01)
        locate('asset/kaindaun.png',True)
        pydirectinput.keyUp('alt')
    #analog()

def kainakar():
    if locate('asset/membuat.png',False) == False and locate('asset/w.png',False) == False and locate('asset/a.png',False) == False and locate('asset/s.png',False) == False and locate('asset/d.png',False) == False:
        pydirectinput.keyDown('alt')
        pydirectinput.leftClick()
        locate('asset/proses.png',True)
        time.sleep(.01)
        locate('asset/kainakar.png',True)
        pydirectinput.keyUp('alt')
    #analog()

def pakaian():
    if locate('asset/membuat.png',False) == False and locate('asset/w.png',False) == False and locate('asset/a.png',False) == False and locate('asset/s.png',False) == False and locate('asset/d.png',False) == False:
        pydirectinput.keyDown('alt')
        pydirectinput.leftClick()
        locate('asset/proses.png',True)
        time.sleep(.01)
        locate('asset/pakaian.png',True)
        pydirectinput.keyUp('alt')
    #analog()

w = 0

def autoTanam():
    if locate('asset/menanam.png',False) == False:
        pydirectinput.keyDown('3')
        time.sleep(.01)
        pydirectinput.keyUp('3')
        #analog()

print("""Command List (Press ctrl + shift + number below):
num 0: Deadactive all function
num 1: RP_Jahit Benang
num 2: RP_Jahit Kain ranting
num 3: RP_Jahit Kain daun
num 4: RP_Jahit Kain akar
num 5: RP_Jahit Pakaian
num 6: RP_Tanam
""")
while(1):
    if state == 0:
        time.sleep(.1)
        if keyboard.is_pressed('ctrl') == True:
            state = 98
            printing()
    elif state != 0:
        switch()
    if keyboard.is_pressed('shift') == True and state != 0:
        playsound('asset/off.mp3')
        print("shift is pressed")
        while 1:
            if keyboard.is_pressed('enter') == True:
                playsound('asset/on.mp3')
                print("shift is done")
                break
    elif state == 1:
        benang()
    elif state == 2:
        kainranting()
    elif state == 3:
        kaindaun()
    elif state == 4:
        kainakar()
    elif state == 5:
        pakaian()
    elif state == 6:
        autoTanam()
    elif berak == True:
        break
