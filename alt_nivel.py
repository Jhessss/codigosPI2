import RPi.GPIO as GPIO
import time

# Configurações do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Lê o estado do sensor
        sensor_state = GPIO.input(23)
        
        if sensor_state == GPIO.HIGH:
            print("nível de água alto")
        else:
            print("nível de água baixo")
        
        # Aguarda 1 segundo antes de ler novamente
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")

finally:
    GPIO.cleanup()
