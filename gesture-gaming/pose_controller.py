import cv2
import mediapipe as mp
from utils.gestures import detect_gesture

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

class PoseController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_gesture(self):
        ret, frame = self.cap.read()
        if not ret:
            return "IDLE", frame

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(rgb)

        gesture = "IDLE"

        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark
            gesture = detect_gesture(landmarks)
            mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow("Camera", frame)
        cv2.waitKey(1)

        return gesture, frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()