# Apple Object Detection with YOLOv8 🍎

This project is a computer vision application designed to detect apples in images using the YOLOv8 architecture. The dataset was collected, annotated via **Roboflow**, and the model was trained locally.

## 🚀 Features
- **Dataset:** Labeled apple images (red, green, and multiple varieties).
- **Model:** YOLOv8 Nano (trained for 20 epochs).
- **Performance:** High precision object detection for agricultural or retail contexts.
- **Tools:** Python, Ultralytics YOLO, Roboflow.

## 📂 Project Structure
- `main.py`: Script to train the YOLOv8 model locally.
- `test_et.py`: Inference script to test the model on new images.
- `data.yaml`: Dataset configuration file.
- `runs/`: Contains the training results and the best model weights (`best.pt`).

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/apple-object-detection-yolov8.git
