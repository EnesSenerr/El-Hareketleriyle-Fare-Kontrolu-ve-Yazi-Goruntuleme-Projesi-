import cv2
import mediapipe as mp
import pandas as pd
import time

# MediaPipe el kütüphanesi
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

columns = [f"x{i}_1" for i in range(21)] + [f"y{i}_1" for i in range(21)] + [f"z{i}_1" for i in range(21)] + ['Label']
data = []

cap = cv2.VideoCapture(0)

current_label = 'Enes'

# Veri toplama durumunu kontrol etmek için bir bayrak (flag) oluştur
data_collection = False

print("Veri toplama başlatmak için 's' tuşuna basın.")
print("Veri toplama durdurmak için 's' tuşuna tekrar basın.")

while cap.isOpened():
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Koordinatları al
            row = []
            for landmark in landmarks.landmark:
                row.extend([landmark.x, landmark.y, landmark.z])
            
            # Veri toplama aktifse, koordinatları ve etiketi CSV'ye ekle
            if data_collection:
                row.append(current_label)  # Etiketi ekle
                data.append(row)
            
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        data_collection = not data_collection  
        if data_collection:
            print("Veri toplama başladı...")
        else:
            print("Veri toplama durduruldu...")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

df = pd.DataFrame(data, columns=columns)
df.to_csv('Enes.csv', index=False)

print("Veri toplama tamamlandı.")
