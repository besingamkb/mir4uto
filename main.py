import pyautogui
import time
import random

x_and_y = [
    (560, 290),
    (1184, 296),
    (1810, 296),
]


def automate_mir4_ultimate():
    counter = 0
    while True:
        print(counter)
        # time.sleep(5)
        for x, y in x_and_y:
            print("executing ultimate of " + str(x) + " and " + str(y))
            ultimate_clicker(x, y)
            # rand_interval = random.randint(8, 15)
            rand_interval = 3
            print("wait for " + str(rand_interval) + " seconds for the next execution")
            time.sleep(rand_interval)
        # print("executing ultimate")
        # ultimate_clicker(562, 296)
        # time.sleep(20)
        # print("executing ultimate")
        # ultimate_clicker(1184, 300)
        # time.sleep(20)
        counter += 1


def ultimate_clicker(x, y):
    pyautogui.tripleClick(x=x, y=y)


if __name__ == '__main__':
    automate_mir4_ultimate()
