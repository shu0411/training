import pygame
from setting import *
from game import Game

pygame.mixer.init()
pygame.init()

#ウィンドウ作成
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(caption_text)

#FPS設定
clock = pygame.time.Clock()

#ゲームクラスインスタンス化
game = Game()

#メインループ開始##############################
run = True
while run:
    #背景の塗りつぶし
    screen.fill(COLOR_BLACK)
            
    #ゲーム実行
    game.run()

    #イベントの取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #×閉じで処理終了
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #Escキーで処理終了
                run = False

    #更新
    pygame.display.update()

    #FPS設定
    clock.tick(FPS)

#メインループ終了##############################

pygame.quit()