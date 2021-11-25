import logging
import time
from pynput import keyboard

class KeyboardDriving:

    def __init__(self, car_controls):
        self.car_control = car_controls

    def on_press(self,key):
        try:
            if key.char == 'w':
                self.car_control.drive_forward()
            elif key.char == 's':
                self.car_control.drive_backward()
            else:
                self.car_control.stopt()
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self,key):
        print('{0} released'.format(key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def keyboard_driving(self):
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()