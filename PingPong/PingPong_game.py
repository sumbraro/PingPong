import pygame
from pygame import *

pygame.init()
mixer.init()
font.init()

font1 = font.SysFont('Arial', 50)

FPS = 90
clock = time.Clock()

speed_x = 3
speed_y = 3

window = display.set_mode((700, 500))
display.set_caption('Левое яйцо прадеда')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
    def move_platform1(self):
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

    def move_platform2(self):
        if keys[K_LEFT] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < 400:
            self.rect.y += self.speed


background = GameSprite('background.jpg', 0, 0, 700, 500, 0)
platform1 = GameSprite('racket.png', 0, 150, 17, 100, 6)
platform2 = GameSprite('racket.png', 683, 150, 17, 100, 6)
ball = GameSprite('ball1.png', 325, 225, 40, 40, 3)

finish = False
game = True


while game:
    keys = key.get_pressed()

    score1 = font1.render(
        'score:', 1, (255, 255, 255)
    )
    
    window.blit(score1, (10, 10))

    for e in event.get():
            if e.type == QUIT:
                game = False

    if finish == False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
        speed_x *= -1
        speed_y *= -1

    if ball.rect.y <= 0 or ball.rect.y >= 450:
        speed_y *= -1


    background.reset()
    platform1.reset()
    platform2.reset()
    ball.reset()

    platform1.move_platform1()
    platform2.move_platform2()

    clock.tick(FPS)
    display.update()