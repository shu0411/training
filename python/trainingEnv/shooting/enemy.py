import pygame
import random
from setting import *
from explosion import Explosion

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, groups, x, y, bullet_group):
        super().__init__(groups)

        self.screen = pygame.display.get_surface()
        
        #グループ
        self.bullet_group = bullet_group
        self.explosion_group = pygame.sprite.Group()

        #画像取得
        self.image_list = []
        for i in range(enemy_image_index_count):
            #tmp_image = pygame.image.load(f'assets/img/enemy/{i}.png')
            tmp_image = pygame.image.load(enemy_image_path + str(i) + image_extension)
            self.image_list.append(tmp_image)

        #画像設定
        #self.image = pygame.Surface(enemy_image_size)
        #self.image.fill(COLOR_BLUE)
        self.image_index = enemy_image_index_def
        self.animation_speed = enemy_animation_speed  # アニメーションの速度（秒単位）
        self.current_time = 0

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

        #体力取得
        self.health = enemy_health
        self.alive = True

        #爆発
        self.explosion_flg = False

    #更新処理
    def update(self):
        self.move()
        self.check_off_screen()
        self.animation()
        self.collision_bullet()
        self.check_alive()

        self.explosion_group.update()
        self.explosion_group.draw(self.screen)

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
        if self.alive:
            self.current_time += 1
            if self.current_time >= self.animation_speed * FPS:
                # 次のフレームへ
                self.image_index += 1
                self.current_time = 0
            if self.image_index >= len(self.image_list):
                self.image_index = 0
            self.update_image()
        else:
            self.image.set_alpha(0)
            
    #画像の更新
    def update_image(self):
        self.pre_image = self.image_list[int(self.image_index)]
        self.image = pygame.transform.scale(self.pre_image, enemy_image_size)
    
    #弾との当たり判定
    def collision_bullet(self):
        for bullet in self.bullet_group:
            #弾が自身に当たったら、弾を消して体力を減らす
            if self.rect.colliderect(bullet.rect):
                bullet.kill()
                self.health -= bullet_power
        self.check_health()

    def check_health(self):
        if self.health <= 0:
            self.alive = False

    #生存確認
    def check_alive(self):
        if not self.alive and not self.explosion_flg:
            self.speed = 0
            explosion = Explosion(self.explosion_group, self.rect.centerx, self.rect.centery)
            self.explosion_flg = True
        if self.explosion_flg and len(self.explosion_group) == 0:
            self.kill()
