import RPi.GPIO as GPIO
import time

# Configuração dos pinos
sensor_pin = 27

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def sensor_callback(channel):
    if GPIO.input(sensor_pin):
        print("Nível da água baixo")
    else:
        print("Nível da água suficiente para operação")

# Configurar interrupção no GPIO
GPIO.add_event_detect(sensor_pin, GPIO.BOTH, callback=sensor_callback)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o programa")
finally:
    GPIO.cleanup()
