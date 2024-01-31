import pyautogui
import time

toggle_summon_key = 'n'
toggle_attack_key = 'b'
window_title = 'Mir4G[2]' # replace with the title of your window.

counter = 0 # initialize counter
pause_counter = 5 # number of iterations before pause
pause_duration = 30 # duration of pause in seconds

while True:
    active_window = pyautogui.getWindowsWithTitle(window_title)[0] # get the window with the specified title
    if not active_window.isActive: # check if the window is already active
        active_window.activate() # activate the window
    pyautogui.press(toggle_summon_key) # simulate a key press for the current key
    time.sleep(3) # wait for 3 seconds before simulating the next key press
    if not active_window.isActive: # check if the window is still active
        active_window.activate() # activate the window
    pyautogui.press(toggle_attack_key)
    counter += 1 # increment counter
    if counter == pause_counter:
        print(f"Pausing for {pause_duration} seconds...")
        time.sleep(pause_duration) # pause for specified duration
        counter = 0 # reset counter
    time.sleep(20) # wait for 20 seconds before simulating the next key press
