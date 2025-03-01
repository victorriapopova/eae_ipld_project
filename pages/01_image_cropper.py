import streamlit as st
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

img_path = "data/starry_night.png"

# Открываем изображение и конвертируем в массив numpy
with Image.open(img_path) as img:
    img_arr = np.array(img)

# Отображаем изображение
plt.imshow(img_arr)
plt.axis('off')  # Это выключает оси, если не хотите их видеть
st.image(img_arr)

# Ex 1.1: Get the height and width of the image in pixels

# Get the height and width of the image in pixels
max_height, max_width = img_arr.shape[:2]  # shape[0] is height, shape[1] is width

# Print the height and width
f"Height: {max_height} pixels"
f"Width: {max_width} pixels"

# Ex 1.2: Define the dimensions of the crop, make sure that min is smaller than max and also that min is larger than 0
# and max is smaller than the size of the image for every dimension. If not, print a message explaining the error.

# Example crop dimensions, modify them to test your code
crop_min_h = 600
crop_max_h = 1000
crop_min_w = 550
crop_max_w = 1100

# Constraint checks

if not (0 < crop_min_h < crop_max_h < max_height):
    print(f"Error: Crop height boundaries are invalid. Ensure 0 < min_h < max_h < {max_height}.")
elif not (0 < crop_min_w < crop_max_w < max_width):
    print(f"Error: Crop width boundaries are invalid. Ensure 0 < min_w < max_w < {max_width}.")
elif crop_min_h >= crop_max_h:
    print("Error: crop_min_h should be smaller than crop_max_h.")
elif crop_min_w >= crop_max_w:
    print("Error: crop_min_w should be smaller than crop_max_w.")
else:
    print("Crop dimensions are valid.")


# TODO: Develop the code to validate the constraints and print the error message if any constraint is invalid

# Ex 1.3: Generate the crop array into a new variable, use NumPy array slicing

crop_arr = img_arr[crop_min_h:crop_max_h, crop_min_w:crop_max_w]
crop_img = Image.fromarray(crop_arr)
plt.imshow(crop_arr)
st.image(crop_arr)
file_name = "starry_night_cropped"
crop_img.save(f"/data/{file_name}.png")