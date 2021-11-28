################################################# #######################################
##          [AUTHOR] TERMINALARCH              ## ##            [LICENSE]              ##             
##             MARIO ROYALE "AI"               ## ##           GNU LICENSE             ##
##     github.com/terminalarch/MarioRoyaleAI   ## ##     Free Open-source software     ##
################################################# #######################################
from pynput.keyboard import Key, Controller
import time, random, threading

keyboard = Controller()
print("Awake, waiting 5 seconds")
time.sleep(5)

while True:
    right = 0 # times in a row count
    left = 0 # times in a row count
    class Random:
        def init():
            # Variables used to block an input if it was used too many times in a row
            global left
            global right

            # Choose a random number
            res = random.randrange(1, 7)

            # Iterate through numbers then choose input
            if res == 1: # Go left
                if left > 2:
                    left = 0
                    print("Cancelled left input")
                    return
                print("A (go left)")
                keyboard.press('a')
                time.sleep(0.2)
                keyboard.release('a')
                left += 1
                right = 0

            elif res == 2: # Go right
                if right > 2:
                    right = 0
                    print("Cancelled right input")
                    return
                print("D (go right)")
                keyboard.press('d')
                time.sleep(1)
                keyboard.release('d')
                right += 1
                left = 0

            elif res == 3: # Down
                print("S (go down)")
                keyboard.press('s')
                time.sleep(0.3)
                keyboard.release('s')

            elif res == 4: # Jump
                print("Space (jump)")
                keyboard.press(Key.space)
                time.sleep(0.6)
                keyboard.release(Key.space)

            elif res == 5: # Right jump
                print("Space + D (right jump)")
                keyboard.press(Key.space)
                with keyboard.pressed(Key.space):
                    keyboard.press('d')
                    time.sleep(0.7)
                    keyboard.release('d')
                keyboard.release(Key.space)

            elif res == 6: # Left jump
                print("Space + A (left jump)")
                keyboard.press(Key.space)
                with keyboard.pressed(Key.space):
                    keyboard.press('a')
                    time.sleep(0.7)
                    keyboard.release('d')
                keyboard.release(Key.space)

    # Activate function every 0.8 seconds
    e = threading.Event()
    while not e.wait(0.8):
        Random.init()