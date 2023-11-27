import machine
import neopixel
import time
from machine import Pin

# DERECHA
NUM_LEDS1 = 18
boton1 = Pin(25, mode=Pin.IN, pull=Pin.PULL_UP)
led1 = Pin(15, mode=Pin.OUT)
np1 = neopixel.NeoPixel(led1, NUM_LEDS1)

# CENTRO
NUM_LEDS2 = 24
boton2 = Pin(26, mode=Pin.IN, pull=Pin.PULL_UP)
led2 = Pin(2, mode=Pin.OUT)
np2 = neopixel.NeoPixel(led2, NUM_LEDS2)

# IZQUIERDA
NUM_LEDS3 = 14
boton3 = Pin(27, mode=Pin.IN, pull=Pin.PULL_UP)
led3 = Pin(4, mode=Pin.OUT)
np3 = neopixel.NeoPixel(led3, NUM_LEDS3)


while True:
    estado_boton1 = boton1.value()
    estado_boton2 = boton2.value()
    estado_boton3 = boton3.value()
    
    if estado_boton1 == 0:
        time.sleep(1)
        for i in range(15):
            for i in range(NUM_LEDS1):
                np1[i] = (255, 225, 0)
                np1.write()
                time.sleep(0.1)
            np1.fill((0, 0, 0))
        np1.fill((0, 0, 0))
        np1.write()

    
    if estado_boton2 == 0:
        time.sleep(1)
        for i in range(15):
            for i in range(NUM_LEDS2):
                np2[i] = (255, 0, 0)
                np2.write()
                time.sleep(0.1)
            np2.fill((0, 0, 0))
        np2.fill((0, 0, 0))
        np2.write()
        
        
    if estado_boton3 == 0:
        time.sleep(1)
        for i in range(15):
            for i in range(NUM_LEDS3):
                np3[i] = (255, 225, 0)
                np3.write()
                time.sleep(0.1)
            np3.fill((0, 0, 0))
        np3.fill((0, 0, 0))
        np3.write()
        
    
            
            
                    
                    
                        