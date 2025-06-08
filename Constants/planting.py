import pyautogui as ag

def place_ice_shroom_and_coffee_bean():
    # first plant 440, 80
    # second plant 535, 80
    # lawn 400, 900
    ag.PAUSE = 0
    ag.click(535, 80)
    [ag.click(400, 900) for _ in range(5)]

    ag.click(440, 80)
    [ag.click(400, 900) for _ in range(5)]
    ag.rightClick()
    ag.PAUSE = 0.1

