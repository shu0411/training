import pygame
import os
import random
from setting import *
from player import Player
from enemy import Enemy

#ゲーム画面のクラス
class Game:
    #ゲーム画面初期化
    def __init__(self):
        #カレントディレクトリ変更
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        self.screen = pygame.display.get_surface()

        #グループ作成
        self.create_group()

        #自機生成
        player = Player(self.player_group, player_default_pos_x, player_default_pos_y)

        #敵機生成タイマー初期化
        self.enemy_timer = 0

        #背景
        self.bg_img = pygame.transform.scale(pygame.image.load(bg_image_path),(screen_width,screen_height))
        self.bg_y = 0
    
    #グループ作成
    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
    
    #背景スクロール
    def scroll_bg(self):
        self.bg_y = (self.bg_y + scroll_speed) % screen_height
        self.screen.blit(self.bg_img,(0,self.bg_y - screen_height))
        self.screen.blit(self.bg_img,(0,self.bg_y))
    
    #ゲーム実行中
    def run(self):
        self.scroll_bg()

        #自機グループの描画と更新
        self.player_group.draw(self.screen)
        self.player_group.update()
        
        #敵機グループの描画と更新
        self.create_enemy()
        self.enemy_group.draw(self.screen)
        self.enemy_group.update()
        
    #敵生成
    def create_enemy(self):
        #TODO:初期位置変更処理から　#4 8:53

        self.enemy_timer += 1
        if self.enemy_timer >= 50:
            enemy = Enemy(self.enemy_group, enemy_default_pos_x, enemy_default_pos_y)
            self.enemy_timer = 0