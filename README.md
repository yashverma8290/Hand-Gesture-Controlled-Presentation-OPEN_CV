# Hand-Gesture-Controlled-Presentation
This project allows you to control a presentation using hand gestures captured by a webcam. The presentation slides are images stored in a folder, and the user can navigate through them by performing specific gestures such as swiping left or right, pointing, drawing, and erasing.

# Features
   >Gesture-based Control:
       >Swipe Left/Right: Navigate through presentation slides by swiping left or right.
       >Pointer Gesture: Show a pointer at the location of the index finger.
       >Drawing Gesture: Draw annotations on the presentation slide by moving the finger.
       >Erase Gesture: Erase previously drawn annotations.
  >Real-Time Hand Detection: Uses OpenCV and cvzone HandTrackingModule to detect and track the user's hand.
  >Webcam Integration: Displays the live webcam feed on the presentation slides for a dynamic, interactive experience.

# Prerequisites
Make sure you have the following Python libraries installed:
  >OpenCV: For computer vision tasks.
  >NumPy: For numerical operations.
  >cvzone: For hand tracking functionality.

You can install the dependencies using pip: pip install opencv-python numpy cvzone

# Setup Instructions
>Clone the Repository: git clone https://github.com/yashverma8290/Hand-Gesture-Controlled-Presentation-OPEN_CV.git
>Prepare Your Presentation:
    >Place your presentation slides in a folder named pictures. Make sure to add .png or .jpg images inside the folder.
    >The images will be displayed in order, and you can navigate between them using gestures.
>Run the Program:
    >Run the Python script:python hand_gesture_presentation.py
    >The live webcam feed will be displayed with the slides on the screen.

# Gesture Control Guide
>Left Swipe Gesture: Raise your left hand with the thumb pointing up to go to the previous slide.
>Right Swipe Gesture: Raise your right hand with the thumb pointing up to go to the next slide.
>Pointer Gesture: Raise your index finger (extended) to show a pointer on the screen.
>Draw Gesture: Raise your index and middle fingers (in a "peace" gesture) to draw on the slide.
>Erase Gesture: Raise your index, middle, and ring fingers to erase the drawing.

# Usage
>Navigation: Use left and right swipe gestures to move between presentation slides.
>Drawing: Use the pointer and draw gestures to mark areas on the slide.
>Erasing: Use the erase gesture to remove annotations.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to update any sections or add more specific instructions based on your preferences. Let me know if you need further adjustments!


