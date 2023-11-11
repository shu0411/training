import pygame
from setting import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像設定
        self.image = pygame.Surface(bullet_image_size)
        self.image.fill(COLOR_GREEN)
        
        #画像を載せる台車
        self.rect = self.image.get_rect(midbottom = (x,y))
        
        #移動速度取得
        self.speed = bullet_speed

    def move(self):
        self.rect.y -= self.speed
    
    def update(self):
        self.move()