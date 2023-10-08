import cv2

# URL de la fuente de video RTSP
rtsp_url = 'rtsp://admin:MeMfea16@192.168.3.224/onvif1'

# Abre la fuente de video RTSP
cap = cv2.VideoCapture(rtsp_url)

# Verifica si la fuente de video se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir la fuente de video RTSP.")
    exit()

# Lee los frames de la fuente de video RTSP y los muestra en una ventana
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video RTSP', frame)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos y cierra la ventana
cap.release()
cv2.destroyAllWindows()
