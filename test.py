from pynput import keyboard
import time 



ctr = keyboard.Controller()
time.sleep(3)
with ctr.pressed(
        keyboard.Key.alt_l,
        keyboard.Key.f4
        ):
    pass

