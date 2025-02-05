import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Initialize camera and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)  # Height
detector = HandDetector(detectionCon=0.7, maxHands=1)

# Calculator layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Variables
equation = ""
delay_counter = 0
pressed_button = None  # Stores the last pressed button


def draw_calculator(img, button_list):
    """Draw the calculator buttons with a realistic UI."""`
    # Draw calculator screen
    cv2.rectangle(img, (400, 50), (800, 130), (50, 50, 50), cv2.FILLED)  # Dark background
    cv2.putText(img, equation, (420, 110), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)  # Green text

    # Draw buttons
    for y, row in enumerate(button_list):
        for x, button in enumerate(row):
            x1, y1 = x * 100 + 400, y * 100 + 150
            x2, y2 = x1 + 90, y1 + 90

            # Button Color: Default gray, pressed yellow
            color = (80, 80, 80) if button != pressed_button else (0, 255, 255)

            # Draw rounded buttons with shadows
            cv2.rectangle(img, (x1, y1), (x2, y2), (40, 40, 40), -1, cv2.LINE_AA)
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 5, cv2.LINE_AA)

            # Draw button text
            cv2.putText(img, button, (x1 + 30, y1 + 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
    return img


def check_button_click(pos, button_list):
    """Check if the finger is clicking a button."""
    for y, row in enumerate(button_list):
        for x, button in enumerate(row):
            x1, y1 = x * 100 + 400, y * 100 + 150
            x2, y2 = x1 + 90, y1 + 90
            if x1 < pos[0] < x2 and y1 < pos[1] < y2:
                return button
    return None


while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip for mirror effect
    hands, img = detector.findHands(img, flipType=False)

    # Draw calculator buttons
    img = draw_calculator(img, buttons)

    if hands:
        # Get the position of the index finger
        lmList = hands[0]['lmList']
        index_finger = lmList[8][:2]  # (x, y) of index finger
        middle_finger = lmList[12][:2]  # (x, y) of middle finger

        # Calculate distance between index and middle fingers
        length, _, img = detector.findDistance(index_finger, middle_finger, img)

        # Ensure only one finger is pressing
        if length > 50:
            button = check_button_click(index_finger, buttons)

            if button and delay_counter == 0:
                pressed_button = button  # Store pressed button for visual feedback

                if button == "=":
                    try:
                        equation = str(eval(equation))  # Evaluate the equation
                    except:
                        equation = "Error"
                elif button == "C":
                    equation = ""  # Clear the equation
                else:
                    equation += button  # Append the button value to the equation

                delay_counter = 1  # Add delay to prevent multiple presses

    # Delay counter to reset pressed button
    if delay_counter != 0:
        delay_counter += 1
        if delay_counter > 10:  # Reset after 10 frames
            delay_counter = 0
            pressed_button = None  # Reset the pressed button

    # Show the image
    cv2.imshow("Virtual Calculator", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
