# Object Tracking App

## Overview

This project is an interactive web application for object tracking in videos using computer vision techniques. It leverages OpenCV's background subtraction method to detect and track moving objects in uploaded video files.
The application allow users to track employees
The application is built with Streamlit, providing an easy-to-use interface for users to upload videos and visualize object tracking results in real-time.

## Features

- **Video Upload**: Support for common video formats (MP4, AVI, MOV)
- **Real-time Processing**: Process videos frame by frame with adjustable speed
- **Customization**: Choose tracking color and processing speed
- **Background Subtraction**: Uses OpenCV's MOG2 background subtractor for object detection
- **Visualization**: Displays processed frames with bounding boxes around detected objects

## Project Structure

- `app.py`: Main Streamlit application
- `Oject_tracking.ipynb`: Jupyter notebook with object tracking demonstrations and examples
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd OT_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser to the provided URL (usually http://localhost:8501)

3. Upload a video file using the file uploader

4. Adjust the color picker and speed slider as needed

5. Watch the object tracking process in real-time

## Technologies Used

- **Streamlit**: Web application framework
- **OpenCV**: Computer vision library for object tracking
- **NumPy**: Numerical computing
- **Pillow**: Image processing
- **Matplotlib**: Plotting and visualization

## Notebook

The `Oject_tracking.ipynb` notebook contains detailed examples and demonstrations of object tracking algorithms, including background subtraction techniques and visualization methods. 

A real-time 