"""Executando o código
python3 led_control.py

"""

import RPi.GPIO as GPIO
import time

# Definir os pinos GPIO
led_pins = 17
# Configurar o modo da numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Configurar os pinos GPIO como saída
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    # Acionar todos os LEDs
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)
    
    # Manter os LEDs ligados por 10 segundos
    time.sleep(15)

finally:
    # Desligar todos os LEDs e limpar a configuração GPIO
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
