import cv2
import mediapipe as mp

# MediaPipe El Algılama Modülü
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

#Parmakların açık olup olmadığını kontrol eder.
def is_finger_open(hand_landmarks, finger_tip, finger_base):
    return hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_base].y

def recognize_gesture(hand_landmarks):
    """El hareketlerini tanımlar."""
    # Parmak uçlarının ve eklem noktalarının indexleri
    thumb_tip = 4
    index_tip = 8
    middle_tip = 12
    ring_tip = 16
    pinky_tip = 20
    
    # Parmağın tabanındaki referans noktaları
    index_base = 5
    middle_base = 9
    ring_base = 13
    pinky_base = 17
    
    # Parmak durumlarını kontrol et
    thumb_open = is_finger_open(hand_landmarks, thumb_tip, 2)  # Başparmak
    index_open = is_finger_open(hand_landmarks, index_tip, index_base)
    middle_open = is_finger_open(hand_landmarks, middle_tip, middle_base)
    ring_open = is_finger_open(hand_landmarks, ring_tip, ring_base)
    pinky_open = is_finger_open(hand_landmarks, pinky_tip, pinky_base)
    
    # Hareket Tanıma
    if thumb_open and index_open and middle_open and ring_open and pinky_open:
        return "Tum Parmaklar Acik"
    elif index_open and not middle_open and not ring_open and not pinky_open:
        return "Isaret Parmagi"
    elif not thumb_open and not index_open and not middle_open and not ring_open and not pinky_open:
        return "Yumruk"
    else:
        return "Bilinmeyen Isaret"

# Kamera Başlatma
cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    #Kamera Aynalama
    img = cv2.flip(img,1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Jest Tanıma
            gesture = recognize_gesture(hand_landmarks)
            print("Gesture:", gesture)
            
            # Görselleştirme
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(img, gesture, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    
    # Görüntüyü Göster
    cv2.imshow("Hand Gesture Recognition", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
