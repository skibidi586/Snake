import sys

class Player:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def render():
    for i in range(height):
        for j in range(width):
            if i == play.y and j == play.x and j < width - 1:
                print('#', end='')
            elif i == play.y and j == play.x:
                print('#')
            elif j < width - 1:
                print('.', end='')
            else:
                print('.')

print('snake by chuh and ric')

print('How wide do you want the map to be?')
width = int(input())

print('How tall do you want the map to be?')
height = int(input())

play = Player(int(width / 2), int(height / 2))

render()

while True:
    print('Which direction would you like to move? (WASD)')
    mov = input().lower()

    if mov == 'w':
        play.y -= 1
    elif mov == 'a':
        play.x -= 1
    elif mov == 's':
        play.y += 1
    elif mov == 'd':
        play.x += 1
    elif mov == 'exit' or mov == 'e':
        sys.exit()
    else:
        print('[ERROR]: Not a move!')
    
    if play.x >= width:
        play.x = width - 1
    
    if play.x <= 0:
        play.x = 0
    
    if play.y >= height:
        play.y = height - 1
    
    if play.y <= 0:
        play.y = 0

    render()

