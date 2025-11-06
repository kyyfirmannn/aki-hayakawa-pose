🖐️ Hand Gesture Control – KON Pose Video Trigger

This project uses OpenCV and MediaPipe to detect a specific hand gesture (KON pose) through a webcam and automatically play a video when the gesture is recognized.

🎯 Features

Real-Time Gesture Detection: Uses MediaPipe Hands to track hand landmarks directly from the webcam feed.

Video Trigger: When the KON pose (index and pinky fingers raised, others folded) is detected, the video "video/fox2.mp4" will automatically play.

Auto Close: When the gesture is no longer detected, the video stops and the window closes automatically.

Visual Overlay: Displays hand landmarks and connections in real-time on the camera window.

🧠 Technologies Used

Python 3

OpenCV

MediaPipe

NumPy

⚙️ How to Run

Install dependencies:

pip install opencv-python mediapipe numpy


Place your video file in:

video/fox2.mp4


Run the script:

python main.py


Show the KON pose to your webcam — the video will appear automatically.

📹 KON Pose Structure

Index and pinky fingers raised.

Middle and ring fingers folded.


🧩 Notes

Press q to quit the application.

The video window will automatically close when playback finishes or when the gesture disappears.
