# Gaussian and Laplacian Pyramids using OpenCV

## Overview

This project demonstrates the implementation of **Gaussian Pyramid** and **Laplacian Pyramid** techniques using OpenCV. The goal is to understand how images can be represented at multiple resolutions and how image details are progressively lost as the resolution decreases.

The project visualizes:

- Multi\-scale image representation using Gaussian Pyramids
- Extraction of image details using Laplacian Pyramids
- Loss of image information at different pyramid levels
- Reconstruction concepts used in advanced computer vision applications

---

## Objectives

- Build a Gaussian Pyramid from an input image.
- Generate a Laplacian Pyramid using Gaussian Pyramid levels.
- Visualize how image resolution changes across levels.
- Observe the loss of fine details and high\-frequency information.
- Understand the role of pyramids in image processing and computer vision.

---

## What is a Gaussian Pyramid?

A Gaussian Pyramid is a sequence of images where each level is a blurred and downsampled version of the previous level.

At every level:

1. Gaussian smoothing is applied.
2. Image dimensions are reduced by half.

Example:

Level 0 : 1024 × 1024

Level 1 : 512 × 512

Level 2 : 256 × 256

Level 3 : 128 × 128

As the pyramid level increases:

- Image size decreases
- Fine details disappear
- Only the major structures remain visible

### OpenCV Function Used

cv2.pyrDown()

---

## What is a Laplacian Pyramid?

A Laplacian Pyramid stores the difference between adjacent Gaussian Pyramid levels.

It highlights:

- Edges
- Fine textures
- Image details

Formula:

Laplacian Level = Gaussian Level − Expanded Next Gaussian Level

Each Laplacian level preserves the information that is lost during downsampling.

### OpenCV Functions Used

cv2.pyrUp()

cv2.subtract()

---

## Workflow

Input Image

      │

      ▼

Create Gaussian Pyramid

      │

      ▼

Generate Laplacian Pyramid

      │

      ▼

Visualize Detail Loss

      │

      ▼

Analyze Multi\-Resolution Representation

---

## Project Structure

gaussian\-laplacian\-pyramid/

│

├── images/

│   └── input.jpg

│

├── gaussian\_pyramid.py

├── laplacian\_pyramid.py

│

├── output/

│   ├── gaussian\_level\_0.jpg

│   ├── gaussian\_level\_1.jpg

│   ├── gaussian\_level\_2.jpg

│   ├── gaussian\_level\_3.jpg

│   ├── laplacian\_level\_0.jpg

│   ├── laplacian\_level\_1.jpg

│   ├── laplacian\_level\_2.jpg

│   └── laplacian\_level\_3.jpg

│

└── README.md

---

## Results

### Gaussian Pyramid

The Gaussian Pyramid demonstrates how the image becomes smaller and smoother at each level.

Observations:

- Resolution decreases gradually.
- High\-frequency details disappear.
- Large image structures remain visible.
- Processing becomes computationally cheaper.

---

### Laplacian Pyramid

The Laplacian Pyramid reveals information lost between Gaussian levels.

Observations:

- Edges become more prominent.
- Fine textures are preserved.
- Detail information is isolated.
- Useful for image blending and reconstruction.

---

## Analysis of Information Loss

The pyramid representation shows that image information is not uniformly distributed.

### Low Pyramid Levels

Contain:

- Fine textures
- Sharp edges
- Small objects

### Higher Pyramid Levels

Contain:

- Overall object shapes
- Coarse image structure
- Reduced detail information

This demonstrates how computer vision systems can analyze images at multiple scales efficiently.

---

## Applications

Image pyramids are widely used in:

- Image Blending
- Feature Detection (SIFT)
- Object Detection
- Image Compression
- Image Stitching
- Optical Flow
- Multi\-Scale Analysis
- Medical Imaging
- Face Detection

---

## Technologies Used

- Python 3
- OpenCV
- NumPy

---

## Learning Outcomes

Through this project, I learned:

- The concept of multi\-resolution image representation.
- How Gaussian Pyramids progressively reduce image size.
- How Laplacian Pyramids capture lost image details.
- The relationship between image resolution and information content.
- Practical implementation of image pyramids using OpenCV.
- Real\-world applications of image pyramids in computer vision systems.

---

## Conclusion

This project provides a practical understanding of Gaussian and Laplacian Pyramids. By visualizing different pyramid levels, it becomes clear how image information is compressed, represented, and preserved across multiple resolutions. These concepts form the foundation of many advanced computer vision tasks such as image blending, feature extraction, and object detection.

