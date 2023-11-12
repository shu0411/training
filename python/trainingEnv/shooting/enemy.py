import pygame
import random
from setting import *

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像設定
        self.image = pygame.Surface(enemy_image_size)
        self.image.fill(COLOR_BLUE)
        
        #画像を載せる台車
        self.rect = self.image.get_rect(midbottom = (x,y))
        
        #移動方向初期化
        move_list = [-1,1]
        default_direction_x = random.choice(move_list)
        self.direction = pygame.math.Vector2(default_direction_x,1)
        self.move_timer = 0

        #移動速度取得
        self.speed = enemy_speed
    
    #更新処理
    def update(self):
        self.move()

    #動き
    def move(self):
        self.move_change()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
    #方向転換
    def move_change(self):
        self.move_timer += 1
        if self.move_timer >= 80:
            self.direction.x *= -1
            self.move_timer = 0
