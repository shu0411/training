import pygame
from setting import *

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像取得
        self.image_list = []
        for i in range(2):
            #tmp_image = pygame.image.load(f'assets/img/bullet/{i}.png')
            tmp_image = pygame.image.load(bullet_image_path + str(i) + image_extension)
            self.image_list.append(tmp_image)

        #画像設定
        #self.image = pygame.Surface(bullet_image_size)
        #self.image.fill(COLOR_GREEN)
        self.image_index = bullet_image_index_0
        self.update_image()
        
        #画像を載せる台車
        self.rect = self.image.get_rect(midbottom = (x,y))
        
        #移動速度取得
        self.speed = bullet_speed
    
    def update(self):
        self.move()
        self.check_off_screen()
        self.animation()

    #移動処理
    def move(self):
        self.rect.y -= self.speed

    #画面外に出た弾は削除
    def check_off_screen(self):
        if self.rect.bottom < 0:
            self.kill()
    
    #アニメーション
    def animation(self):
        self.image_index += 0.05
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        self.update_image()

    #画像の更新
    #TODO：共通化したい
    def update_image(self):
        self.pre_image = self.image_list[int(self.image_index)]
        self.image = pygame.transform.scale(self.pre_image, bullet_image_size)
    