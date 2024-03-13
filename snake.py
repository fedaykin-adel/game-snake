import pygame 
import math

class Snake():
    def __init__(self,  scale, size_window):
        self.scale = scale
        self.size_window = size_window
        self.pos = ((size_window[0] / scale) // 2, (size_window[1] / scale) // 2)
        self.head = pygame.rect.Rect(self.pos[0] ,self.pos[1] ,scale,scale)
        self.color_head = (125,15,125)
        self.color_body = (255,75,255)
        self.direction = 'UP'
        self.move_count = 0
        self.delay_move = 10
        self.body = []
        
        self.done = False
    def reset(self):
        if self.done:
            self.body = []
            self.head = pygame.rect.Rect(self.pos[0],self.pos[1],self.scale, self.scale)
            self.move_count = 0
            self.direction = 'UP'
            self.done = False
    def draw(self,screen):
        
        pygame.draw.rect(screen,self.color_head, (self.head.x  * self.scale ,self.head.y * self.scale ,self.scale,self.scale) )
        for section in self.body:
            pygame.draw.rect(screen,self.color_body, (section.x * self.scale ,section.y * self.scale ,self.scale,self.scale) )
            
    def change_direction(self,new_direction):
        if new_direction == 'UP' and self.direction != 'DOWN' :
            self.direction = new_direction
        if new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = new_direction
        if new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = new_direction
        if new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = new_direction
    def add_body(self):
        if not self.body:
            pos_x, pos_y = self.new_pos(self.head.x, self.head.y)
            
        else:
            pos_x = self.body[-1].x
            pos_y = self.body[-1].y
        self.body.append(pygame.rect.Rect(pos_x, pos_y, self.scale, self.scale))
           
    def move(self):
        if self.direction == 'UP':
            self.head.y -= 1
        if self.direction == 'DOWN':
            self.head.y += 1
        if self.direction == 'RIGHT':
            self.head.x += 1
        if self.direction == 'LEFT':
            self.head.x -= 1
    def collision_himself(self):
        for body in self.body[0 :]:
            distance = math.sqrt(math.pow(self.head.x  - body.x , 2) + math.pow(self.head.y  - body.y , 2))
            if distance < 1:
               self.done = True
    def new_pos(self,pos_x,pos_y):
        if self.direction == 'UP':
            pos_y += 1
        if self.direction == 'DOWN':
            pos_y -= 1
        if self.direction == 'LEFT':
            pos_x += 1
        if self.direction == 'RIGHT':
            pos_x -= 1
        return pos_x, pos_y 
    def move_body(self):
        for i in range(len(self.body)-1, -1, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
         
        self.body[0].x, self.body[0].y = self.new_pos(self.head.x, self.head.y)
    def collision_wall(self):
        if self.head.x < 0 or self.head.x > (self.size_window[0] - self.scale) / self.scale:
            self.done = True    
        if self.head.y < 0 or self.head.y > (self.size_window[1] - self.scale) / self.scale:
            self.done = True
           
    def update(self):
        self.collision_himself()
        self.collision_wall()
        if self.move_count == self.delay_move:
            self.move()
            if self.body:
                self.move_body()
            self.move_count = 0
        else:
            self.move_count += 1
    
    def control(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.change_direction('UP')
        if key[pygame.K_s]:
            self.change_direction('DOWN')
        if key[pygame.K_d]:
            self.change_direction('RIGHT')
        if key[pygame.K_a]:
            self.change_direction('LEFT')