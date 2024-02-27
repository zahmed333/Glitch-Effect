import os
from PIL import Image, ImageChops
import time

def glitch_effect(image_path):
    """Applies a basic glitch effect to an image."""
    # Open the image
    original = Image.open(image_path)
    
    # Split the image into RGB bands
    r, g, b = original.split()
    
    # Shift the bands
    r_shift = ImageChops.offset(r, 5, 0)  # Shift red band
    g_shift = ImageChops.offset(g, 0, 0)  # No shift for green
    b_shift = ImageChops.offset(b, -5, 0) # Shift blue band
    
    # Merge the bands back
    result = Image.merge('RGB', (r_shift, g_shift, b_shift))
    
    return result

def display_images(folder_path):
    """Goes through every image in a folder, applies glitch effect, and displays them."""
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            
            # Apply glitch effect
            glitched = glitch_effect(image_path)
            
            # Display the image
            glitched.show()
            
            # Wait before moving to the next photo
            time.sleep(2)  # Adjust as needed

current_directory = os.getcwd()
print(current_directory)
# Specify your folder path here
folder_path = 'AllFabricImages'
display_images(folder_path)
