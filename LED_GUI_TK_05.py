from tkinter import *
import RPi.GPIO as GPIO
import time
import requests
import json

#RPI setup code    
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO_PINS={1:'b1',
   2:'b2',
   3:'b3',
   4:'b4',
   5:'b5',
   6:'b6',
   7:'b7',
   8:'b8',
   9:'b9',
   10:'b10',
   11:'b11',
   12:'b12',
   13:'b13',
   14:'b14',
   15:'b15',
   16:'b16',
   17:'b17',
   18:'b18',
   19:'b19',
   20:'b20',
   21:'b21',
   22:'b22',
   23:'b23',
   24:'b24',
   25:'b25',
   26:'b26',
   27:'b27',
   28:'b28',
   29:'b29',
   30:'b30',
   31:'b31',
   32:'b32',
   33:'b33',
   34:'b34',
   35:'b35',
   36:'b36',
   37:'b37',
   38:'b38',
   39:'b39',
   40:'b40',
   }

GN_GPIO = (0,8,10,12,16,18,22,24,26,32,36,38,40,37,35,33,31,29,23,21,19,15,13,11,7,5,3)

def update_button_status(n,status):
    global GN_GPIO, GPIO_PINS
    n=int(n)
    status=bool(status)
    
    if(status):
        GPIO.output(GN_GPIO[n],GPIO.HIGH)
        tmp=GN_GPIO[n]
        tmp2=GPIO_PINS[tmp]
        eval(tmp2)['bg']='green'
    else:
        GPIO.output(GN_GPIO[n],GPIO.LOW)
        tmp=GN_GPIO[n]
        tmp2=GPIO_PINS[tmp]
        eval(tmp2)['bg']='yellow'
    
    win.update()

win=Tk()
win.geometry("300x600")

b1=Button(win,text='Pin 1 (3.3V)',bg='red',fg='white')
b1.grid(row=0,column=0)

b2=Button(win,text='Pin 2 (5V)',bg='red',fg='white')
b2.grid(row=0,column=1)

b3=Button(win,text='Pin 3 (GPIO2)',bg='yellow')
b3.grid(row=1,column=0)

b4=Button(win,text='Pin 4 (5V)',bg='red',fg='white')
b4.grid(row=1,column=1)

b5=Button(win,text='Pin 5 (GPIO3)',bg='yellow')
b5.grid(row=2,column=0)

b6=Button(win,text='Pin 6 (GND)',bg='black',fg='white')
b6.grid(row=2,column=1)

b7=Button(win,text='Pin 7 (GPIO4)',bg='yellow')
b7.grid(row=3,column=0)

b8=Button(win,text='Pin 8 (GPIO14)',bg='yellow')
b8.grid(row=3,column=1)

b9=Button(win,text='Pin 9 (GND)',bg='black',fg='white')
b9.grid(row=4,column=0)

b10=Button(win,text='Pin 10 (GPIO15)',bg='yellow')
b10.grid(row=4,column=1)


b11=Button(win,text='Pin 11 (GPIO17)',bg='yellow')
b11.grid(row=5,column=0)

b12=Button(win,text='Pin 12 (GPIO18)',bg='yellow')
b12.grid(row=5,column=1)

b13=Button(win,text='Pin 13 GPIO(27)',bg='yellow')
b13.grid(row=6,column=0)

b14=Button(win,text='Pin 14 (GND)',bg='black',fg='white')
b14.grid(row=6,column=1)

b15=Button(win,text='Pin 15 (GPIO22)',bg='yellow')
b15.grid(row=7,column=0)

b16=Button(win,text='Pin 16 (GPIO23)',bg='yellow')
b16.grid(row=7,column=1)

b17=Button(win,text='Pin 17 (3.3V)',bg='red',fg='white')
b17.grid(row=8,column=0)

b18=Button(win,text='Pin 18 (GPIO24)',bg='yellow')
b18.grid(row=8,column=1)

b19=Button(win,text='Pin 19 (GPIO10)',bg='yellow')
b19.grid(row=9,column=0)

b20=Button(win,text='Pin 20 (GND)',bg='black',fg='white')
b20.grid(row=9,column=1)


b21=Button(win,text='Pin 21 (GPIO9)',bg='yellow')
b21.grid(row=10,column=0)

b22=Button(win,text='Pin 22 (GPIO25)',bg='yellow')
b22.grid(row=10,column=1)

b23=Button(win,text='Pin 23 (GPIO11)',bg='yellow')
b23.grid(row=11,column=0)

b24=Button(win,text='Pin 24 (GPIO8)',bg='yellow')
b24.grid(row=11,column=1)

b25=Button(win,text='Pin 25 (GND)',bg='black',fg='white')
b25.grid(row=12,column=0)

b26=Button(win,text='Pin 26 (GPIO7)',bg='yellow')
b26.grid(row=12,column=1)

b27=Button(win,text='Pin 27 (DNC)')
b27.grid(row=13,column=0)

b28=Button(win,text='Pin 28 (DNC)')
b28.grid(row=13,column=1)

b29=Button(win,text='Pin 29 (GPIO5)',bg='yellow')
b29.grid(row=14,column=0)

b30=Button(win,text='Pin 30 (GND)',bg='black',fg='white')
b30.grid(row=14,column=1)


b31=Button(win,text='Pin 31 (GPIO6)',bg='yellow')
b31.grid(row=15,column=0)

b32=Button(win,text='Pin 32 (GPIO12)',bg='yellow')
b32.grid(row=15,column=1)

b33=Button(win,text='Pin 33 (GPIO13)',bg='yellow')
b33.grid(row=16,column=0)

b34=Button(win,text='Pin 34 (GND)',bg='black',fg='white')
b34.grid(row=16,column=1)

b35=Button(win,text='Pin 35 (GPIO19)',bg='yellow')
b35.grid(row=17,column=0)

b36=Button(win,text='Pin 36 (GPIO16)',bg='yellow')
b36.grid(row=17,column=1)

b37=Button(win,text='Pin 37 (GPIO26)',bg='yellow')
b37.grid(row=18,column=0)

b38=Button(win,text='Pin 38 (GPIO20)',bg='yellow')
b38.grid(row=18,column=1)

b39=Button(win,text='Pin 39 (GND)',bg='black',fg='white')
b39.grid(row=19,column=0)

b40=Button(win,text='Pin 40 (GPIO21)',bg='yellow')
b40.grid(row=19,column=1)

win.update()

for i in range(1,27): # from 1 to 26
    GPIO.setup(GN_GPIO[i],GPIO.OUT)

while(True):
    res = requests.get('https://scifisolutions.in/rpi_gpio_status')
    a=res.json()
    if(a['success']==True):
        b=a['message']
            
        for x,y in b.items():
            if(y==1):
                flag=True
            else:
                flag=False
            update_button_status(x,flag)
        time.sleep(0.5)
