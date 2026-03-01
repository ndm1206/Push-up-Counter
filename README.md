# Push-up-Counter

This is a simple Python application that uses OpenCV and cvzone to count the number of push-ups a user performs in front of a camera. It leverages pose detection to analyze arm angles and determine when a full push-up has been completed.

## Features

- Real-time push-up counting using webcam input
- Visual feedback with percentage bars for left and right arm angles
- Displays frames per second (FPS)
- Color-coded progress bars and counts

## Requirements

- Python 3.8 or higher
- OpenCV (`opencv-python`)
- cvzone
- numpy

## Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate     # Windows

# Install dependencies
pip install opencv-python cvzone numpy
```

## Usage

```bash
python pushup.py
```

- The script will open the webcam and display a window with live feedback.
- Press `q` to quit the application.

## Notes

- Ensure your camera is functioning and accessible by OpenCV.
- The counters are based on detecting specific joint angles, so lighting and camera angle can affect accuracy.

## License

This project is provided under the MIT License. Feel free to modify and use it as needed.
