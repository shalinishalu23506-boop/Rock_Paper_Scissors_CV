import cv2
import mediapipe as mp
import random
import time

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


# -----------------------------
# Download/use hand model
# -----------------------------
MODEL_PATH = "./hand_landmarker.task"

base_options = python.BaseOptions(
    model_asset_path=MODEL_PATH
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)
landmarker = vision.HandLandmarker.create_from_options(options)


# -----------------------------
# Game
# -----------------------------
choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

state = "countdown"
start_time = time.time()

player_choice = ""
computer_choice = ""
result = ""


def detect_gesture(landmarks):

    # Finger tips and joints
    index_open = landmarks[8].y < landmarks[6].y
    middle_open = landmarks[12].y < landmarks[10].y
    ring_open = landmarks[16].y < landmarks[14].y
    little_open = landmarks[20].y < landmarks[18].y

    fingers = [
        index_open,
        middle_open,
        ring_open,
        little_open
    ]

    if fingers == [False, False, False, False]:
        return "Rock"

    if fingers == [True, True, True, True]:
        return "Paper"

    if fingers == [True, True, False, False]:
        return "Scissors"

    return "Unknown"


def get_winner(player, computer):

    if player == computer:
        return "Draw"

    if (
        (player == "Rock" and computer == "Scissors")
        or
        (player == "Paper" and computer == "Rock")
        or
        (player == "Scissors" and computer == "Paper")
    ):
        return "You Win!"

    return "Computer Wins!"


# -----------------------------
# Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    frame_timestamp_ms = int(time.time() * 1000)
    detection_result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)

    current_move = "Show Hand"

    # Draw landmarks
    if detection_result.hand_landmarks:

        landmarks = detection_result.hand_landmarks[0]

        current_move = detect_gesture(landmarks)

        h, w, _ = frame.shape

        for landmark in landmarks:

            x = int(landmark.x * w)
            y = int(landmark.y * h)

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )


    # -----------------------------
    # Countdown
    # -----------------------------
    if state == "countdown":

        elapsed = time.time() - start_time

        if elapsed < 1:
            text = "3"

        elif elapsed < 2:
            text = "2"

        elif elapsed < 3:
            text = "1"

        else:

            text = "SHOOT!"

            player_choice = current_move
            computer_choice = random.choice(choices)

            if player_choice in choices:

                result = get_winner(
                    player_choice,
                    computer_choice
                )

                if result == "You Win!":
                    player_score += 1

                elif result == "Computer Wins!":
                    computer_score += 1

            state = "result"
            start_time = time.time()


        cv2.putText(
            frame,
            text,
            (500, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            2.5,
            (0, 255, 255),
            5
        )


    # -----------------------------
    # Result
    # -----------------------------
    elif state == "result":

        cv2.putText(
            frame,
            "You: " + player_choice,
            (30, 60),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Computer: " + computer_choice,
            (30, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            result,
            (350, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.3,
            (0, 255, 255),
            3
        )

        if time.time() - start_time > 2:

            state = "countdown"
            start_time = time.time()


    # Score
    cv2.putText(
        frame,
        f"Your Score: {player_score}",
        (30, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Computer Score: {computer_score}",
        (30, 490),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        "Rock Paper Scissors",
        (300, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Rock Paper Scissors",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()