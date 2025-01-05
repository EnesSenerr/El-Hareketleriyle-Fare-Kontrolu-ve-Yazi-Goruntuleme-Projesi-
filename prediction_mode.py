import cv2
import mediapipe as mp
import numpy as np
import joblib


def run_prediction_mode():
    from main import main_loop
    # Modeli yükle
    model = joblib.load('knn_model3.pkl')
    def process_left_hand(hand_landmarks, gesture, img_width, img_height):
        """Sol el hareketlerini işler ve fareyi kontrol eder."""

    # Mediapipe
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

               
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append([lm.x, lm.y, lm.z])

                features = np.array(landmarks).flatten().reshape(1, -1)

                # Model ile tahmin yap
                prediction = model.predict(features)

                cv2.putText(frame, f'Predicted: {prediction[0]}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Hand Detection', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    