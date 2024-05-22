"""Executando o código
sudo apt-get update
sudo apt-get install python3-rpi.gpio

Conexões físicas.
GPIO 17 (Pino físico 11)
GPIO 27 (Pino físico 13)
GPIO 22 (Pino físico 15)
GPIO 23 (Pino físico 16)
GPIO 24 (Pino físico 18)


python3 led_control.py

"""

import RPi.GPIO as GPIO
import time

# Definir os pinos GPIO
led_pins = [17, 27, 22, 23, 24]

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
