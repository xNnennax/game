my_character=Actor(character)
my_character.pos=100,50

WIDTH=500
HEIGHT=my_character.height+20

def draw():
    screen.clear()
    screen.fill((255,255,255))
    my_character.draw()

def update():
    my_character.left=my_character.left+2
    if my_character.left > WIDTH:
         my_character.right=0
