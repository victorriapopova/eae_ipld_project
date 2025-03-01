import numpy as np
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt


img_path = "data/starry_night.png"

with Image.open(img_path) as img:
    img_arr = np.array(img)

'Before cropping'

st.image(img_arr)

max_height = img_arr.shape[0]
max_width = img_arr.shape[1]

f"Height: {max_height} pixels"
f"Width: {max_width} pixels"


crop_min_h = 600
crop_max_h = 1000
crop_min_w = 550
crop_max_w = 1100

if (crop_min_h < 0) or (crop_min_w < 0):
    print('Min value has to be > 0')

if crop_max_h > max_height:
    print(f'Max crop height has to be less than {max_height}') 

if crop_max_w > max_width:
    print(f'Max crop width has to be less than {max_width}')

f'Crop dimensions (h:h,w:w): {crop_min_h}:{crop_max_h}, {crop_min_w}:{crop_max_w}'

crop_arr = img_arr[crop_min_h:crop_max_h, crop_min_w:crop_max_w]

crop_img = Image.fromarray(crop_arr)

file_name = 'cropped_starry_night'

crop_img.save(f"data/{file_name}.png")

'After cropping'

st.image(crop_img)
