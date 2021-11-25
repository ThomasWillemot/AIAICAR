import curses
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
                screen.addstr(2,20,"FW")
            if char == ord('s'):
                screen.addstr(2,20,"BW")
            if char == ord(' '):
                screen.addstr(2,20,"Up")
    except:
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ =="__main__":
    main()