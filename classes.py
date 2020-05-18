import pygame

class Player:
    def __init__(self, heigh):
        self.player = pygame.image.load("player.png")
        self.rect = self.player.get_rect()
        self.score = 0
        self.y_speed = 2
    def moveUp(self):
        if self.rect.top == 0:
            self.rect.top = 0
            return
        self.rect.top -= self.y_speed
    
    def moveDown(self):
    
        if self.rect.bottom == 400:
            self.rect.bottom = 400
            return
        self.rect.top += self.y_speed
    
        
class Ball:
    
    def __init__(self):
        
        self.ball = pygame.image.load("ball.png")
        self.rect = self.ball.get_rect()
        self.rect.left = 348
        self.rect.top = 190
        self.speed_y = 1
        self.speed_x = 1
        
    def move(self):
        if self.rect.left == 0:
            self.speed_x = 1
        elif self.rect.right == 700:
            self.speed_x = -1
        elif self.rect.bottom == 400:
            self.speed_y = -1
        elif self.rect.top == 0:
            self.speed_y = 1
            
        self.rect.left += self.speed_x
        self.rect.top += self.speed_y
        
        
        