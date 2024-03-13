import pygame

class World():
    def __init__(self,size_window,scale):
        self.size_window = size_window
        self.scale = scale
    def draw(self,screen):
        for i in range(int(self.size_window[0] / self.scale)):
            for j in range(int(self.size_window[1]/ self.scale)):
                pygame.draw.line(screen,(255,255,255), (0,i * self.scale),( self.size_window[0],i * self.scale))
                pygame.draw.line(screen, (255,255,255), (j * self.scale, 0), (j*self.scale, self.size_window[1]))
    
