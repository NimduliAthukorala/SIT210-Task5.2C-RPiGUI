#Making a GUI
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##HArdware
ledblue = LED(4)
ledred = LED(2)
ledgreen = LED(3)


## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## EVENT FUNCTION ##
def ledtoggler1():
    if ledblue.is_lit:
        ledblue.off()
        ledButton1["text"] = "Turn LED on"
    else:
        ledblue.on()
        ledButton1["text"] = "Turn LED off"
        ledred.off()
        ledButton2["text"] = "Turn LED on"
        ledgreen.off()
        ledButton3["text"] = "Turn LED on"

def ledtoggler2():
    if ledred.is_lit:
        ledred.off()
        ledButton2["text"] = "Turn LED on"
    else:
        ledred.on()
        ledButton2["text"] = "Turn LED off"
        ledblue.off()
        ledButton1["text"] = "Turn LED on"
        ledgreen.off()
        ledButton3["text"] = "Turn LED on"

def ledtoggler3():
    if ledgreen.is_lit:
        ledgreen.off()
        ledButton3["text"] = "Turn LED on"
    else:
        ledgreen.on()
        ledButton3["text"] = "Turn LED off"
        ledblue.off()
        ledButton1["text"] = "Turn LED on"
        ledred.off()
        ledButton2["text"] = "Turn LED on"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()

## WIDGETS ##
ledButton1 = Button(win, text = 'Turn LED on', font = myFont, command = ledtoggler1,bg = 'SkyBlue',height=1, width =24)
ledButton1.grid(row=0,column=1)

ledButton2 = Button(win, text = 'Turn LED on', font = myFont, command = ledtoggler2,bg = 'FireBrick',height=1, width =24)
ledButton2.grid(row=0,column=2)

ledButton3 = Button(win, text = 'Turn LED on', font = myFont, command = ledtoggler3,bg = 'SeaGreen',height=1, width =24)
ledButton3.grid(row=0,column=3)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close,bg = 'red',height=1, width =6)
exitButton.grid(row=1,column=2)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop()#loop forever