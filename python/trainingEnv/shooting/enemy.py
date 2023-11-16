import pygame
import random
from setting import *

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像取得
        self.image_list = []
        for i in range(2):
            #tmp_image = pygame.image.load(f'assets/img/enemy/{i}.png')
            tmp_image = pygame.image.load(enemy_image_path + str(i) + image_extension)
            self.image_list.append(tmp_image)

        #画像設定
        #self.image = pygame.Surface(enemy_image_size)
        #self.image.fill(COLOR_BLUE)
        self.image_index = enemy_image_index_0
        self.update_image()
        
        
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
        self.check_off_screen()
        self.animation()

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

    #画面外に出た敵は削除
    def check_off_screen(self):
        if self.rect.top > screen_height:
            self.kill()
    
    #アニメーション
    def animation(self):
        self.image_index += 0.15
        if self.image_index >= len(self.image_list):
            self.image_index = 0
        self.update_image()
            
    #画像の更新
    def update_image(self):
        self.pre_image = self.image_list[int(self.image_index)]
        self.image = pygame.transform.scale(self.pre_image, enemy_image_size)