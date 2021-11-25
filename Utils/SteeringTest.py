import curses
import CarControls as CarControls

screen = curses.initscr()
#curses.noecho()
curses.cbreak()
screen.keypad(True)

def main():
    try:
        while(1):
            char = screen.getch()
            screen.addch(20,2,char)
            screen.refresh()
            if char == ord('w'):
                car_controls.drive_forward()
                screen.addstr(2,20,"FW")
            if char == ord('s'):
                car_controls.drive_backward()
                screen.addstr(2,20,"BW")
            if char == ord('q'):
                car_controls.rotate_left()
                screen.addstr(2,20,"RL")
            if char == ord('e'):
                car_controls.rotate_right()
                screen.addstr(2, 20, "RR")
            if char == ord(' '):
                car_controls.stop()
                screen.addstr(2,20,"Up")
            if char == ord('0'):
                car_controls.motor_0()
                screen.addstr(2,20,"0")
            if char == ord('1'):
                car_controls.motor_1()
                screen.addstr(2,20,"1")
            if char == ord('2'):
                car_controls.motor_2()
                screen.addstr(2,20,"2")
            if char == ord('3'):
                car_controls.motor_3()
                screen.addstr(2,20,"3")
            if char == ord('4'):
                car_controls.motor_4()
                screen.addstr(2,20,"4")
            if char == ord('5'):
                car_controls.motor_5()
                screen.addstr(2,20,"5")
            if char == ord('6'):
                car_controls.motor_6()
                screen.addstr(2,20,"6")
            if char == ord('7'):
                car_controls.motor_7()
                screen.addstr(2,20,"7")
    except:
        car_controls.stop()
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ =="__main__":
    AIn1 = 4
    AIn2 = 2
    AIn3 = 17
    AIn4 = 3

    BIn1 = 6
    BIn2 = 13
    BIn3 = 19
    BIn4 = 26

    car_motor_pins_config = [AIn1, AIn2, AIn3, AIn4, BIn1, BIn2, BIn3, BIn4]
    car_controls = CarControls.CarControls(car_motor_pins_config)
    main()