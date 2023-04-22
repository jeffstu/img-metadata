import os
import glob
from PIL import Image, ImageTk
import yaml
import tkinter as tk

def load_existing_metadata(directory):
    yaml_file = os.path.join(directory, "image_info.yaml")
    if os.path.exists(yaml_file):
        with open(yaml_file, "r") as f:
            return yaml.safe_load(f)["images"]
    else:
        return []

def save_image_metadata(directory, image_metadata):
    yaml_file = os.path.join(directory, "image_info.yaml")
    with open(yaml_file, "w") as f:
        yaml.dump({"images": image_metadata}, f)

def main():
    directory = input("Enter the directory path containing the images: ")
    image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif"]

    existing_metadata = load_existing_metadata(directory)
    existing_filenames = {entry["filename"] for entry in existing_metadata}
    image_metadata = existing_metadata.copy()

    image_files = [
        img
        for ext in image_extensions
        for img in glob.glob(os.path.join(directory, ext))
        if not "_thumb" in img and os.path.basename(img) not in existing_filenames
    ]

    if not image_files:
        print("No images to process")
        return

    root = tk.Tk()
    root.title("Image Metadata Entry")

    img_label = tk.Label(root)
    img_label.grid(row=0, column=0, columnspan=2)

    title_label = tk.Label(root, text="Title: ")
    title_label.grid(row=1, column=0)
    title_entry = tk.Entry(root)
    title_entry.grid(row=1, column=1)

    desc_label = tk.Label(root, text="Description: ")
    desc_label.grid(row=2, column=0)
    desc_entry = tk.Entry(root)
    desc_entry.grid(row=2, column=1)

    def save_and_next():
        nonlocal image_files
        title = title_entry.get()
        description = desc_entry.get()

        if title and description:
            image_file = image_files.pop(0)
            image_metadata.append({
                "filename": os.path.basename(image_file),
                "title": title,
                "description": description
            })

            title_entry.delete(0, tk.END)
            desc_entry.delete(0, tk.END)

            if image_files:
                show_image(image_files[0])
            else:
                save_image_metadata(directory, image_metadata)
                print(f"YAML file saved in {directory}")
                root.quit()

    def show_image(image_path):
        img = Image.open(image_path)
        img.thumbnail((600, 600))
        imgtk = ImageTk.PhotoImage(img)
        img_label.config(image=imgtk)
        img_label.image = imgtk

    show_image(image_files[0])

    save_button = tk.Button(root, text="Save and Next", command=save_and_next)
    save_button.grid(row=3, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()
