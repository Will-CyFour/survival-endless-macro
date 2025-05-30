from time import time, sleep
from PIL import Image
import pyautogui as ag

now = lambda: int(round(time() * 1000))

cannon_location_1 = (500,500)
cannon_location_2 = (500,650)
cannon_targets = (
    (1450, 875),
    (1450, 400)
)

cannons = (
    (500, 500),
    (500, 650),
    (800, 500),
    (800, 650),
    (1100, 500),
    (1100, 650),
    (1100, 200),
    (1100, 350),
    (1100, 800),
    (1100, 1000),
)
assert len(cannons) % 2 == 0

def fire_cannon_at_target(cannon, cannon_target):
    ag.click(cannon)
    ag.rightClick()
    ag.click(cannon)
    ag.click(cannon_target)

# returns next cannon index
def fire_next_cannon_set(cannon_index) -> int:
    fire_cannon_at_target(cannons[cannon_index], cannon_targets[0])
    fire_cannon_at_target(cannons[cannon_index + 1], cannon_targets[1])

    return (cannon_index + 2) % len(cannons)

next_cannon_index = 0

time_last_fired: int = now()
def check_huge_wave():
    big_wave_color = (244, 0, 0)
    # screenshot = ag.screenshot()
    screenshot = Image.open('image_library/huge_wave_3.png')

    return screenshot.getpixel((240, 710)) == (249, 242, 216)

print(check_huge_wave())

sleep(500)
while True:
    if now() - time_last_fired >= 7000:
        next_cannon_index = fire_next_cannon_set(next_cannon_index)
        time_last_fired = now()
    # if (big_wave_detected):
    #     time_wave_detected = now()
    # if (time_wave_detected and now() time_wave_detected >= 5000):
    #     plant ice shroom and coffee bean
    #     time_wave_detected = None


