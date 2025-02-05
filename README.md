# virtual-calculator

 

Virtual Hand-Gesture Calculator 🤖🖐️
A touchless calculator that uses hand gestures to perform arithmetic operations! This project utilizes OpenCV, cvzone, and MediaPipe for hand tracking and gesture recognition.



🛠️ Features
✅ Perform basic arithmetic operations (+, -, *, /)
✅ Virtual button presses using hand gestures
✅ Smooth and realistic UI with visual feedback
✅ Works with a webcam (No additional hardware needed!)

🚀 Installation
1️⃣ Clone the Repository

2️⃣ Install Dependencies
Ensure you have Python 3.7+ installed. Then, install the required libraries:

pip install opencv-python numpy cvzone mediapipe

3️⃣ Run the Application

python calculator.py
📌 Usage
Start the program – Your webcam will activate.
Use your index finger to press buttons.
Ensure only one finger is extended when pressing.
Press '=' to evaluate the equation.
Press 'C' to clear the screen.
Press 'q' on your keyboard to exit.

🔧 How It Works
Uses OpenCV to process webcam input.
Detects hand landmarks using cvzone.HandTrackingModule.
Checks for button clicks using the index finger's position.
Displays the equation on a custom UI built with OpenCV.
