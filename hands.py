import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import keyboard

def see_hands():
    
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    RunningMode = mp.tasks.vision.RunningMode

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
        running_mode=RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,   # Increased for stability
        min_hand_presence_confidence=0.3,    # Increased for stability
        min_tracking_confidence=0.5,         # Fixed extreme low confidence jitter
    )

    with HandLandmarker.create_from_options(options) as landmarker:
        cap = cv2.VideoCapture(0)
        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Camera", 320, 240)
        cv2.setWindowProperty(
            "Camera",
            cv2.WND_PROP_TOPMOST,
            1
        )

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )
            timestamp_ms = int(time.time() * 1000)
            result = landmarker.detect_for_video(mp_image, timestamp_ms)
            if result:
                for hand in result.hand_landmarks:
                    for mark in hand:
                        x = int(mark.x * frame.shape[1])
                        y = int(mark.y * frame.shape[0])

                        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                keyboard.release("w")
                keyboard.release("a")
                keyboard.release("d")
                break

            yield result.hand_landmarks
        cap.release()
        cv2.destroyAllWindows() 

if __name__ == "__main__":
    see_hands()