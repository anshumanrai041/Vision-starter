# Image Blending Using Laplacian Pyramid

## Overview

This project demonstrates seamless image blending using **Gaussian Pyramids** and **Laplacian Pyramids** in OpenCV. The objective is to combine two images in a way that minimizes visible seams and preserves image details across multiple scales.

Unlike direct image concatenation, Laplacian Pyramid Blending performs blending at different frequency levels, resulting in a smoother and more natural transition between images.

---

## Project Objective

The main goals of this project are:

- Understand multi\-resolution image representation.
- Construct Gaussian Pyramids for input images.
- Generate Laplacian Pyramids from Gaussian Pyramids.
- Blend corresponding Laplacian levels.
- Reconstruct the final blended image.
- Compare direct blending with Laplacian Pyramid blending.

---

## What is a Gaussian Pyramid?

A Gaussian Pyramid is a collection of images where each level is created by:

1. Applying Gaussian smoothing.
2. Reducing the image dimensions by half.

Each successive level contains less detail while preserving the overall structure of the image.

Example:

Level 0 : 512 × 512

Level 1 : 256 × 256

Level 2 : 128 × 128

Level 3 : 64 × 64

Level 4 : 32 × 32

Level 5 : 16 × 16

Level 6 : 8 × 8

OpenCV function used:

cv2.pyrDown()

---

## What is a Laplacian Pyramid?

A Laplacian Pyramid stores the difference between adjacent Gaussian Pyramid levels.

Formula:

Laplacian Level = Current Gaussian Level

                  \-

                  Expanded Next Gaussian Level

This difference image contains:

- Edges
- Fine textures
- High\-frequency image details

OpenCV functions used:

cv2.pyrUp()

cv2.subtract()

---

## Blending Process

The blending process consists of four major steps:

### Step 1: Build Gaussian Pyramids

Create Gaussian Pyramids for both images.

Apple Image   →    Gaussian Pyramid

Orange Image  →    Gaussian Pyramid

---

### Step 2: Build Laplacian Pyramids

Generate Laplacian images using the Gaussian levels.

Gaussian Levels

       ↓

Laplacian Levels

These levels store image details that are lost during downsampling.

---

### Step 3: Blend Corresponding Levels

For each Laplacian level:

- Left half is taken from Image A.
- Right half is taken from Image B.

Apple Details \+ Orange Details

This blending is performed independently at every pyramid level.

---

### Step 4: Reconstruct Final Image

Starting from the smallest pyramid level:

Expand

↓

Add

↓

Expand

↓

Add

until the original image size is recovered.

The result is a smoothly blended image with minimal visible boundary.

---

## Workflow

Image A              Image B

   │                    │

   ▼                    ▼

Gaussian Pyramid   Gaussian Pyramid

   │                    │

   ▼                    ▼

Laplacian Pyramid  Laplacian Pyramid

   │                    │

    \\                  /

     \\                /

      ▼              ▼

     Blend Levels

           ▼

     Reconstruction

           ▼

   Final Blended Image

---

## Project Structure

image\_blending\_laplacian\_pyramid/

│

├── fruit1.jpg

├── fruit2.webp

├── image\_blending.py

│

├── outputs/

│   ├── apple\_gaussian\_levels/

│   ├── orange\_gaussian\_levels/

│   ├── apple\_laplacian\_levels/

│   ├── orange\_laplacian\_levels/

│   ├── blended\_levels/

│   └── final\_blended\_image.jpg

│

└── README.md

---

## Results

### Direct Blending

Directly combining two images creates a visible seam at the boundary.

Image A \| Image B

Problems:

- Sharp transition
- Visible boundary
- Unrealistic appearance

---

### Laplacian Pyramid Blending

Blending is performed at multiple resolution levels.

Benefits:

- Smooth transition
- Better edge preservation
- Natural appearance
- Reduced seam visibility

---

## Applications

Laplacian Pyramid Blending is commonly used in:

- Panorama Generation
- Image Stitching
- HDR Imaging
- Medical Image Processing
- Multi\-Resolution Image Analysis
- Photo Editing Software
- Computer Vision Systems

---

## Technologies Used

- Python
- OpenCV
- NumPy

---

## Key OpenCV Functions

cv2.imread()

cv2.resize()

cv2.pyrDown()

cv2.pyrUp()

cv2.subtract()

cv2.add()

cv2.imshow()

---

## Learning Outcomes

Through this project, I learned:

- Multi\-resolution image representation using pyramids.
- Construction of Gaussian and Laplacian Pyramids.
- The relationship between image smoothing and detail extraction.
- Image reconstruction from Laplacian levels.
- Seamless image blending techniques used in computer vision.
- Practical implementation of pyramid\-based image processing using OpenCV.

---

## Conclusion

This project successfully implements Laplacian Pyramid Blending using OpenCV. By decomposing images into multiple frequency levels, blending the corresponding Laplacian levels, and reconstructing the final image, a smooth and visually appealing transition between images is achieved. This technique serves as a foundation for more advanced computer vision applications such as panorama creation, image stitching, and multi\-resolution image processing.

