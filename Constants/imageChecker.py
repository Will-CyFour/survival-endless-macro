
from PIL import Image
import pyautogui as ag

def is_huge_wave():
    BIG_WAVE_COLOR = (244, 0, 0)
    screenshot = ag.screenshot(region=(807, 564, 1, 1))
    return screenshot.getpixel((0,0))[:3] == BIG_WAVE_COLOR

def mess_up_everything(x, y):
    screenshot = Image.open('../image_library/more_zombies_approaching.png')
    for i in range (x - 5, x + 5):
        for j in range(y - 5, y + 5):
            screenshot.putpixel((i, j),(255,255,255,255))
    screenshot.save('test.png')


def is_end_of_level():
    END_OF_LEVEL_COLOR = (116, 106, 116)
    screenshot = ag.screenshot(region=(248, 611, 1, 1))
    return screenshot.getpixel((248, 611))[:3] == END_OF_LEVEL_COLOR

