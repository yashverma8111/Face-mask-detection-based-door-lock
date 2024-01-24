# Face Mask Detection and Door Lock System

This project utilizes computer vision and hardware control to create a system that detects face masks and automatically locks a door if a mask is not worn correctly.

## Key Features:

Real-time face mask detection using MediaPipe Face Detection: Accurately identifies whether a person is wearing a mask or not.
Hand detection for gesture control: Allows users to interact with the system without touching a physical interface.
Hardware integration for door control: Connects to a door mechanism to lock or unlock it based on mask detection results.
Visual feedback and alerts: Provides clear visual cues on screen to indicate mask status and door state.
## Prerequisites:

Python 3.7 or later
OpenCV
MediaPipe
Necessary libraries for hardware control (e.g., controller.py for door automation and LED)
## Installation:

Clone this repository:
Bash
git clone https://github.com/<your-username>/face-mask-door-lock.git
Use code with caution. Learn more
Install the required libraries:
Bash
pip install -r requirements.txt
Use code with caution. Learn more
## Usage:

Connect the necessary hardware components according to your setup.
Run the main Python script:
Bash
python main.py
Use code with caution. Learn more
The system will start detecting faces and masks in real-time.
The door will automatically lock if a person is not wearing a mask correctly.
## Additional Information:

Hardware configuration: Provides details on the specific hardware components used for door control and LED signaling.
Troubleshooting: Offers guidance on common issues and potential solutions.
Customization: Explains how to adjust parameters for sensitivity, hardware interactions, and other settings.
## Contributions:

We welcome contributions to enhance this project! Please feel free to submit pull requests or raise issues.

## License:

This project is licensed under the MIT License.
