import pyautogui as ag
from PIL import Image

# with Image.open('present_closeup.png') as im:
#     width, height = im.size
#     middle_height = height // 2
#     middle_row: Image = im.crop((0, middle_height, width, middle_height + 1))
#     middle_row.save('present_middle_row.png')

with Image.open('image_library/present_middle_row.png').convert('RGB') as im:
    pixels = im.load()
    width, height = im.size
    middle_height = height // 2
    middle_row_pixels = [pixels[x, middle_height] for x in range(width)]
    print(middle_row_pixels)
