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
                car_controls.drive_backward()
                screen.addstr(2,20,"RL")
            if char == ord('e'):
                car_controls.drive_backward()
                screen.addstr(2, 20, "RR")
            if char == ord(' '):
                car_controls.stop()
                screen.addstr(2,20,"Up")
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