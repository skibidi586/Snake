import sys
import curses

def main(stdscr):
    stdscr.clear()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.timeout(150)
    max_y, max_x = stdscr.getmaxyx()

    dx = 0
    dy = 0

    def render():
        for y, x in head:
            stdscr.addch(y, x, '#')
        stdscr.refresh()

    stdscr.addstr(0, 0, 'snake by chuh and ric')
    stdscr.refresh()

    stdscr.nodelay(False)

    curses.echo()

    stdscr.addstr(1, 0, 'How wide do you want the map to be?')
    stdscr.refresh()
    width = int(stdscr.getstr().decode())

    stdscr.refresh()

    stdscr.addstr(2, 0, 'How tall do you want the map to be?')
    stdscr.refresh()
    height = int(stdscr.getstr().decode())

    curses.noecho()

    head = [(int(height / 2 + 1), int(width / 2 + 1)), (int(height / 2 + 1), int(width / 2)), (int(height / 2 + 1), int(width / 2 - 1))]

    stdscr.nodelay(True)

    for i in range(height):
        for j in range(width):
            stdscr.addch(i, j, '.')
    stdscr.refresh()

    render()
    stdscr.refresh()

    while True:
        stdscr.addstr(height + 1, 0, 'Which direction would you like to move? (WASD)')
        mov = stdscr.getch()

        if mov == ord('w'):
            stdscr.addch(head[0][0], head[0][1], '.')
            dx, dy = 0, -1
        elif mov == ord('a'):
            stdscr.addch(head[0][0], head[0][1], '.')
            dx, dy = -1, 0
        elif mov == ord('s'):
            stdscr.addch(head[0][0], head[0][1], '.')
            dx, dy = 0, +1
        elif mov == ord('d'):
            stdscr.addch(head[0][0], head[0][1],  '.')
            dx, dy = +1, 0
        elif mov == ord('e'):
            sys.exit()

        new_head = (head[0][0] + dy, head[0][1] + dx)

        if new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
            stdscr.addstr(max_y - 1, 0, 'Game Over!! (Press any key)')
            stdscr.refresh()
            stdscr.getch()
            sys.exit()

        head.insert(0, new_head)
        head.pop()
        
        render()
curses.wrapper(main)
