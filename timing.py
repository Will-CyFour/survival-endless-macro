import sys
from time import time, sleep
from PIL import Image
import pyautogui as ag
from Constants.cannons import fire_cannon_at_target, Cannons
from Constants.imageChecker import is_huge_wave
from Constants.planting import place_ice_shroom_and_coffee_bean

now = lambda: int(round(time() * 1000))

#TODO
"""
Click on sunflowers/sun?

Planting Tallnuts in pool, planting pumpkins in pool?

Click above cannons first to remove sun.
Click cannons multiple times to remove sun.

Time cannon shots with waves. (hard)

"""

time_last_fired: int = 0
time_last_checked_for_big_wave: int = 0
time_last_used_ice_shroom = 0

big_wave_detected_at: int | None = None

cannons = Cannons()
while True:
    if now() - time_last_fired >= 7_000:
        cannons.fire_next_cannon_set()
        time_last_fired = now()

    if time_last_checked_for_big_wave >= 500 and now() - time_last_used_ice_shroom > 40_000:
        if big_wave_detected_at is None:
            time_last_checked_for_big_wave = now()
            big_wave_detected_at = now() if is_huge_wave() else None

    if big_wave_detected_at and now() - big_wave_detected_at >= 5_000:
        place_ice_shroom_and_coffee_bean()
        time_last_used_ice_shroom = now()
        big_wave_detected_at = None


