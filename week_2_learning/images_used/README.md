# Document Denoising using OpenCV

## Overview

This project focuses on improving the readability of noisy scanned documents using classical image processing techniques in OpenCV.

Scanned documents often contain noise introduced during scanning, photographing, compression, or transmission. Such noise reduces text clarity and negatively impacts OCR (Optical Character Recognition) performance.

The objective of this project is to remove noise while preserving textual information and produce a clean, readable document.

---

## Problem Statement

Given a noisy scanned document:

- Remove unwanted noise.
- Preserve text edges and character structures.
- Improve visual readability.
- Generate a clean binary document suitable for further processing.

---

## Techniques Used

### 1\. Grayscale Conversion

The input image is converted from BGR to grayscale:

gray = cv2.cvtColor(img, cv2.COLOR\_BGR2GRAY)

This reduces computational complexity and prepares the image for document processing operations.

---

### 2\. Median Filtering

A median filter is applied to remove salt\-and\-pepper noise while preserving text boundaries.

denoised = cv2.medianBlur(gray, 3)

Why Median Filter?

- Effective for impulse noise.
- Preserves document edges.
- Prevents character distortion.

---

### 3\. Otsu Thresholding

Automatic threshold selection is used to separate foreground text from background.

\_, thresh = cv2.threshold(

    denoised,

    0,

    255,

    cv2.THRESH\_BINARY \+ cv2.THRESH\_OTSU

)

Benefits:

- Automatically determines the optimal threshold.
- Produces a clean black\-and\-white document.
- Improves text visibility.

---

## Processing Pipeline

Input Document

↓

Grayscale Conversion

↓

Median Filtering

↓

Otsu Thresholding

↓

Clean Binary Document

---

## Folder Structure

week\_2\_learning/

│

├── denoise\_Document.py

│

└── images\_used/

    ├── document2.jpg

    ├── document3.jpg

    ├── document4.webp

    ├── document5.gif

    ├── document6.gif

    └── document7.webp

---

## Requirements

pip install opencv\-python numpy

or

pip install \-r requirements.txt

---

## How to Run

From the project root:

python week\_2\_learning/denoise\_Document.py

Or from inside the folder:

cd week\_2\_learning

python denoise\_Document.py

---

## Sample Applications

Document denoising is commonly used in:

- OCR systems
- Digitization of books
- Archival document restoration
- Invoice processing
- Form processing
- Passport and ID scanning
- Banking document verification

---

## Learning Outcomes

Through this project, the following concepts were practiced:

- Image loading with OpenCV
- Grayscale conversion
- Noise removal
- Median filtering
- Otsu thresholding
- Binary image generation
- Document enhancement

---

## Author

Anshuman Rai

Computer Vision Training Project \- Week 2

