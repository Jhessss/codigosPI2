import schedule
import time
import RPi.GPIO as GPIO

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
control_pin = 17  # Pino GPIO conectado à base do transistor
GPIO.setup(control_pin, GPIO.OUT, initial=GPIO.LOW)

def ligar_bomba():
    GPIO.output(control_pin, GPIO.HIGH)  # Liga o transistor (e consequentemente o Arduino)
    time.sleep(30)                       # Mantém ligado por 30 segundos
    GPIO.output(control_pin, GPIO.LOW)   # Desliga o transistor

# Agenda a tarefa para ser executada todos os dias às 17h
schedule.every().day.at("17:00").do(ligar_bomba)

while True:
    schedule.run_pending()
    time.sleep(1)
