import logging
import time

from pynput import keyboard
import Utils.CarControls as CarControls



def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
def keyboard_driving():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()



def main():
    # Test each motor movement
    car_motor_pins_config = [0,0,0,0,0,0,0,0]
    car_controls = CarControls.CarControls(car_motor_pins_config)

    car_controls.drive_forward()
    print("Forward")
    time.sleep(5)
    print("Backward")
    car_controls.drive_backward()
    time.sleep(5)
    print("Stop")
    car_controls.stop()


if __name__ == "__main__":
    main()