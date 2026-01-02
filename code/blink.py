import time
import board
import digitalio

led1 = digitalio.DigitalInOut(board.GP16)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP15)
led2.direction = digitalio.Direction.OUTPUT


while True:
    led1.value = True   
    time.sleep(.5)    
    led2.value = True
    time.sleep(.5)
    led1.value = False 
    time.sleep(.5)    
    led2.value = False
    time.sleep(.5)