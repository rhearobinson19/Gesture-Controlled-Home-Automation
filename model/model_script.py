import cv2
import darknet

# Initialize the Darknet network with custom configuration
def load_model(cfg_file, weight_file, data_file):
    network, class_names, class_colors = darknet.load_network(cfg_file, data_file, weight_file)
    return network, class_names, class_colors
import cv2
import darknet

# Initialize the Darknet network with custom configuration
def load_model(cfg_file, weight_file, data_file):
    network, class_names, class_colors = darknet.load_network(cfg_file, data_file, weight_file)
    return network, class_names, class_colors

# Run inference on a given image
def run_inference(image_path, network, class_names, class_colors):
    image = cv2.imread(image_path)
    width = darknet.network_width(network)
    height = darknet.network_height(network)
    # Resize image for YOLO model
    resized_image = cv2.resize(image, (width, height))
    
    # Get detections
    detections = darknet.detect_image(network, class_names, resized_image)
    
    # Process detections (Optional: Draw bounding boxes)
    for label, confidence, bbox in detections:
        print(f"Detected: {label} with confidence {confidence}")
        # Code to process the bounding box
    return detections

# Load YOLO model
cfg_file = "data/yolov4-custom.cfg"
weight_file = "models/yolov4-custom.weights"
data_file = "data/classes.data"
network, class_names, class_colors = load_model(cfg_file, weight_file, data_file)

# Run inference
image_path = "test_image.jpg"
run_inference(image_path, network, class_names, class_colors)


def run_inference(image_path, network, class_names, class_colors):
    image = cv2.imread(image_path)
    width = darknet.network_width(network)
    height = darknet.network_height(network)
    # Resize image for YOLO model
    resized_image = cv2.resize(image, (width, height))
    
    # Get detections
    detections = darknet.detect_image(network, class_names, resized_image)
    
    # Process detections (Optional: Draw bounding boxes)
    for label, confidence, bbox in detections:
        print(f"Detected: {label} with confidence {confidence}")
        # Code to process the bounding box
    return detections

# Load YOLO model
cfg_file = "data/yolov4-custom.cfg"
weight_file = "models/yolov4-custom.weights"
data_file = "data/classes.data"
network, class_names, class_colors = load_model(cfg_file, weight_file, data_file)

# Run inference
image_path = "test_image.jpg"
run_inference(image_path, network, class_names, class_colors)
