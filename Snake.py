import sys
import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    stdscr.timeout(150)
    max_y, max_x = stdscr.getmaxyx()
    grow = False

    dx = 1
    dy = 0

    def render():
        for y, x in head:
            try:
                stdscr.addch(y, x, '#')
            except curses.error():
                pass

    def respawn_apple():
        while True:
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)
            if (y, x) not in head:
                return y, x

    height, width = max_y - 1, max_x - 1
    playable_area = width * height

    head = [(int(height / 2 + 1), int(width / 2 + 1)), (int(height / 2 + 1), int(width / 2)), (int(height / 2 + 1), int(width / 2 - 1))]

    class Apple:
        def __init__(self, y, x):
            self.y = y
            self.x = x
    
    appies = []

    for k in range(15):
        appies.append(
            Apple(
                random.randint(0, height - 1),
                random.randint(0, width - 1)
            )
        )

    while True:
        mov = stdscr.getch()

        if mov == ord('w'):
            dx, dy = 0, -1
        elif mov == ord('a'):
            dx, dy = -1, 0
        elif mov == ord('s'):
            dx, dy = 0, 1
        elif mov == ord('d'):
            dx, dy = 1, 0
        elif mov == ord('e'):
            sys.exit()

        new_y = head[0][0] + dy
        new_x = head[0][1] + dx

        new_head = (new_y, new_x)
        tail = head[-1]

        if (
            new_y < 0 or new_y >= height or
            new_x < 0 or new_x >= width
        ):
            stdscr.clear()
            stdscr.addstr(0, 0, 'Game Over!!')
            stdscr.refresh()
            time.sleep(1)
            sys.exit()
            
        if new_head in head[:-1]:
            stdscr.clear()
            stdscr.addstr(0, 0, 'Game Over!!')
            stdscr.refresh()
            time.sleep(1)
            sys.exit()
        
        occupied = set(head)
        free_cells = playable_area - len(occupied)
    
        if free_cells == 0:
            stdscr.clear()
            stdscr.addstr(0, 0, 'You win!!')
            stdscr.refresh()
            time.sleep(1)
            sys.exit()
        
        for apple in appies:
            if (new_y, new_x) == (apple.y, apple.x):
                grow = True
                apple.y, apple.x = respawn_apple()
                break
            

        head.insert(0, (new_y, new_x))

        if not grow:
            head.pop()
        else:
            grow = False
        
        stdscr.clear()

        for apple in appies:
            try:
                stdscr.addch(apple.y, apple.x, 'o')
            except curses.error:
                pass
                
        render()
        
        stdscr.refresh()
curses.wrapper(main)
