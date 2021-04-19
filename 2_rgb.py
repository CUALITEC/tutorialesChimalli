#importar módulos
from gpiozero import RGBLED
from time import sleep
#crear objeto led asignando el GPIO que corresponde para cada color
led = RGBLED(red = 21 , green = 20 , blue = 19)

#declaración de función que ejecutará una sucesión de colores

def coloresBase():
    
    led.color = (1, 1, 1) # todos apagados [R,G,B], el RGB es de ánodo común
    sleep(1)# durante 1 segundo
    led.color = (0, 1, 1)# rojo maxima intensidad
    sleep(1)# durante 1 segundo
    led.color = (1, 0, 1)# verde  maxima intensidad
    sleep(1)# durante 1 segundo
    led.color = (1, 1, 0)# azul  maxima intensidad
    sleep(1)# durante 1 segundo
    led.color = (0.5, 0.5, 0.5)# todos a media intensidad [blanco]
    sleep(1)# durante 1 segundo
    led.color = (0, 0, 0)# todos máxima intensidad [blanco]
    sleep(1)# durante 1 segundo
    
if __name__ == '__main__':
    while True:
        coloresBase()