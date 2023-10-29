import pygame
from setting import *

class Player(pygame.sprite.Sprite):

    #初期化（元グループ、初期位置ｘ、初期位置ｙ）
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像設定
        self.image = pygame.Surface((50,50))
        self.image.fill(COLOR_RED)

        #載せる台車
        self.rect = self.image.get_rect(center = (x,y))

        #移動
        self.direction = pygame.math.Vector2()
        self.speed = player_speed
    
    def input(self):
        key = pygame.key.get_pressed()

        #上下移動
        if key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        #左右移動
        if key[pygame.K_LEFT]:
            self.direction.x = -1
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def update(self):
        pass