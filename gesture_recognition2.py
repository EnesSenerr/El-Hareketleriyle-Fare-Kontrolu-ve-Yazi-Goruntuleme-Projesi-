def is_finger_open(hand_landmarks, finger_tip, finger_base):
    return hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_base].y

def calculate_distance(p1, p2):
    """İki nokta arasındaki mesafeyi hesaplar"""
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

def recognize_gesture(hand_landmarks):
    thumb_tip = 4
    index_tip = 8
    middle_tip = 12
    ring_tip = 16
    pinky_tip = 20
    
    index_base = 5
    middle_base = 9
    ring_base = 13
    pinky_base = 17
    
    thumb_open = is_finger_open(hand_landmarks, thumb_tip, 2)
    index_open = is_finger_open(hand_landmarks, index_tip, index_base)
    middle_open = is_finger_open(hand_landmarks, middle_tip, middle_base)
    ring_open = is_finger_open(hand_landmarks, ring_tip, ring_base)
    pinky_open = is_finger_open(hand_landmarks, pinky_tip, pinky_base)
    
    # Baş parmak ve işaret parmağının uç noktalarındaki mesafeyi kontrol et
    thumb_tip_landmark = hand_landmarks.landmark[thumb_tip]
    index_tip_landmark = hand_landmarks.landmark[index_tip]
    middle_tip_landmark = hand_landmarks.landmark[middle_tip]
    
    distance_thumb_index = calculate_distance(thumb_tip_landmark, index_tip_landmark)
    distance_middle_index = calculate_distance(thumb_tip_landmark, middle_tip_landmark)
    
    if distance_thumb_index < 0.05:  # Mesafe eşik değeri (0.05, deneyerek uygun değeri ayarlayın)
        return "Thumb and Index Touched"
    if distance_middle_index < 0.05:  # Mesafe eşik değeri (0.05, deneyerek uygun değeri ayarlayın)
        return "Thumb and Middle Touched"
    
    # if index_open or not index_open and not middle_open and not ring_open and not pinky_open:
    #     return "Pointing"
    # elif thumb_open and index_open and middle_open and ring_open and pinky_open:
    #     return "Open Hand"
    # elif not thumb_open and not index_open and not middle_open and not ring_open and not pinky_open:
    #     return "Fist"
    # else:
    #     return "Unknown Gesture"
    if thumb_open and index_open and middle_open and ring_open and pinky_open:
        return "Open Hand"
    elif distance_thumb_index < 0.05:  # Mesafe eşik değeri 0.05 
        return "Thumb and Index Touched"  # Baş ve işaret parmağı birleşik
    elif index_open or not index_open and not middle_open and not ring_open and not pinky_open:
        return "Pointing"
    else:
        return "Unknown Gesture"
    
    
