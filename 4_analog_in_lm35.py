#Importamos los módulos
from gpiozero import MCP3008 #MCP es el ADC
from time import sleep
# Crear el objeto adc indicando en cual canal (de los 8 disponibles) está conectado el sensor LM35
adc = MCP3008(channel=0)
# Declarar la función que convierte el valor leído por el ADC en temperatura en °C
def convert_temp(gen):
    for value in gen:
        yield (value * 3.3) * 100


for temp in convert_temp(adc.values): # Blucle para convertir todos los valores que se reciban del ADC
    print('Temperatura: ', temp, '°C')
    sleep(1)