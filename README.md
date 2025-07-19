# Image segmentation
![output_DJI_20240421090742_0001_D](https://github.com/user-attachments/assets/0157b05c-a856-4e3a-8fff-f623992cddac)

# Segmentation-of-rice-field-images-captured-by-UAV-graduationthesis-
Data_set: 5280 × 3956 pixels, sl: 201
-----------
Data_train: Data_set_resize, size: 1280 × 960, sl: 201
Data_test: 21
labeling image: anylabeling - python3.9
training on Colab.
Thư viện:
-----------
1. Data Preparation
    Image data: Collect images that require segmentation.
    Dataset splitting: Divide the dataset into training, validation, and testing sets.
2. Data Preprocessing
    Object-level segmentation: Annotate images and split into train, validation, and test sets accordingly.
    Semantic segmentation: Ensure consistent labeling across classes.
    Image resizing: Resize all images and corresponding masks to a uniform shape.
    Normalization: Normalize pixel values to the range [0, 1] or [-1, 1].
    Data augmentation: Apply techniques such as rotation, flipping, cropping, and brightness adjustment to enhance the dataset and reduce overfitting.
3. Model Selection
    U-Net: Well-suited for medical image segmentation tasks (e.g., tumor segmentation).
    Mask R-CNN: Ideal for instance segmentation and object-level segmentation.
    DeepLab: Suitable for semantic segmentation tasks requiring high accuracy.
    YOLO: While primarily for object detection, it can be adapted for segmentation tasks via labeling conversion tools.
    Semantic segmentation models: U-Net, DeepLab.
    Instance/object segmentation models: YOLO (via labelme2yolo), Faster R-CNN (via labelme2coco).
4. Model Development
    - Yolo: YOLO1280.ipynb
    - Mark-RCNN + resnet(50 - 101): maskrcnn_resnet50_101.ipynb
    - Deeplabv3 + resnet(50 - 101): Deeplab_resnet50_101.ipynb
    - UnetSegformet: Unet_segformer.ipynb
5. Model Training
    Instance/Object Segmentation:
        Step 1: Annotate and format the dataset according to the requirements of each model.
        Step 2: Prepare the dataset (images and corresponding .json annotation files).
        Step 3: Build and train the model using architectures such as YOLOv8 Segmentation and Mask R-CNN.
    Semantic Segmentation:
        Step 1: Parse and process label data from JSON annotation files.
        Step 2: Prepare the dataset (images and corresponding segmentation masks).
        Step 3: Build and train the model using architectures like U-Net, Segmentation Transformers, or DeepLabv3 with ResNet backbone.
6. Model Evaluation
    Evaluate model performance using metrics such as:
        IoU (Intersection over Union)
        Dice Coefficient
        Pixel Accuracy
7. Prediction and Visualization
    Use the trained model to make predictions on new or unseen data.
    Visualize the results by overlaying the predicted masks on the original input images for qualitative assessment.
8. Optimization and Improvement
    Fine-tune hyperparameters (e.g., learning rate, batch size).
    Explore advanced architectures or pre-trained backbones.

--------------
Phân loại ảnh: ResNet, EfficientNet, MobileNet.
Phân đoạn ảnh: U-Net, DeepLab, Mask R-CNN, PSPNet.
Phát hiện đối tượng: YOLO(labelme2yolo), Faster R-CNN(labelme2COCO), SSD.
Thời gian thực: YOLO, MobileNet, SSD.
Tạo ảnh: GAN, StyleGAN, CycleGAN.
# 🔍 The training results were filtered, and the best-performing model version was selected for testing (click to view)
[![Watch the video](https://github.com/user-attachments/assets/3fc453cf-7dcd-4c0d-ba70-5ced35dcf8dd)](https://drive.google.com/file/d/1RX8wX9yU02q82FP6Hzq5p0T0SZayqvk1/view?usp=drive_link)

