import os
import requests
from PIL import Image
import sys

# Function to download an image from a URL
def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check for any errors
        image_data = response.content

        # Create the 'downloads/mj' folder if it doesn't exist
        os.makedirs(save_path, exist_ok=True)

        # Extract the filename from the URL
        filename = os.path.join(save_path, os.path.basename(image_url))

        # Save the image to the specified path
        with open(filename, 'wb') as f:
            f.write(image_data)
        
        return filename
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

# Function to split an image into four quadrants
def split_image(image):
    width, height = image.size
    left_upper = (0, 0, width // 2, height // 2)
    right_upper = (width // 2, 0, width, height // 2)
    left_lower = (0, height // 2, width // 2, height)
    right_lower = (width // 2, height // 2, width, height)

    upper_left_image = image.crop(left_upper)
    upper_right_image = image.crop(right_upper)
    lower_left_image = image.crop(left_lower)
    lower_right_image = image.crop(right_lower)

    return upper_left_image, upper_right_image, lower_left_image, lower_right_image

if __name__ == "__main__":
    while True:
        # Get the image URL as terminal input
        image_url = input("Enter the URL of the image (or 'exit' to quit): ")
        
        if image_url.lower() == 'exit':
            sys.exit(0)  # Exit the program if the user enters 'exit'

        # Download the image to the '/downloads/mj' folder
        download_folder = './mj'
        downloaded_image_path = download_image(image_url, download_folder)

        if downloaded_image_path:
            # Open the downloaded image using Pillow
            image = Image.open(downloaded_image_path)

            # Split the image into four parts
            images = split_image(image)

            # Create the '/downloads/mj/output' folder if it doesn't exist
            output_folder = os.path.join(download_folder, 'output')
            os.makedirs(output_folder, exist_ok=True)

            # Save the four images to the '/downloads/mj/output' folder
            for i, img in enumerate(images):
                img.save(os.path.join(output_folder, f"image_{i + 1}.jpg"))

            # Delete the downloaded image
            os.remove(downloaded_image_path)

            print("Image downloaded, split into four images, and the original image deleted successfully.")
