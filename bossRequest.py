import pyautogui
import pygetwindow as gw
import time
import random

mir4_window_title = "Mir4G[1]"
favorite_x = 1270
favorite_y = 255
fast_travel_x = 780
fast_travel_y = 920

boss_coordinates = [
    {'label': '1st Boss', 'x': 960, 'y': 215, 'interval': 15},
    {'label': '2nd Boss', 'x': 960, 'y': 340, 'interval': 15},
    {'label': '3rd Boss', 'x': 960, 'y': 470, 'interval': 15},
    # {'label': 'Yellow Boss', 'x': 2900, 'y': 600, 'interval': 20},
    # Add more coordinates here
]

fast_click_interval = [0.3, 0.4, 0.5]


def focus_window(title):
    try:
        # Get the window by title
        window = gw.getWindowsWithTitle(title)[0]
        # If the window is minimized
        if window.isMinimized:
            window.restore()
        # Bring the window to front
        window.activate()
    except IndexError:
        print(f"No window with title '{title}' found.")


def minus_or_add(n, a1=5, a2=15):
    operation = ['add', 'minus']
    return n + random.randint(a1, a2) if random.choice(operation) == "add" else n - random.randint(a1, a2)


def kill_the_boss(x, y, end_interval):
    # Type 'a'
    pyautogui.press('y')
    time.sleep(1)

    # Move the cursor to the position (x, y)
    pyautogui.moveTo(minus_or_add(favorite_x), minus_or_add(favorite_y), random.choice(fast_click_interval))
    # Perform the click
    pyautogui.click()
    time.sleep(1)

    # Move the cursor to the position (x, y)
    pyautogui.moveTo(minus_or_add(x), minus_or_add(y), random.choice(fast_click_interval))
    # Perform the click
    pyautogui.click()
    time.sleep(1)

    # Move the cursor to the position (x, y)
    pyautogui.moveTo(minus_or_add(fast_travel_x), minus_or_add(fast_travel_y), random.choice(fast_click_interval))
    # Perform the click
    pyautogui.click()

    pyautogui.moveTo(minus_or_add(200, 10, 40), minus_or_add(200, 10, 40), random.choice(fast_click_interval))
    time.sleep(random.randint(5, 15))

    # Type 'a'
    pyautogui.press('b')
    time.sleep(minus_or_add(end_interval, 2, 5))


# Infinite loop
while True:
    # Focus on the window by its title
    focus_window(mir4_window_title)

    for coordinate in boss_coordinates:
        print(f"Attacking {coordinate['label']} at ({coordinate['x']}, {coordinate['y']})")
        kill_the_boss(coordinate['x'], coordinate['y'], coordinate['interval'])

    # Sleep for 1 second to avoid overloading
    time.sleep(random.randint(5, 10))
