import cv2
import mediapipe as mp

#Mediapipe El Modülü
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#Kamera Erişimi
cap = cv2.VideoCapture(0)

#Video Döngüsü
while True:
    success, img = cap.read()
    #RGB Dönüşümü
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    #Tespit Edilen Noktaları Cizdirme
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#Görüntüyü Ekrana Verme
    cv2.imshow("Image", img)
    #"q" ile çıkış yapma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #Kamera ve Kaynak Temizleme
cap.release()
cv2.destroyAllWindows()
