# PIL is the Python Imaging Library
# install using pip install pillow or pip3 install pillow or conda install -c conda-forge pillow
from PIL import Image   



# Basic algo idea:
# 1. Read the images
# 2. Resize the images to 256x256 pixels each
# 3. Store pixel values of each image in a list
# 4. Check if green pixel values exist in stored list
# 5. If green pixel values exist, return True
# 6. If green pixel values do not exist, return False & print error message (optional)


def verify(image_path):
    # 1. Read the images using PIL
    image = Image.open(image_path)

    # 2. Resize the image to 256x256 pixels each using PIL
    image = image.resize((256, 256))

    # 3. Store pixel values of image in a list using PIL
    image_pixels = list(image.getdata())

    # 4. Check if green pixel values exist in stored list
    green_pixels = [pixel for pixel in image_pixels if pixel[1] > 200]

    # 5. If green pixel values exist, return True
    if len(green_pixels) > 0:
        return True
    # 6. If green pixel values do not exist, return False & print error message
    else:
        return False




"""
Having issues with the image verification using OpenCV. Pillow is working fine.
Will look into this later. 
"""