import pygame

#初期化
pygame.init()

##関数定義 開始####################
def draw_grid():
    one_third_width = screen_width / 3
    one_third_height = screen_height / 3
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0, one_third_height * i), (screen_width, one_third_height * i), 3)
        pygame.draw.line(screen, BLACK, (one_third_width * i, 0), (one_third_width * i, screen_height), 3)
##関数定義 終了####################

#ウィンドウ作成
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("○×ゲーム")

#色定数
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#ボード定義(0:空白、1:○、-1:×)
board =  [
    [1, 0, 0],
    [0,-1, 0],
    [0, 0, 1]
]
print(board)
for row in board:
    for col in row:
        print(col)


#画面処理メインループ開始######################
run = True
while run:
    
    #背景設定
    screen.fill(WHITE)

    #線を描く
    draw_grid()

    #イベント取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    #更新
    pygame.display.update()

#画面処理メインループ終了######################

pygame.quit()

