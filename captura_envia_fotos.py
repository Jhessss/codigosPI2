"""
sudo apt-get update
sudo apt-get install python3-opencv
pip install requests
"""

import cv2
import time
import requests

# URL do servidor para onde as fotos serão enviadas
url = 'http://example.com/upload'  # Substituir pelo URL do servidor

# Inicializar a webcam
camera = cv2.VideoCapture(0)

# Verificar se a webcam foi inicializada corretamente
if not camera.isOpened():
    print("Erro ao acessar a webcam")
    exit()

# Aguardar 3 segundos para a câmera estabilizar
time.sleep(3)

# Função para capturar e salvar uma foto
def capture_photo(filename):
    ret, frame = camera.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Foto salva como {filename}")
    else:
        print("Erro ao capturar a foto")

# Função para enviar uma foto
def send_photo(filename):
    with open(filename, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print(f"Foto {filename} enviada com sucesso")
        else:
            print(f"Falha ao enviar a foto {filename}")

# Capturar e enviar 3 fotos
for i in range(3):
    photo_filename = f'foto_{i+1}.jpg'
    capture_photo(photo_filename)
    time.sleep(2)  # Esperar 2 segundos entre cada foto
    send_photo(photo_filename)

# Liberar a câmera
camera.release()
cv2.destroyAllWindows()
