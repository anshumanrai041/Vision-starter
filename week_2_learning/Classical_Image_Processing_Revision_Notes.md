# Classical Image Processing Complete Revision Notes

## Topics Covered
1. Convolution & Correlation
2. Gaussian / Box / Median Filters
3. Sobel
4. Laplacian
5. Canny Edge Detector
6. Image Pyramids
7. Morphology
8. Thresholding (Otsu)
9. Histogram Equalization

---

# 1. Convolution (The Heart of Computer Vision)

## Real Life Analogy
Imagine looking through different glasses.

- Normal glasses → Original image
- Blurry glasses → Blur filter
- Edge glasses → Edge detector
- Sharpening glasses → Sharpen filter

The operation used to create all these effects is **Convolution**.

## Formula
Output(x,y)=Σ Image(x+i,y+j) × Kernel(i,j)

Think of convolution as sliding a small window over an image and performing multiply-add operations.

## Example
Image:

```text
10 10 10
10 50 10
10 10 10
```

Kernel:

```text
1 1 1
1 1 1
1 1 1
```

Average = 130/9 = 14.44

The center pixel becomes smoother.

## Why Vision Depends on Convolution

| Task | Kernel |
|------|---------|
| Blur | Gaussian |
| Edge Detection | Sobel |
| Sharpening | Laplacian |
| CNNs | Learnable kernels |

Without convolution:
- No edge detection
- No image filters
- No CNNs

---

# Correlation vs Convolution

### Correlation
Kernel is used directly.

### Convolution
Kernel is flipped before use.

Example:

```text
1 2 3
4 5 6
7 8 9
```

Flipped:

```text
9 8 7
6 5 4
3 2 1
```

---

# 2. Noise and Filters

## Box Filter

### Idea
Average all neighboring pixels equally.

### Code
```python
blur = cv2.blur(img, (5,5))
```

### Real-Life Example
Calculating average marks of students where all students have equal importance.

### Drawback
Blurs edges.

---

## Gaussian Filter

### Idea
Nearby pixels get higher importance.

Kernel:

```text
1 2 1
2 4 2
1 2 1
```

### Code
```python
gaussian = cv2.GaussianBlur(img,(5,5),0)
```

### Best For
Gaussian Noise (camera grain, low-light images).

---

## Median Filter

### Idea
Replace center pixel with median value.

Example:

```text
10 11 12
13 255 14
15 16 17
```

Median = 14

### Code
```python
median = cv2.medianBlur(img,5)
```

### Best For
Salt-and-Pepper Noise.

Examples:
- Scanner dust
- Dead pixels
- Transmission errors

---

## Filter Selection Shortcut

| Problem | Filter |
|----------|---------|
| Gaussian Noise | Gaussian |
| Salt Pepper Noise | Median |
| Fast Blur | Box |
| Preserve Edges | Bilateral |
| Scanned Document | Median |

---

# 3. Sobel Operator

## Purpose
Detect image edges.

### Sobel X
Detects vertical edges.

Kernel:

```text
-1 0 1
-2 0 2
-1 0 1
```

### Sobel Y
Detects horizontal edges.

Kernel:

```text
-1 -2 -1
 0  0  0
 1  2  1
```

### Code
```python
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sobel_x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobel_y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
```

### Magnitude
```python
magnitude = cv2.magnitude(sobel_x,sobel_y)
```

### Real-Life Example
Tracing object boundaries like coloring books.

---

# 4. Laplacian

## Purpose
Detect edges in all directions.

Kernel:

```text
0 1 0
1 -4 1
0 1 0
```

### Code
```python
lap = cv2.Laplacian(gray,cv2.CV_64F)
```

### Real-Life Example
Crack detection in roads.

---

# 5. Canny Edge Detector

## Canny Pipeline

### Step 1: Gaussian Blur
```python
blur = cv2.GaussianBlur(gray,(5,5),0)
```

### Step 2: Gradient Computation (Sobel)
```python
gx=cv2.Sobel(...)
gy=cv2.Sobel(...)
```

### Step 3: Non-Maximum Suppression
Keep only strongest edge pixels.

### Step 4: Double Threshold

- Strong Edge: > High threshold
- Weak Edge: Between thresholds
- Noise: < Low threshold

### Step 5: Hysteresis
Keep weak edges only if connected to strong edges.

### OpenCV Code
```python
edges = cv2.Canny(gray,100,200)
```

### Real-Life Example
Finding road boundaries in self-driving cars.

---

# 6. Image Pyramids

## Real-Life Example
Google Maps Zoom In / Zoom Out.

### Gaussian Pyramid
```python
gp = cv2.pyrDown(img)
```

### Laplacian Pyramid
Stores edge/detail information between Gaussian levels.

### Uses
- Compression
- Blending
- Multi-scale detection

---

# 7. Image Blending

Example:

Apple + Orange = Orapple

### Steps
1. Gaussian Pyramid
2. Laplacian Pyramid
3. Blend Levels
4. Reconstruct

### Use Case
Seamless image merging.

---

# 8. Morphology

Works on Binary Images.

## Erosion
Shrinks white objects.

```python
eroded=cv2.erode(img,kernel)
```

Use: Remove tiny white noise.

## Dilation
Expands white objects.

```python
dilated=cv2.dilate(img,kernel)
```

Use: Repair broken text.

## Opening
Erosion + Dilation

Use: Remove small white dots.

## Closing
Dilation + Erosion

Use: Fill small holes.

### Scanned Documents
Common pipeline:

Opening → Closing

---

# 9. Thresholding

Convert grayscale image into binary image.

### Code
```python
_,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
```

### Real-Life Example
Passport scanning and OCR.

---

# 10. Otsu Thresholding

## Problem
Choosing threshold manually is difficult.

## Solution
Otsu automatically finds the optimal threshold.

### Code
```python
_,otsu=cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
```

### Real-Life Example
Adobe Scan, Microsoft Lens, CamScanner.

---

# 11. Histogram Equalization

## Purpose
Improve image contrast.

### Code
```python
equalized=cv2.equalizeHist(gray)
```

### Real-Life Examples
- X-Ray enhancement
- Satellite imagery
- Security cameras

---

# Week-2 Projects

## Project 1: Document Denoising

```text
Read Image
 ↓
Gray
 ↓
Median Blur
 ↓
Otsu Threshold
 ↓
Morphology Opening
 ↓
Save
```

## Project 2: Gaussian Pyramid

```python
pyrDown()
pyrDown()
pyrDown()
```

## Project 3: Laplacian Pyramid Blending

```text
Gaussian Pyramid
 ↓
Laplacian Pyramid
 ↓
Blend
 ↓
Reconstruct
```

---

# Final Interview Revision Table

| Topic | One-Line Memory Trick |
|---------|----------------------|
| Convolution | Sliding weighted calculator |
| Box Filter | Equal averaging |
| Gaussian Filter | Smart averaging |
| Median Filter | Outlier remover |
| Sobel | Directional edges |
| Laplacian | All-direction edges |
| Canny | Professional edge detector |
| Pyramid | Multi-scale representation |
| Morphology | Shape processing |
| Threshold | Gray → Binary |
| Otsu | Automatic threshold |
| Histogram Equalization | Contrast enhancement |
