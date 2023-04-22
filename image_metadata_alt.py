import os
import glob
from PIL import Image
import yaml
import cv2

# Function to display image preview
def display_preview(image_path):
    img = cv2.imread(image_path)
    window_name = os.path.basename(image_path)
    cv2.imshow(window_name, img)
    cv2.waitKey(1)

# Function to close image preview
def close_preview(window_name):
    cv2.destroyWindow(window_name)

# Function to input metadata and save YAML file
def save_image_metadata(directory, image_metadata):
    yaml_file = os.path.join(directory, "image_info.yaml")
    with open(yaml_file, "w") as f:
        yaml.dump({"images": image_metadata}, f)

def main():
    directory = input("Enter the directory path containing the images: ")
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

    image_metadata = []

    for ext in image_extensions:
        for image_file in glob.glob(os.path.join(directory, ext)):
            if not "_thumb" in image_file:  # Ignore thumbnail images
                window_name = os.path.basename(image_file)
                display_preview(image_file)
                title = input(f"Enter the title for {window_name}: ")
                description = input(f"Enter the description for {window_name}: ")

                image_metadata.append({
                    "filename": window_name,
                    "title": title,
                    "description": description
                })

                close_preview(window_name)

    save_image_metadata(directory, image_metadata)
    print(f"YAML file saved in {directory}")

if __name__ == "__main__":
    main()
