# Image Metadata Entry

This Python script is designed to help you add title and description metadata for images in a directory. The metadata is saved in a YAML file called `image_info.yaml`. The script will prompt for input only for images that don't have metadata in the existing YAML file.

## Requirements

- Python 3.6 or higher
- Pillow
- PyYAML
- Tkinter (included in Python's standard library)

if you use the alt script you will also need

- opencv-python

## Setting Up a Python Virtual Environment

It's a good practice to use a virtual environment when working with Python projects. This helps keep dependencies required by different projects separate and ensures a clean working environment. Follow the steps below to set up a virtual environment for this script:

1. Open a terminal or command prompt and navigate to the directory where you want to store the virtual environment.

2. Run the following command to create a virtual environment named `imgmeta` (you can replace `imgmeta` with a name of your choice):
```
python3 -m venv imgmeta
```

3. Activate the virtual environment:

- On macOS and Linux:

  ```
  source imgmeta/bin/activate
  ```

- On Windows:

  ```
  imgmeta\Scripts\activate
  ```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Once you have installed the required packages, you can run the script within the virtual environment.

## Usage

1. Copy the Python script into the directory containing your images and the `image_info.yaml` file.

2. Run the script:


3. Follow the prompts to enter title and description metadata for the images in the directory.
