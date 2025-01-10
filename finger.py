import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Buka kamera
cap = cv2.VideoCapture(0)

# Inisialisasi MediaPipe Hands
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip gambar untuk tampilan seperti cermin
        frame = cv2.flip(frame, 1)
        # Ubah gambar ke RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Deteksi tangan
        results = hands.process(rgb_frame)

        # Jika ada tangan yang terdeteksi
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Gambar landmark tangan
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Ambil posisi landmark
                landmarks = hand_landmarks.landmark

                # Deteksi apakah jempol atau telunjuk terangkat
                thumb_up = landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_IP].y
                index_up = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y

                # Tampilkan status deteksi di layar
                if thumb_up:
                    cv2.putText(frame, "Jempol Terangkat", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                if index_up:
                    cv2.putText(frame, "Telunjuk Terangkat", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Tampilkan hasil di layar
        cv2.imshow('Gesture Detection', frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Bersihkan sumber daya
cap.release()
cv2.destroyAllWindows()
