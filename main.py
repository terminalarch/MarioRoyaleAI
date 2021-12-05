################################################# #######################################
##          [AUTHOR] TERMINALARCH              ## ##            [LICENSE]              ##             
##             MARIO ROYALE "AI"               ## ##           GNU LICENSE             ##
##     github.com/terminalarch/MarioRoyaleAI   ## ##     Free Open-source software     ##
################################################# #######################################
from pynput.keyboard import Key, Controller
import configparser
import time, random, threading

keyboard = Controller()
print("Awake, waiting 5 seconds")
for i in range(5):
    print(i + 1)
    time.sleep(1)

# Configuration
config = configparser.ConfigParser()
config.read('conf.cfg')

class main():
    def init():
        # Variables used to block an input if it was used too many times in a row
        global left

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
interval = config.getint('Config', 'Interval')

e = threading.Event()
while not e.wait(int(interval - 0.8)):
    main.init()