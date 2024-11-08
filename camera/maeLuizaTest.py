import cv2

# Iniciar a captura de vídeo
cam = cv2.VideoCapture(0)

# Carregar o classificador Haar para detecção de rosto
detec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Definir o nome da janela e permitir que seja redimensionada
window_name = 'Camera'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Definir a largura e altura da janela para cobrir uma parte da tela
screen_width = 1280  # Ajuste este valor conforme o desejado
screen_height = 720  # Ajuste este valor conforme o desejado
cv2.resizeWindow(window_name, screen_width, screen_height)

odd = True

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Não foi possível capturar a imagem da câmera.")
        break

    if odd:
        # Converter para escala de cinza para a detecção
        cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem
        faces = detec.detectMultiScale(cinza, 1.3, 3)

        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, larg, alt) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + larg, y + alt), (0, 255, 0), 3)

        # Mostrar o frame
        cv2.imshow(window_name, frame)
        
        # Pressione 'q' para sair do loop
        if cv2.waitKey(1) == ord('q'):
            break

    odd = not odd

# Liberar a captura e fechar as janelas
cam.release()
cv2.destroyAllWindows()

