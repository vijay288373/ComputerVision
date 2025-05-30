import shutil
import os

# Source image path
source_path = r"C:\Users\vijay\Downloads\sample_house.jpg"

# Destination folder
destination_folder = r"C:\Users\vijay\Pictures\MovedImages"

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Create full destination path
destination_path = os.path.join(destination_folder, os.path.basename(source_path))

# Move the file
shutil.move(source_path, destination_path)

print(f"Image moved to: {destination_path}")
