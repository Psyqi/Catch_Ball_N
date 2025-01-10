import cv2
import mediapipe as mp
import constants

class HandTracking:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.hands.close()

    def detect_hand(self, frame):
        # Baca dan proses gambar untuk mendeteksi tangan
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        # Deteksi telunjuk
        finger_x = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                # Ambil koordinat telunjuk
                index_finger_tip = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
                finger_x = int(index_finger_tip.x * constants.SCREEN_WIDTH)
        
        return finger_x

    def update_paddle_position(self, finger_x, paddle_x):
    # Update posisi paddle berdasarkan posisi telunjuk
        paddle_x = finger_x - constants.PADDLE_WIDTH // 2
    # Batasi agar paddle tidak keluar dari layar
        paddle_x = max(0, min(paddle_x, constants.SCREEN_WIDTH - constants.PADDLE_WIDTH))
        return paddle_x


