import pygame
import os
from setting import *
from player import Player

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
        player = Player(self.player_group, 300, 500)

        #背景
        self.bg_img = pygame.transform.scale(pygame.image.load(bg_img_path),(screen_width,screen_height))
        self.bg_y = 0
    
    #グループ作成
    def create_group(self):
        self.player_group = pygame.sprite.GroupSingle()
    
    #背景スクロール
    def scroll_bg(self):
        self.bg_y = (self.bg_y + scroll_speed) % screen_height
        self.screen.blit(self.bg_img,(0,self.bg_y - screen_height))
        self.screen.blit(self.bg_img,(0,self.bg_y))
    
    #ゲーム実行中
    def run(self):
        self.scroll_bg()

        #グループの描画と更新
        self.player_group.draw(self.screen)
        self.player_group.update()