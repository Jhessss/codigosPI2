import RPi.GPIO as GPIO
import time
import cv2
import requests
import os
import glob
import schedule
import serial

###########Codigo para acionar os leds

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
    
    # Manter os LEDs ligados por 20 segundos
    time.sleep(20)

finally:
    # Desligar todos os LEDs e limpar a configuração GPIO
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()


###########Codigo para acionar a câmera e tirar 3 fotos

# URL do servidor para onde as fotos serão enviadas
#url = 'http://example.com/upload'  # Substituir pelo URL do servidor

# Inicializar a webcam
camera = cv2.VideoCapture(0)

# Verificar se a webcam foi inicializada corretamente
if not camera.isOpened():
    print("Erro ao acessar a webcam")
    exit()

# Aguardar 3 segundos para a câmera estabilizar
time.sleep(3)

# Nome da pasta onde as fotos serão armazenadas
folder_name = 'fotos'

# Criar a pasta se ela não existir
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Função para capturar e salvar uma foto
def capture_photo(filename):
    ret, frame = camera.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Foto salva como {filename}")
    else:
        print("Erro ao capturar a foto")

# Função para enviar uma foto
'''def send_photo(filename):
    with open(filename, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print(f"Foto {filename} enviada com sucesso")
        else:
            print(f"Falha ao enviar a foto {filename}")'''

# Capturar e enviar 3 fotos
for i in range(3):
    photo_filename = os.path.join(folder_name, f'foto_{i+1}.jpg')
    capture_photo(photo_filename)
    time.sleep(2)  # Esperar 2 segundos entre cada foto
   # send_photo(photo_filename)

# Liberar a câmera
camera.release()
cv2.destroyAllWindows()

########Codigo para leitura do sensor de temperatura.

# Inicializa as variáveis de caminho do sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_temp():
    lines = read_temp_raw()
    # Espera até que a leitura esteja completa ('YES' na segunda linha)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

# Loop principal para leitura da temperatura
while True:
    temp_c, temp_f = read_temp()
    print(f'Temperature: {temp_c:.2f} °C / {temp_f:.2f} °F')
    time.sleep(1)  # Aguarda 1 segundo entre as leituras


###########Codigo para acionar a bomba

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






