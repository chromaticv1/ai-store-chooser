
import os
import pandas as pd
import sys
sys.path.append('src')
from data_extractor import img_extr_2

# Get all images from example_images
image_dir = "example_images"
files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]

print(f"Processing {len(files)} images...")
try:
    df = img_extr_2(files)
    df.to_csv("src/demo_data.csv", index=False)
    print("Successfully saved demo_data.csv")
    print(df.head())
except Exception as e:
    print(f"Error: {e}")
