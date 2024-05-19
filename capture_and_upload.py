""" Instalando as dependencias
sudo apt update
sudo apt install python3-opencv
pip3 install RPi.GPIO requests
"""

"""Executando o script:

python3 capture_and_upload.py
"""



import RPi.GPIO as GPIO
import time
import cv2
import requests

# Configurações dos pinos
LED_PIN = 17  # Escolha um pino GPIO, aqui usamos o GPIO 17 (pino físico 11)

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Função para acionar os LEDs
def acionar_leds():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3)

# Função para capturar fotos com a webcam
def capturar_fotos():
    cap = cv2.VideoCapture(0)  # 0 é o índice para a primeira webcam conectada
    fotos = []

    if not cap.isOpened():
        print("Erro ao acessar a webcam")
        return []

    for i in range(3):
        ret, frame = cap.read()
        if ret:
            foto_path = f"foto_{i + 1}.jpg"
            cv2.imwrite(foto_path, frame)
            fotos.append(foto_path)
            time.sleep(1)  # Espera de 1 segundo entre as fotos
        else:
            print(f"Falha ao capturar a foto {i + 1}")

    cap.release()
    return fotos

# Função para enviar fotos para um endereço na internet
def enviar_fotos(fotos, url):
    for foto in fotos:
        with open(foto, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)
            if response.status_code == 200:
                print(f"{foto} enviada com sucesso!")
            else:
                print(f"Falha ao enviar {foto}")

if __name__ == "__main__":
    try:
        # Aciona os LEDs e espera 3 segundos
        acionar_leds()
        
        # Captura as fotos enquanto os LEDs estão acesos
        fotos = capturar_fotos()
        
        if fotos:
            # Envia as fotos (substituir 'http://example.com/upload' pela URL desejada)
            enviar_fotos(fotos, 'http://example.com/upload')
    finally:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()
