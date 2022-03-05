################################################# #######################################
##          [AUTHOR] TERMINALARCH              ## ##            [LICENSE]              ##             
##             MARIO ROYALE "AI"               ## ##           GNU LICENSE             ##
##     github.com/terminalarch/MarioRoyaleAI   ## ##     Free Open-source software     ##
################################################# #######################################

# Import libraries
from pynput.keyboard import Key, Controller
import time, random, threading

keyboard = Controller()

# Configuration
try:
    import configparser
    config = configparser.ConfigParser()
    config.read('main.cfg')
    CONFIG_IMPORT = True
except:
    print("Could not find configparser module, using fallback to defaults.")
    CONFIG_IMPORT = False

def loadData():
    if CONFIG_IMPORT == True: # Load customized data
        interval = config.getint('Config', 'Interval')
        timer = config.getint('Config', 'Timer')
    else: # Load default data
        interval = 1
        timer = 5
loadData()

def countdown():
    while timer > 0:
        print(f"{timer} seconds left")
        timer -= 1
        time.sleep(1)
countdown()

def app():
    # Choose a random number
    res = random.randrange(1, 9)

    # Iterate through numbers then choose input
    if res == 1 or res == 2: # Go right
        print("D (go right)")
        keyboard.press('d')
        time.sleep(0.4)
        keyboard.release('d')
        left = 0

    elif res == 3 or res == 4: # Right jump
        print("Space + D (right jump)")
        keyboard.press(Key.space)
        with keyboard.pressed(Key.space):
            keyboard.press('d')
            time.sleep(0.7)
            keyboard.release('d')
        keyboard.release(Key.space)

    elif res == 5: # Go left
        print("A (left)")
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')

    elif res == 6: # Jump
        print("Space (jump)")
        keyboard.press(Key.space)
        time.sleep(0.3)
        keyboard.release(Key.space)

    elif res == 7: # Pipe down
        print("S (go down)")
        keyboard.press('s')
        time.sleep(0.3)
        keyboard.release('s')

    elif res == 8: # Slight speedup/fireball
        print("Shift (fire)")
        keyboard.press(Key.shift)
        time.sleep(0.2)
        keyboard.release(Key.shift)

# Activate function every [time] seconds
e = threading.Event()
while not e.wait(int(interval)):
    app()