import pygame
from setting import *

class Player(pygame.sprite.Sprite):

    #初期化（元グループ、初期位置ｘ、初期位置ｙ）
    def __init__(self, groups, x, y):
        super().__init__(groups)

        #画像設定
        self.image = pygame.Surface((50,50))
        self.image.fill(COLOR_RED)

        #自機を載せる台車
        self.rect = self.image.get_rect(center = (x,y))

        #移動
        self.direction = pygame.math.Vector2()

        #移動速度取得
        self.speed = player_speed
    
    ##表示の更新
    def update(self):
        self.input()
        self.move()
        print(str(self.direction) + "-" + str(self.rect))

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
        elif key[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    #移動処理
    def move(self):
        #画面橋チェック（画面端での移動速度修正）
        self.check_edge_screen()

        #移動速度の平準化
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        #X座標移動
        self.rect.x += self.direction.x * self.speed
        #self.check_off_screen("x")
        #y座標移動
        self.rect.y += self.direction.y * self.speed
        #self.check_off_screen("y")
    

    #画面端チェック
    #画面端でキーが押されたらそちらの方向への移動をしない
    ##TODO：うまくいってない→たぶん中途半端なところにいる場合を考慮する必要あり
    def check_edge_screen(self):
        if self.rect.left == 0 and self.direction.x < 0:
            self.direction.x = 0
        if self.rect.right == screen_width and self.direction.x > 0:
            self.direction.x = 0
        if self.rect.top == 0 and self.direction.y < 0:
            self.direction.y = 0
        if self.rect.bottom == screen_height and self.direction.y > 0:
            self.direction.y = 0

    #画面外チェック
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

