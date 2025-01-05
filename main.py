import cv2
import mediapipe as mp
from gesture_recognition2 import recognize_gesture
from prediction_mode import run_prediction_mode
import ctypes  # Kameranın ön planda kalmasını sağlamak için
import os
import webbrowser
import pyautogui  # Ekran çözünürlüğünü almak için
import time

# MediaPipe modülleri
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
# Ekran boyutlarını al
screen_width, screen_height = pyautogui.size()
# Tıklama işlevi için bekleme süresi kontrol değişkeni
last_click_time = 0
click_delay = 0.3
cap = cv2.VideoCapture(0)

def keep_window_on_top(window_name):
    hwnd = ctypes.windll.user32.FindWindowW(None, window_name)
    if hwnd:
        ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001)
# 

def scale_coordinates(x, y, img_width, img_height):
    scaled_x = int(x / img_width * screen_width)
    scaled_y = int(y / img_height * screen_height)

    if scaled_y > screen_height - 10:
        scaled_y = screen_height - 10
    
    return scaled_x, scaled_y



def process_left_hand(hand_landmarks, gesture, img_width, img_height):
    if gesture == "Pointing":
        index_finger_tip = hand_landmarks.landmark[8]  # İşaret parmağı ucu 8 numara
        x, y = index_finger_tip.x, index_finger_tip.y
        screen_x, screen_y = scale_coordinates(
            x * img_width, y * img_height, img_width, img_height)
        ctypes.windll.user32.SetCursorPos(
            screen_x, screen_y)  # İmleci ekranda hareket ettir
    elif gesture == "Open Hand":
            print("Tahmin moduna geçiliyor...")
            cap.release()
            cv2.destroyAllWindows()
            run_prediction_mode()        

def process_right_hand(gesture):
    global last_click_time
    current_time = time.time()

    # Tıklama işlemleri arasında bekleme süresi kontrolü
    if current_time - last_click_time < click_delay:
        return

    if gesture == "Thumb and Index Touched":
        print("Sağ el sol tıklama yapıyor.")
        ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Sol tık bas
        ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Sol tık bırak
        last_click_time = current_time  # Son tıklama zamanını güncelle
        
    elif gesture == "Thumb and Middle Touched":
        print("Baş parmak ve işaret parmağı birbirine değdi, sağ tıklama yapılıyor.")
        ctypes.windll.user32.mouse_event(8, 0, 0, 0, 0)  # Sağ tık 
        ctypes.windll.user32.mouse_event(16, 0, 0, 0, 0)  # Sağ tık bırak
        last_click_time = current_time   
 
def main_loop():
    """Kamera döngüsü ve hareket algılama."""
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=2)  # Çift el

    while True:
        success, img = cap.read()
        if not success:
            print("Kamera açılamadı!")
            break

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        img_height, img_width, _ = img.shape

        # Sol ve sağ el hareketlerini tanımlama
        left_hand_landmarks = None
        right_hand_landmarks = None
        left_hand_gesture = None
        right_hand_gesture = None

        if results.multi_hand_landmarks and results.multi_handedness:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                hand_label = results.multi_handedness[idx].classification[0].label
                gesture = recognize_gesture(hand_landmarks)

                if hand_label == "Left":
                    left_hand_landmarks = hand_landmarks
                    left_hand_gesture = gesture
                    mp_draw.draw_landmarks(
                        img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                elif hand_label == "Right":
                    right_hand_landmarks = hand_landmarks
                    right_hand_gesture = gesture
                    mp_draw.draw_landmarks(
                        img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Sol el (fare kontrolü)
            if left_hand_landmarks and left_hand_gesture:
                process_left_hand(left_hand_landmarks,
                                  left_hand_gesture, img_width, img_height)

            # Sağ el (tıklama işlemleri)
            if right_hand_gesture:
                process_right_hand(right_hand_gesture)

        cv2.imshow("Gesture Control", img)
        keep_window_on_top("Gesture Control")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_loop()
