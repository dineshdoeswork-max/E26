#8.1

import numpy as np

# 1. SETUP: Create two "images" (3x3 pixels, 3 color channels)
# img1 is all 100s (gray)
# We use uint8 because that's the standard for image pixels (0-255)
img1 = np.full((3, 3, 3), 100, dtype=np.uint8)

# img2 is all 10s (very dark)
img2 = np.full((3, 3, 3), 10, dtype=np.uint8)

print("--- INITIAL DATA ---")
print(f"Image 1 :\n{img1}")
print(f"Image 2 :\n{img2}\n")

# # 2. MATRIX ADDITION (Brightening)
# # Adds corresponding pixels together
added = img1 + img2

# # 3. MATRIX SUBTRACTION (Darkening)
# # Subtracts img2 values from img1
subbed = img1 - img2

# # 4. ELEMENT-WISE MULTIPLICATION (Scaling)
# # Multiplies each pixel by a factor
multiplied = img1 * 2

# # 5. MATRIX MULTIPLICATION (Dot Product / Color Filtering)
# # We use a 3x3 filter to transform the 3 color channels
# # This example effectively scales the channels
color_filter = np.array([[1, 0, 0], 
                         [0, 1, 0], 
                         [0, 0, 1.5]]) 
matrix_mult = img1 @ color_filter

# # 6. TRANSPOSE (Axis Swapping)
# # Swaps Height (0) and Width (1), keeps Channels (2)
transposed = img1.transpose(1, 0, 2)

# --- PRINTING RESULTS ---
print("--- RESULTS ---")
print(f"Addition :\n{added}")
print(f"Subtraction (100 - 10) :\n{subbed}")
print(f"Multiplication (100 * 2) :\n{multiplied}")
print(f"Matrix Mult :\n{matrix_mult}") # Shows all 3 channels
print(f"Original Shape :\n{img1.shape}")
print(f"Transposed Shape :\n{transposed.shape}")
