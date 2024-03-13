import pygame
from snake import Snake
from fruit import Fruit
from world import World
pygame.init()
size_window = (600,600)





screen = pygame.display.set_mode(size_window)
run = True
scale = 20

group_fruit = pygame.sprite.Group()
fruit = Fruit(scale, size_window,group_fruit)
fruit.gen_fruit()

#control draw square
draw_square = False

snake = Snake(scale,size_window)


world = World(size_window,scale)

while run:
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    snake.control()
    #collision fruit here
    
    #update snake
    snake.update()
    #when snake eat fruit
    fruit.eat(snake)
    if draw_square:
        world.draw(screen)
    fruit.draw(screen)
    snake.draw(screen)
    
    #game reset
    snake.reset()
    
    #game flip
    pygame.display.flip()
    #game tick fps
    pygame.time.Clock().tick(60)       
pygame.quit()