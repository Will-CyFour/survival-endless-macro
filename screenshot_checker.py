import pyautogui as ag
from PIL import Image
import time
import os
from datetime import datetime

# Target hex color
TARGET_HEX = "#651510"
TARGET_RGB = tuple(int(TARGET_HEX[i:i+2], 16) for i in (1, 3, 5))
TARGET_RGB = (87, 6, 6)


# Output directory
OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def contains_color(img: Image.Image, target_rgb: tuple) -> bool:
    pixels = img.convert('RGB').getdata()
    return target_rgb in pixels

def main():
    print("Monitoring screen for color:", TARGET_RGB)
    try:
        while True:
            screenshot = ag.screenshot()
            if contains_color(screenshot, TARGET_RGB):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filepath = os.path.join(OUTPUT_DIR, f"screenshot_{timestamp}.png")
                screenshot.save(filepath)
                print(f"Saved screenshot: {filepath}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    main()
