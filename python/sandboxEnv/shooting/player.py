import pygame
from setting import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):

    #初期化（元グループ、初期位置ｘ、初期位置ｙ）
    def __init__(self, groups, x, y, enemy_group):
        super().__init__(groups)

        #敵グループ
        self.enemy_group = enemy_group

        #画面取得
        self.screen = pygame.display.get_surface()

        #画像取得
        self.image_list = []
        for i in range(3):
            #tmp_image = pygame.image.load(f'assets/img/player/{i}.png')
            tmp_image = pygame.image.load(player_image_path + str(i) + image_extension)
            self.image_list.append(tmp_image)

        #画像設定
        #self.image = pygame.Surface((50,50))
        #self.image.fill(COLOR_RED)
        self.image_index = player_image_index_straight
        self.update_image()

        #自機を載せる台車
        self.rect = self.image.get_rect(center = (x,y))

        #移動方向初期化
        self.direction = pygame.math.Vector2()

        #移動速度取得
        self.speed = player_speed

        #体力
        self.health = player_health
        self.alive = True

        #効果音
        self.shot_sound = pygame.mixer.Sound(shot_se_path)
        self.shot_sound.set_volume(se_volume)

        #弾グループ設定
        self.bullet_group = pygame.sprite.Group()

        #弾発射中
        self.fire = False
        self.cooldown_timer = 0

    ##表示の更新
    def update(self):
        self.input()
        self.move()
        self.update_image()
        #print(str(self.direction) + "-" + str(self.rect))
        
        #弾描画
        self.bullet_cooldown()
        self.bullet_group.draw(self.screen)
        self.bullet_group.update()

        #体力
        self.collision_enemy()
        self.check_alive()

        #デバッグ用
        #print('b:' + str(self.bullet_group))

    #入力キー取得
    def input(self):
        key = pygame.key.get_pressed()

        #上下キー
        if key[pygame.K_UP]:
            self.direction.y = -1
        elif key[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        #左右キー
        if key[pygame.K_LEFT]:
            self.direction.x = -1
            self.image_index = player_image_index_left
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
            self.image_index = player_image_index_right
        else:
            self.direction.x = 0
            self.image_index = player_image_index_straight
        
        #zキー（弾発射）
        if key[pygame.K_z] and not self.fire:
            bullet = Bullet(self.bullet_group, self.rect.centerx, self.rect.top)
            self.fire = True
            self.shot_sound.play()
    
    #移動処理
    def move(self):
        #画面端チェック（画面端での移動速度修正）
        self.check_edge_screen()

        #移動速度の平準化
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        #X座標移動
        self.rect.x += self.direction.x * self.speed
        self.check_off_screen("x")
        #y座標移動
        self.rect.y += self.direction.y * self.speed
        self.check_off_screen("y")
    
    #画面端チェック
    #画面端でキーが押されたらそちらの方向への移動を0に
    def check_edge_screen(self):
        if self.rect.left <= 0 and self.direction.x < 0:
            self.direction.x = 0
        if self.rect.right >= screen_width and self.direction.x > 0:
            self.direction.x = 0
        if self.rect.top <= 0 and self.direction.y < 0:
            self.direction.y = 0
        if self.rect.bottom >= screen_height and self.direction.y > 0:
            self.direction.y = 0

    #画面外チェック
    #画面外に出そうな場合は座標を修正（画面端チェックだけでは微妙にはみ出すため残す）
    def check_off_screen(self, vector):
        if vector == "x":
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width
        if vector == "y":
            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
        #TODO:画面端で斜め移動しようとしたとき、x成分y成分の移動速度は斜め移動の値のままのため、遅くなっている。

    #画像の更新
    def update_image(self):
        self.pre_image = self.image_list[int(self.image_index)]
        self.image = pygame.transform.scale(self.pre_image, player_image_size)
    
    #弾クールダウン処理
    def bullet_cooldown(self):
        if self.fire:
            self.cooldown_timer += 1
        if self.cooldown_timer > bullet_cooldown_time:
            self.fire = False
            self.cooldown_timer = 0
            
    #敵との当たり判定
    def collision_enemy(self):
        for enemy in self.enemy_group:
            if self.rect.colliderect(enemy.rect) and enemy.alive:
                self.health -= enemy_power
        self.check_health()
    
    def check_health(self):
        if self.health <= 0:
            self.alive = False

    #生存確認
    def check_alive(self):
        if not self.alive:
            self.kill()
