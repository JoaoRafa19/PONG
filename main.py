from classes import *
import pygame, sys

pygame.init()

size = width,heigh = 700, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")

player1 = Player(heigh)
player2 = Player(heigh)
player1.rect.top = 50
player1.rect.left = 0
player2.rect.top = 50
player2.rect.right = width
clock = pygame.time.Clock()
ball = Ball()
split = pygame.image.load("split.png")
split_ = split.get_rect()
split_.left = (width/2)-5
split_.top = 0

def draw():
    screen.fill([127,127,127])
    #draw players
    screen.blit(player1.player, player1.rect)
    screen.blit(player2.player, player2.rect)   
    screen.blit(split, split_)
    #draw ball
    screen.blit(score, (275, 10))
    screen.blit(ball.ball, ball.rect)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
          
    pressed_keys = pygame.key.get_pressed()
    
    
    #player2 moves
    if pressed_keys[pygame.K_UP]:
        player2.moveUp()
    if pressed_keys[pygame.K_DOWN]:
        player2.moveDown()
        
    #player1 moves
    if pressed_keys[pygame.K_w]:
        player1.moveUp()
    if pressed_keys[pygame.K_s]:
        player1.moveDown()  
        
    #ball moves
    ball.move()
    
    #scores
    
    if ball.rect.left == 0:
        player2.score += 1
        ball.rect.left = 350
        ball.rect.top = 200
        ball.speed_x = ball.speed_x*-1
    elif ball.rect.right == 700:
        player1.score += 1
        ball.rect.left = 350
        ball.rect.top = 200
        ball.speed_x = ball.speed_x*-1
        
    myfont = pygame.font.SysFont("monospace", 15)
    #render text
    score = myfont.render("P1 = {} || P2 = {}".format(player1.score, player2.score), 1, (255,255,255))
    
    #collisions
    if pygame.Rect.colliderect(ball.rect, player1.rect) or pygame.Rect.colliderect(ball.rect, player2.rect):
        ball.speed_x = ball.speed_x * -1
    
    draw()
    clock.tick(280)
    pygame.display.update()