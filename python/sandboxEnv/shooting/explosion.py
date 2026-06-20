import pygame
from setting import *

class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)

        self.image_list = []
        self.load_images()
        
        self.image_index = 0
        self.animation_speed = explosion_animation_speed  # アニメーションの速度（秒単位）
        self.current_time = 0

        #最初の画像表示
        self.update_image()
        #画像を載せる台車
        self.rect = self.image.get_rect(center = (x,y))

    def load_images(self):
        # 爆発のフレーム画像を読み込む
        for i in range(explosion_image_index_count):
            #tmp_image = pygame.image.load(f'assets/img/explosion/{i}.png')
            tmp_image = pygame.image.load(explosion_image_path + str(i) + image_extension)
            self.image_list.append(tmp_image)

    def update(self):
        # アニメーションの更新
        self.animation()
        
    def animation(self):
        # アニメーションの更新
        self.current_time += 1
        if self.current_time >= self.animation_speed * FPS:
            # 次のフレームへ
            self.image_index += 1
            self.current_time = 0
            if self.image_index >= len(self.image_list):
                # 最後のフレームまで再生したらオブジェクトを削除
                self.kill()
            else:
                # 次のフレーム画像を表示
                self.update_image()

    #画像の更新
    def update_image(self):
        self.pre_image = self.image_list[int(self.image_index)]
        self.image = pygame.transform.scale(self.pre_image, explosion_image_size)