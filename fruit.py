import pygame
import random

class Fruit(pygame.sprite.Sprite):
    def __init__(self,scale, size_window, group):
        super().__init__(group)
        self.size_window = size_window
        self.scale = scale 
        self.color = (0,255,0)
        self.group = group
    
    def draw(self,screen):
        for fruit in self.group:
            pygame.draw.rect(screen,self.color,(fruit.rect.x  * self.scale , fruit.rect.y  * self.scale,self.scale, self.scale) )
    
    def gen_fruit(self):
        pos_x = random.randint(0, (self.size_window[0] - self.scale) / self.scale ) 
        pos_y = random.randint(0, (self.size_window[1] - self.scale) / self.scale )
        # print(pos_x,pos_y)
        self.rect = pygame.rect.Rect(pos_x ,pos_y, self.scale, self.scale)
        # print(self.rect)
        self.group.add(self)
    def eat(self,snake):
        rect_snake = pygame.rect.Rect(snake.head.x * self.scale, snake.head.y * self.scale, self.scale, self.scale)
        for fruit in self.group:
            rect_fruit = pygame.rect.Rect(fruit.rect.x * self.scale, fruit.rect.y * self.scale,self.scale,self.scale )
            if rect_fruit.colliderect(rect_snake):
                fruit.kill()
                self.gen_fruit()
                snake.add_body()
                