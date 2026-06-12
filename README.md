# 🌾 Segmentation of Rice Field Images Captured by UAV

![UAV Image Segmentation](https://github.com/user-attachments/assets/0157b05c-a856-4e3a-8fff-f623992cddac)

This project (developed for a Graduation Thesis) focuses on the automated segmentation of rice fields using high-resolution Unmanned Aerial Vehicle (UAV) imagery. It evaluates and compares various deep learning architectures for both Semantic and Instance Segmentation.

---

## 📊 Dataset Overview

* **Original Dataset:** 201 images at a resolution of `5280 × 3956` pixels.
* **Training Data (Resized):** 201 images scaled down to `1280 × 960` pixels to optimize computational load.
* **Testing Data:** 21 independent images.
* **Annotation Tool:** [AnyLabeling](https://github.com/vietanhdev/anylabeling) (Python 3.9 environment).
* **Training Environment:** Google Colab.

---

## 🛠️ Complete Machine Learning Pipeline

### 1. Data Preparation
* Collect raw high-resolution UAV imagery.
* Strategically split the dataset into Training, Validation, and Testing subsets.

### 2. Data Preprocessing
* **Object/Instance Level:** Annotate images and split them into respective sets.
* **Semantic Level:** Ensure consistent class labeling across all masks.
* **Standardization:** Resize all images and corresponding masks to a uniform shape (`1280 × 960`).
* **Normalization:** Scale pixel values to `[0, 1]` or `[-1, 1]` intervals.
* **Data Augmentation:** Apply random rotation, flipping, cropping, and brightness adjustments to enhance dataset variance and mitigate overfitting.

### 3. Model Architecture Selection
Different models were chosen based on specific segmentation goals:
* **U-Net:** Renowned for precise, boundary-level semantic segmentation.
* **Mask R-CNN:** The gold standard for instance-level segmentation and distinct object isolation.
* **DeepLab(v3):** Excellent for semantic segmentation requiring high accuracy over complex features.
* **YOLOv8-Seg:** Adapted from object detection, offering a balance between instance segmentation accuracy and real-time processing speed.

### 4. Implementation Details (Notebooks)
The development and training of these models are structured in the following Jupyter Notebooks:
* 🟢 `YOLO1280.ipynb` - YOLOv8 Segmentation.
* 🔵 `maskrcnn_resnet50_101.ipynb` - Mask R-CNN utilizing ResNet-50 / ResNet-101 backbones.
* 🟣 `Deeplab_resnet50_101.ipynb` - DeepLabv3 utilizing ResNet-50 / ResNet-101 backbones.
* 🟠 `Unet_segformer.ipynb` - U-Net paired with SegFormer architecture.

### 5. Training Workflows

**A. Instance/Object Segmentation (YOLO, Mask R-CNN)**
1. Annotate and format the dataset matching the architecture's requirements (e.g., `labelme2yolo` or `labelme2coco`).
2. Aggregate datasets (images + `.json` annotations).
3. Build and train models like YOLOv8-Seg and Mask R-CNN.

**B. Semantic Segmentation (U-Net, DeepLab)**
1. Parse and extract exact mask matrices from JSON annotations.
2. Prepare the dataset pairs (images + binary/multi-class masks).
3. Build and train using U-Net, SegFormer, or DeepLabv3 (ResNet backbone).

### 6. Model Evaluation
Model accuracy and robustness were validated using standard computer vision metrics:
* **IoU (Intersection over Union)**
* **Dice Coefficient**
* **Pixel Accuracy**

### 7. Prediction & Optimization
* **Visualization:** Predicted masks are overlaid onto original inputs for immediate qualitative assessment.
* **Optimization:** Hyperparameter fine-tuning (Learning Rate, Batch Size) and exploration of advanced pre-trained backbones to maximize metric performance.

---

## 📌 Architecture Reference Guide

For future expansion, the project references the following architectural categories:

| Task | Recommended Architectures |
| :--- | :--- |
| **Image Classification** | ResNet, EfficientNet, MobileNet |
| **Semantic Segmentation** | U-Net, DeepLab, PSPNet, SegFormer |
| **Object Detection / Instance Seg.** | YOLO, Faster R-CNN, Mask R-CNN, SSD |
| **Real-Time Processing** | YOLO, MobileNet, SSD |
| **Generative Image Processing**| GAN, StyleGAN, CycleGAN |

---

## 🔍 Video Demo: Best Model Inference

The training results were rigorously filtered, and the best-performing model version was selected for final testing on unseen UAV data. 

**Click the thumbnail below to watch the inference video:**

[![Watch the video](https://github.com/user-attachments/assets/3fc453cf-7dcd-4c0d-ba70-5ced35dcf8dd)](https://drive.google.com/file/d/1RX8wX9yU02q82FP6Hzq5p0T0SZayqvk1/view?usp=drive_link)
