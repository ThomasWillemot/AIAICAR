import curses
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def main():

    char = screen.getch()

    if char == 'w':
        print('forward')
    if char == 's':
        print('backward')
    if char == ' ':
        print('jump')


if __name__ =="__main__":
    main()