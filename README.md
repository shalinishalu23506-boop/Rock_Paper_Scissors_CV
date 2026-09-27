# 🎮 Rock Paper Scissors using Computer Vision

A real-time **Rock Paper Scissors game** developed using **Python, OpenCV, and MediaPipe**. The project uses a webcam to detect the user's hand gestures and recognize Rock, Paper, and Scissors. The user can play against the computer with a countdown and score tracking.

## 📌 Project Overview

This project demonstrates how **Computer Vision and Hand Gesture Recognition** can be used to create an interactive game.

The webcam captures the user's hand movements, while MediaPipe detects the hand landmarks. Based on the detected finger positions, the system identifies the user's gesture as Rock, Paper, or Scissors.

The computer then generates its own move and the program determines the result of the round.

## 🎯 Objectives

- To understand the basics of Computer Vision.
- To detect and track hand landmarks using MediaPipe.
- To recognize hand gestures in real time.
- To develop an interactive game using Python.
- To gain practical experience with OpenCV and MediaPipe.

## ✨ Features

- 📷 Real-time webcam input
- ✋ Hand landmark detection
- ✊ Rock gesture recognition
- ✋ Paper gesture recognition
- ✌️ Scissors gesture recognition
- 🤖 Computer-generated moves
- ⏱️ Countdown before each round
- 🏆 Automatic result detection
- 📊 Real-time score tracking

## 🛠️ Technologies Used

- **Python**
- **OpenCV**
- **MediaPipe**
- **NumPy**

## 🔄 Working Process

The project follows this basic workflow:

**Webcam → OpenCV → MediaPipe → Hand Landmark Detection → Gesture Recognition → Game Logic → Computer Move → Result**

### How it works

1. The webcam captures the user's hand.
2. OpenCV processes the camera frames.
3. MediaPipe detects the hand landmarks.
4. The program analyzes the finger positions.
5. The gesture is identified as Rock, Paper, or Scissors.
6. The computer randomly selects its move.
7. The program compares both moves.
8. The winner is displayed on the screen.
9. The scores are updated after each round.

## 💻 Installation

Make sure Python is installed on your computer.

Install the required Python libraries using:

```bash
pip install opencv-python mediapipe numpy
