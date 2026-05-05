import streamlit as st
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tempfile
import time


# Set page configuration
st.set_page_config(
    page_title="Object Tracking App",
    page_icon=":guardsman:",
    layout="wide",
)


with st.sidebar:
    st.header("🎯 Object Tracking App")
    st.markdown(
        """
        This app allows you to upload a video and see object tracking in action using OpenCV's Background Subtraction method.
        """)
    st.markdown("---")
    st.header("🎨 Customization")
    color = st.color_picker("Pick a color", "#FF0000")
    st.markdown("---")
    st.header("speed")
    speed = st.slider("Processing Speed", 1, 60, 30)




st.title("🎯 Object Tracking App")
st.write("Upload a video to see object tracking in action using OpenCV's Background Subtraction method.")


def convert_color(image):
    """Convert the input image to RGB."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)




uplaoded_file = st.file_uploader("Choose an Video...", type=["mp4", "avi", "mov"])



if uplaoded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uplaoded_file.read())
    tfile.close()



    capture = cv2.VideoCapture(tfile.name)
    
    if not capture.isOpened():
        st.error("❌ Error opening video file.")
    
    else:
        st.success("✅ Video file opened successfully!, processing...")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Video")
            stframe1 = st.empty()
        with col2:
            st.subheader("Processed Video")
            stframe2 = st.empty()
            
            
        background_subtractor= cv2.createBackgroundSubtractorMOG2()
        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        progress_bar = st.progress(0)
        frame_idx = 0
        
        #covent color hex to BGR to openCV
        hex_color = color.lstrip("#")
        color = tuple(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
        
        
        while capture.isOpened():
            ret, frame = capture.read()
            if not ret:
                break
            fg_mask = background_subtractor.apply(frame)
            (contours, _) = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
            
            stframe1.image(convert_color(frame), channels="RGB")
            stframe2.image(fg_mask, channels="GRAY")
            frame_idx += 1
            progress_bar.progress(min(frame_idx / frame_count, 1.0))
            time.sleep(1 / speed)  # Simulate processing time
            
        capture.release()
        st.success("🥳 Video processing completed!")
        









