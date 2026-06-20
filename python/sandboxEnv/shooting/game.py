import pygame
import os
import random
from setting import *
from support import draw_text
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
        self.player = Player(self.player_group, player_default_pos_x, player_default_pos_y,self.enemy_group)
        self.game_over = False

        #敵機生成タイマー初期化
        self.enemy_timer = 0

        #背景
        self.bg_img = pygame.transform.scale(pygame.image.load(bg_image_path),(screen_width,screen_height))
        self.bg_y = 0

        #BGM
        pygame.mixer.music.load(bgm_path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(bgm_volume)
    
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
        
        #ゲームオーバー処理
        self.check_game_over()
        self.reset()
        
        #デバッグ用
        print('e:' + str(self.enemy_group))
        
    #敵生成
    def create_enemy(self):
        #初期座標をランダムに
        enemy_start_pos_x = random.randint(enemy_spawn_x_margin, screen_width - enemy_spawn_x_margin )
        enemy_start_pos_y = enemy_default_pos_y

        self.enemy_timer += 1
        if self.enemy_timer >= 50:
            enemy = Enemy(self.enemy_group, enemy_start_pos_x, enemy_start_pos_y, self.player.bullet_group)
            self.enemy_timer = 0
    
    def check_game_over(self):
        if len(self.player_group) == 0:
            self.game_over = True
            draw_text(self.screen, "GAME OVER", screen_width//2, screen_height//2, 75, COLOR_RED)
            draw_text(self.screen, "Press SPACE KEY To Reset", screen_width//2, screen_height//2 + 100, 50, COLOR_GREEN)

    def reset(self):
        key = pygame.key.get_pressed()
        if self.game_over and key[pygame.K_SPACE]:
            self.player = Player(self.player_group, player_default_pos_x, player_default_pos_y,self.enemy_group)
            self.enemy_group.empty()
            self.game_over = False