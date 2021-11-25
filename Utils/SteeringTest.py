import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def main():
    try:
        while(1):
            char = screen.getch()
            if char == 'w':
                print('forward')
            if char == 's':
                print('backward')
            if char == ' ':
                print('jump')
    except:
        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()

if __name__ =="__main__":
    main()