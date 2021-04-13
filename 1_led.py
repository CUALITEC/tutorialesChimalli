#importar módulos
from gpiozero import LED
from time import sleep
#crear objeto LED
led = LED(7) #7 porque está conectado en el gpio7
#creación del main
if __name__ = '__main__':
    while True: # Declaración del blucle
        led.on() # método para encender led
        sleep(1) # durante 1 segundo
        led.off() # método para pagar un led
        sleep(1) # durante 1 segundo