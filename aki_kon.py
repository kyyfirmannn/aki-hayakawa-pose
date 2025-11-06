import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

video_path = "video/fox2.mp4"
cap_video = None
video_playing = False

cap = cv2.VideoCapture(0)
print("Tekan 'q' untuk keluar")

def detect_kon_pose(landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_pip = [6, 10, 14, 18]
    up_fingers = []
    for tip, pip in zip(finger_tips, finger_pip):
        if landmarks[tip].y < landmarks[pip].y:
            up_fingers.append(1)
        else:
            up_fingers.append(0)
    return up_fingers == [1, 0, 0, 1]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    kon_detected = False

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(255,0,0), thickness=2)
            )

            if detect_kon_pose(hand_landmarks.landmark):
                kon_detected = True
                cv2.putText(frame, "KON Pose!", (30, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    if kon_detected:
        if not video_playing:
            cap_video = cv2.VideoCapture(video_path)
            video_playing = True

        if cap_video:
            ret_vid, vid_frame = cap_video.read()
            if not ret_vid:
                cap_video.release()
                cap_video = None
                video_playing = False
            else:
                vid_frame = cv2.resize(vid_frame, (640, 360))
                cv2.imshow("Fox Summon", vid_frame)
    else:
        if video_playing:
            video_playing = False
            if cap_video:
                cap_video.release()
                cap_video = None
            cv2.destroyWindow("Fox Summon")

    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if cap_video:
    cap_video.release()
cv2.destroyAllWindows()
