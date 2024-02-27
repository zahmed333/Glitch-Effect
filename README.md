# Image Glitch Effect Program

## Description
This Python program iterates through all images in a specified folder, applies a simple glitch effect to each, and displays them sequentially.

## Requirements
- Python 3.x
- Pillow library

## Installation
First, ensure you have Python installed on your system. Then, install the Pillow library using pip:

```
pip install requirements -r
```

## Usage
1. Place all your images in a single folder.
2. Modify the `folder_path` variable in the script to the path of your images folder.
   ```python
   folder_path = 'path/to/your/folder'
   ```
3. Run the script:
   ```
   python main.py
   ```

The script will display each glitched image for a brief period before moving to the next.

## Customization
- The glitch effect can be adjusted by modifying the `glitch_effect` function.
- The display duration of each image can be changed by altering the `time.sleep(2)` value in the `display_images` function.

## Support
For support, please open an issue in the project repository or contact me


---
