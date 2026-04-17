class Player:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

print('snake by chuh and ric')

print('How wide do you want the map to be?')
width = int(input())

print('How tall do you want the map to be?')
height = int(input())

play = Player(width / 2 + 1, height / 2 + 1)

for i in range(height):
    for j in range(width):
            if j < width - 1:
                print('.', end='')
            else:
                print('.')
