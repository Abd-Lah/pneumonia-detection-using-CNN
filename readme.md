# Chest X-Ray Pneumonia Detection Using CNN 

This project aims to detect pneumonia from chest X-ray images using Convolutional Neural Network (CNN) models. The dataset is sourced from <a href="https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia">Kaggle </a> and includes both Pneumonia and Normal categories. The project explores different CNN architectures, preprocessing techniques, and addresses dataset imbalance issues.

## Table of Contents
1. [Dataset Description](#dataset-description)
2. [Data Preprocessing and Splitting](#data-preprocessing-and-splitting)
3. [Explanation of Dataset Imbalance](#explanation-of-dataset-imbalance)
4. [Built Models](#built-models)
    - [VGG16](#vgg16)
    - [ResNet50](#resnet50)
    - [Net5 (Adapted from LeNet-5)](#net5-adapted-from-lenet-5)
5. [Web Application: Chest X-Ray Classifier](#web-application-chest-x-ray-classifier)
6. [Conclusion](#conclusion)

## Dataset Description

The dataset sourced from Kaggle comprises 5,863 chest X-ray images categorized into Pneumonia and Normal, organized into three folders: train, test, and validation. Each folder contains subfolders for each image category.

- **Train**: Contains 5,216 X-ray images.
- **Test**: Contains 624 X-ray images.
- **Validation**: Contains 16 X-ray images.

## Data Preprocessing and Splitting

To prepare the dataset for training, several preprocessing steps were undertaken:

- Invalid or corrupt images were removed.
- Pixel values were normalized to the range [0, 1].
- ImageDataGenerator from TensorFlow was used for data augmentation with transformations like rotation, shifts, shear, zoom, and flips.
- Categorical labels were converted to numerical format: 0 for Normal and 1 for Pneumonia.

The dataset was split into training, validation, and test sets to ensure unbiased model evaluation.

## Explanation of Dataset Imbalance

The training dataset contains more images in the Pneumonia class compared to the Normal class. Initially, the dataset was artificially balanced using oversampling, but this led to overfitting in all three models. Subsequently, the original dataset was used with the Net5 architecture, achieving an 80% validation accuracy.

## Built Models

### VGG16

- **Architecture**:
    - 16 weight layers: 13 convolutional layers and 3 fully connected layers.
    - Input images of size 224x224.
- **Training Process**:
    - Trained using the Adam optimizer with categorical cross-entropy loss.
    - Dataset with 4,000 images per class, 15% for validation.
    - Early stopping implemented after 21 epochs.
- **Evaluation**:
    - Achieved a peak validation accuracy of 98.14%.
    - High precision, recall, and F1-score in the classification report.
- **Conclusion**:
    - Excellent performance but faced overfitting issues with the augmented dataset.

### ResNet50

- **Architecture**:
    - Deep residual network with 50 layers.
- **Training Process**:
    - Similar training setup as VGG16.
- **Evaluation**:
    - Achieved similar results to VGG16, with high accuracy but overfitting on the augmented dataset.

### Net5 (Adapted from LeNet-5)

- **Architecture**:
    - Adapted for grayscale chest X-ray images with 100x100 resolution.
    - Three convolutional layers with batch normalization and max-pooling.
    - Final dense layers with ReLU activations and dropout for regularization.
- **Training Process**:
    - Trained using the Adam optimizer and binary cross-entropy loss.
    - Original dataset used after oversampling led to overfitting.
- **Evaluation**:
    - Achieved an 80% validation accuracy without overfitting.

## Web Application: Chest X-Ray Classifier

A Flask web application was developed to provide functionalities for displaying test images and predicting whether a given chest X-ray image indicates pneumonia or is normal.

### Features

- **Loading Test Images**:
    - Displays the test images available in the test_images directory.
- **Predicting Image Label**:
    - Allows users to upload or select a chest X-ray image for prediction.
    - The model predicts and returns whether the image indicates "PNEUMONIA" or "NORMAL".

## Conclusion

This project demonstrates the effectiveness of CNN models in detecting pneumonia from chest X-ray images. Despite the challenges of dataset imbalance and overfitting, the Net5 model achieved an 80% validation accuracy using the original dataset. The project also includes a web application for easy deployment and testing of the trained models.

