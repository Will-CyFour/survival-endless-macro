import pyautogui as ag

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


def fire_cannon_at_target(cannon, cannon_target):
    ag.click(cannon)
    ag.rightClick()
    ag.click(cannon)
    ag.click(cannon_target)


class Cannons:
    cannon_index = 0

    def fire_next_cannon_set(self):
        fire_cannon_at_target(cannons[self.cannon_index], cannon_targets[0])
        fire_cannon_at_target(cannons[self.cannon_index + 1], cannon_targets[1])

        self.cannon_index = (self.cannon_index + 2) % len(cannons)


