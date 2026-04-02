# 🎮 Gesture Gaming System (AI-Based Game Control)

## 📌 Project Overview

The **Gesture Gaming System** is a computer vision–based interactive game where players control gameplay using **body movements instead of keyboard or mouse**.
It uses a webcam to detect human pose and converts gestures into game actions in real-time.

---

## 🚀 Features

* 🎥 Real-time **pose detection using camera**
* 🧠 Gesture recognition (Jump, Move Left, Move Right)
* 🎮 Endless runner game (Subway Surfers–style)
* 🧱 Dynamic obstacle generation
* 📈 Score tracking system
* ⚡ AI-based difficulty scaling
* 🏆 Leaderboard (Top scores saved locally)
* 🌆 Scrolling background
* 🔊 Sound effects (jump & game over)
* 🖼️ Character and obstacle graphics

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – camera processing
* **MediaPipe** – pose detection
* **Pygame** – game development
* **NumPy** – numerical operations

---

## 📁 Project Structure

```
gesture-gaming/
│── main.py
│── game.py
│── pose_controller.py
│── leaderboard.py
│── requirements.txt
│
├── assets/
│   ├── player.png
│   ├── obstacle.png
│   ├── background.png
│   ├── jump.wav
│   └── gameover.wav
│
└── utils/
    └── gestures.py
```

---

## ⚙️ Installation & Setup

### 1. Install Python (Recommended: 3.10 / 3.11)

### 2. Install dependencies

```
pip install -r requirements.txt
```

OR

```
python -m pip install opencv-python mediapipe pygame numpy
```

---

## ▶️ How to Run

```
python main.py
```

---

## 🎮 Controls (Gesture-Based)

| Gesture             | Action     |
| ------------------- | ---------- |
| 🙌 Raise both hands | Jump       |
| 👈 Move left hand   | Move left  |
| 👉 Move right hand  | Move right |

---

## 🧠 How It Works

1. Webcam captures live video
2. Pose detection identifies body landmarks
3. Gestures are recognized based on hand positions
4. Game updates player movement accordingly

---

## 🏆 Leaderboard

* Stores top scores in a local file (`leaderboard.json`)
* Displays top 5 scores during gameplay

---

## 💡 Future Enhancements

* 🌐 Web-based version using AI + JavaScript
* 📱 Mobile app integration
* 🧍 Full-body gesture gaming
* 🎯 Multiplayer support
* 🧠 Advanced AI gesture recognition

---

## ⚠️ Requirements

* Webcam required 🎥
* Good lighting for accurate detection
* Compatible Python version (3.10/3.11 recommended)

---

## 👨‍💻 Author

Developed as a **Computer Vision + Game Development Project**
Ideal for:

* Final Year Projects 🎓
* Hackathons 🏆
* AI/ML Portfolio 💼

---

## 🔥 Summary

This project demonstrates how **Computer Vision + AI can replace traditional input devices**, creating an immersive and interactive gaming experience.

---
