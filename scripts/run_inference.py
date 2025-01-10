import cv2
from models.model_script import run_inference
from api.control_api import send_control_signal

def process_image_and_control_device(image_path):
    detections = run_inference(image_path, network, class_names, class_colors)
    for detection in detections:
        if detection[0] == "gesture" and detection[1] > 0.5:
            # If a gesture is detected with sufficient confidence
            send_control_signal(1, "turn_on")  
        elif detection[0] == "object" and detection[1] > 0.5:
            send_control_signal(2, "turn_off") 

process_image_and_control_device("test_image.jpg")
