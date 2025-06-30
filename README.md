# Phân đoạn hình ảnh
![output_DJI_20240421090742_0001_D](https://github.com/user-attachments/assets/0157b05c-a856-4e3a-8fff-f623992cddac)

# Segmentation-of-rice-field-images-captured-by-UAV-graduationthesis-
    Data_set: 5280 × 3956 pixels, sl: 201
    -----------
    Data_train: Data_set_resize, size: 1280 × 960, sl: 201
    Data_test: 21
    Gán nhãn dữ liệu: anylabeling - python3.9
    Huấn luyện trên github.
    Thư viện:
        TensorFlow/Keras: U-Net, DeepLab.
        PyTorch: Mask R-CNN, PSPNet.
        OpenCV: xử lý ảnh
    -----------
    1. Chuẩn bị dữ liệu
        Dữ liệu hình ảnh: Thu thập hình ảnh cần phân đoạn.
        Chia dữ liệu: Chia dữ liệu thành tập huấn luyện (train), tập kiểm tra (test), và tập validation.

    2. Tiền xử lý dữ liệu
        Phân đoạn theo đối tượng: gán dữ liệu và chia thành 3 tập train val test
        Phân đoạn theo ngữ nghĩa
        Resize hình ảnh: Đưa tất cả hình ảnh và mask về cùng kích thước.
        Chuẩn hóa: Chuẩn hóa giá trị pixel về khoảng [0, 1] hoặc [-1, 1].
        Data Augmentation: Áp dụng các kỹ thuật như xoay, lật, crop, thay đổi độ sáng để tăng cường dữ liệu.
    3. Chọn mô hình
        U-Net: Phù hợp cho bài toán phân đoạn y tế (ví dụ: phân đoạn khối u trong ảnh y tế).
        Mask R-CNN: Phù hợp cho bài toán phân đoạn đối tượng và instance segmentation.
        DeepLab: Phù hợp cho bài toán semantic segmentation với độ chính xác cao.
        YOLO
        Phân đoạn ảnh ngữ nghĩa: U-Net, DeepLab
        Phân đoạn ảnh đối tượng: YOLO(labelme2yolo), Faster R-CNN(labelme2COCO)
    4. Xây dựng mô hình
    - Yolo: YOLO1280.ipynb
    - Mark-RCNN + resnet(50 - 101): maskrcnn_resnet50_101.ipynb
    - Deeplabv3 + resnet(50 - 101): Deeplab_resnet50_101.ipynb
    - UnetSegformet: Unet_segformer.ipynb
    5. Huấn luyện mô hình
    Phân đoạn theo đối tượng:
        b1. Gán nhãn và chuẩn bị dữ liệu theo yêu cầu từng mô hình.
        b2. Chuẩn bị dữ liệu (ảnh và json).
        b3. Xây dựng và huấn luyện mô hình (Yolov8 segmentation, Mask R-CNN)
    Phân đoạn ngữ nghĩa:
        b1. Đọc và xử lý dữ liệu từ file JSON.
        b2. Chuẩn bị dữ liệu (ảnh và mask).
        b3. Xây dựng và huấn luyện mô hình (U-Net segmentation tranformer, DeepLabv3 + resnet)
    6. Đánh giá mô hình
        Sử dụng các chỉ số như IoU (Intersection over Union), Dice Coefficient, hoặc Pixel Accuracy để đánh giá hiệu suất mô hình.
    7. Dự đoán và hiển thị kết quả
        Sử dụng mô hình đã huấn luyện để dự đoán trên dữ liệu mới.
        Hiển thị kết quả phân đoạn bằng cách vẽ mask dự đoán lên hình ảnh gốc.
    8. Tối ưu hóa và cải thiện
    
    --------------
    Phân loại ảnh: ResNet, EfficientNet, MobileNet.
    Phân đoạn ảnh: U-Net, DeepLab, Mask R-CNN, PSPNet.
    Phát hiện đối tượng: YOLO(labelme2yolo), Faster R-CNN(labelme2COCO), SSD.
    Thời gian thực: YOLO, MobileNet, SSD.
    Tạo ảnh: GAN, StyleGAN, CycleGAN.
# Kết quả huấn luyện được lọc và lấy ra phiên bản mô hình tốt nhất để test
[![Watch the video](https://github.com/user-attachments/assets/3fc453cf-7dcd-4c0d-ba70-5ced35dcf8dd)](https://drive.google.com/file/d/1RX8wX9yU02q82FP6Hzq5p0T0SZayqvk1/view?usp=drive_link)

