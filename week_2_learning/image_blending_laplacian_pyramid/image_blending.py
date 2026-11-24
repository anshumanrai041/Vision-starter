
import cv2
import numpy as np

# 1. Read Images
# ==========================================================

apple = cv2.imread(
    "week_2_learning/image_blending_laplacian_pyramid/fruit1.jpg"
)

orange = cv2.imread(
    "week_2_learning/image_blending_laplacian_pyramid/fruit2.webp"
)

if apple is None or orange is None:
    raise FileNotFoundError("Check image paths!")

# Resize both images to 800 x 800
apple = cv2.resize(apple, (800, 800))
orange = cv2.resize(orange, (800, 800))

print("Apple:", apple.shape)
print("Orange:", orange.shape)

# 2. Create Gaussian Pyramids
# ==========================================================

levels = 6

gp_apple = [apple.copy()]
gp_orange = [orange.copy()]

for i in range(levels):
    gp_apple.append(cv2.pyrDown(gp_apple[-1]))
    gp_orange.append(cv2.pyrDown(gp_orange[-1]))

# 3. Create Laplacian Pyramids
# ==========================================================

def create_laplacian_pyramid(gp):

    lp = []

    for i in range(len(gp) - 1):

        expanded = cv2.pyrUp(
            gp[i + 1],
            dstsize=(gp[i].shape[1], gp[i].shape[0])
        )

        lap = cv2.subtract(gp[i], expanded)

        lp.append(lap)

    lp.append(gp[-1])

    return lp


lp_apple = create_laplacian_pyramid(gp_apple)
lp_orange = create_laplacian_pyramid(gp_orange)

# 4. Create Smooth Blending Mask
# ==========================================================

mask = np.zeros((800, 800), dtype=np.float32)

# Create gradual transition around the center
transition_width = 200

center = 400

for x in range(800):

    value = 0.5 - (x - center) / transition_width

    mask[:, x] = np.clip(value, 0, 1)

# Gaussian pyramid of mask
gp_mask = [mask]

for i in range(levels):

    gp_mask.append(cv2.pyrDown(gp_mask[-1]))

# 5. Blend Laplacian Pyramids
# ==========================================================

blended_pyramid = []

for la, lo, gm in zip(
    lp_apple,
    lp_orange,
    gp_mask
):

    # Convert mask into 3 channels
    gm = cv2.merge([gm, gm, gm])

    # Convert images to float
    la = la.astype(np.float32)
    lo = lo.astype(np.float32)

    # Laplacian blending formula
    blended = (
        la * gm +
        lo * (1.0 - gm)
    )

    blended_pyramid.append(blended)

# 6. Reconstruct Final Image
# ==========================================================

reconstructed = blended_pyramid[-1]

for i in range(len(blended_pyramid) - 2, -1, -1):

    reconstructed = cv2.pyrUp(
        reconstructed,
        dstsize=(
            blended_pyramid[i].shape[1],
            blended_pyramid[i].shape[0]
        )
    )

    reconstructed = cv2.add(
        reconstructed,
        blended_pyramid[i]
    )


# Convert to uint8
reconstructed = np.clip(
    reconstructed, 0, 255
).astype(np.uint8)

# 7. Direct Blend For Comparison
# ==========================================================

direct_mask = np.zeros((800, 800), dtype=np.float32)
direct_mask[:, :400] = 1

direct_mask = cv2.merge(
    [direct_mask, direct_mask, direct_mask]
)

direct_blend = (
    apple.astype(np.float32) * direct_mask +
    orange.astype(np.float32) * (1 - direct_mask)
)

direct_blend = direct_blend.astype(np.uint8)

# 8. Display Results
# ==========================================================

cv2.imshow("Original Apple", apple)
cv2.imshow("Original Orange", orange)

cv2.imshow("Direct Blend", direct_blend)

cv2.imshow("Laplacian Pyramid Blending", reconstructed)

cv2.imwrite("laplacian_blended_800x800.jpg", reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
