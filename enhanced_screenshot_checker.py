import pyautogui
from PIL import Image
import time
import os
from datetime import datetime

from Constants import Constants

TARGET_ROW_PATTERN = Constants.PRESENT_RGB_ROWS
PATTERN_LENGTH = len(TARGET_ROW_PATTERN)

OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def row_contains_pattern(pixels, width, y, pattern):
    for x in range(width - PATTERN_LENGTH + 1):
        match = True
        for i, expected in enumerate(pattern):
            if pixels[x + i, y] != expected:
                match = False
                break
        if match:
            return True
    return False

def screenshot_contains_row_pattern(img: Image.Image, pattern: list) -> bool:
    img_rgb = img.convert("RGB")
    pixels = img_rgb.load()
    width, height = img_rgb.size

    for y in range(height):
        if row_contains_pattern(pixels, width, y, pattern):
            return True
    return False

def main():
    print("Monitoring screen for row pattern match...")
    try:
        while True:
            screenshot = pyautogui.screenshot()
            if screenshot_contains_row_pattern(screenshot, TARGET_ROW_PATTERN):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filepath = os.path.join(OUTPUT_DIR, f"match_{timestamp}.png")
                screenshot.save(filepath)
                print(f"Saved screenshot: {filepath}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    main()
