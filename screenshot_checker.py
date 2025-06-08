import pyautogui as ag
from PIL import Image
from time import sleep
import os
from datetime import datetime
from Constants.imageChecker import check_huge_wave

# Output directory
OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():
    try:
        while True:
            sleep(1.5)

            flag = check_huge_wave()
            if flag:
                screenshot = ag.screenshot()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filepath = os.path.join(OUTPUT_DIR, f"screenshot_{timestamp}.png")
                screenshot.save(filepath)
                print(f"Saved screenshot: {filepath}")
    except KeyboardInterrupt:
        print("Stopped by user.")

if __name__ == "__main__":
    main()
