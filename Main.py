import logging
import time
from pynput import keyboard
import Utils.CarControls as CarControls
from Utils.KeyboardDriving import KeyboardDriving



def main():
    # Test each motor movement
    AIn1 = 4
    AIn2 = 2
    AIn3 = 17
    AIn4 = 3

    BIn1 = 6
    BIn2 = 13
    BIn3 = 19
    BIn4 = 26

    car_motor_pins_config = [AIn1,AIn2,AIn3,AIn4,BIn1,BIn2,BIn3,BIn4]
    car_controls = CarControls.CarControls(car_motor_pins_config)
    KBDR = KeyboardDriving(car_controls)
    KBDR.keyboard_driving()

if __name__ == "__main__":
    main()