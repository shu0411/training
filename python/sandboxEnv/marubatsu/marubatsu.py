import pygame
import copy

#初期化
pygame.init()

##関数定義 開始####################
def draw_grid():
    for i in range(1,3):
        pygame.draw.line(screen, BLACK, (0, row_height * i), (screen_width, row_height * i), line_width)
        pygame.draw.line(screen, BLACK, (col_width * i, 0), (col_width * i, screen_height), line_width)

def draw_board():
    for row_index, row in enumerate(board):
        #print(row_index,row)
        for col_index, col in enumerate(row):
            #print(row_index,col_index,col)
            pos_x = col_width * col_index + col_width / 2       #図形中心のx座標=列幅*列id+列幅/2
            pos_y = row_height * row_index + row_height / 2     #図形中心のy座標=行高さ*行id+行幅/2
            if col == 1:
                #print(row_index,col_index,col,'○')
                pygame.draw.circle(screen, RED, (pos_x,pos_y), mark_size / 2, mark_line_width)
            elif col == -1:
                #print(row_index,col_index,col,'×')
                #pygame.draw.circle(screen, BLUE, (pos_x,pos_y), mark_size / 2, mark_line_width)
                pos_x_left = col_width * col_index + col_width / 2 - mark_size / 2
                pos_x_right = col_width * col_index + col_width / 2 + mark_size / 2
                pos_y_upper = row_height * row_index + row_height / 2 - mark_size / 2
                pos_y_lower = row_height * row_index + row_height / 2 + mark_size / 2
                pygame.draw.line(screen, BLUE, (pos_x_left, pos_y_upper), (pos_x_right, pos_y_lower), mark_line_width)
                pygame.draw.line(screen, BLUE, (pos_x_left, pos_y_lower), (pos_x_right, pos_y_upper), mark_line_width)
            #else:
                #print(row_index,col_index,col,'-')

def check_winner():
    winner = None
    for index in range(3):
        #横
        if sum(board[index]) == 3:
            winner = 'o'
        if sum(board[index]) == -3:
            winner = 'x'
        #縦
        if board[0][index] + board[1][index] + board[2][index] == 3:
            winner = 'o'
        if board[0][index] + board[1][index] + board[2][index] == -3:
            winner = 'x'
    #斜め
    if board[0][0] + board[1][1] + board[2][2] == 3 or  board[0][2] + board[1][1] + board[2][0] == 3:
            winner = 'o'
    if board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
            winner = 'x'
    
    if winner != None:
        text = 'Winner : ' + winner
        text_image = font.render(text, True, BLACK, GREEN)
        screen.blit(text_image,(100,200))
        text = 'Click to Reset'
        text_image = font.render(text, True, BLACK, GREEN)
        screen.blit(text_image,(100,400))
        return True
    
    return False
##関数定義 終了####################

#変数、初期値
screen_width = 600      #ウィンドウ幅
screen_height = 600     #ウィンドウ高さ
col_width = screen_width / 3    #列幅
row_height = screen_height / 3  #行高さ

line_width = 3          #線の幅
mark_size = 160         #図形サイズ
mark_line_width = 5     #図形の線の幅

#フォント
font = pygame.font.SysFont(None, 100)

#ウィンドウ作成
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("○×ゲーム")

#色定数
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#ボード定義(0:空白、1:○、-1:×)
val_o = 1
val_x = val_o * -1
val_n = 0
default_board =  [
    [val_n, val_n, val_n],
    [val_n, val_n, val_n],
    [val_n, val_n, val_n]
]
board = copy.deepcopy(default_board)
turn = val_o
game_over = False

#画面処理メインループ開始######################
run = True
while run:
    
    ###画面描画###
    #背景設定
    screen.fill(WHITE)
    #枠線描画
    draw_grid()
    #ボード描画
    draw_board()

    ###勝利確認###
    game_over = check_winner()
    
    #マウス位置取得
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    mouse_pos_cell_x = mouse_pos_x // 200
    mouse_pos_cell_y = mouse_pos_y // 200

    #イベント取得
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(mouse_pos_cell_x, mouse_pos_cell_y)
            if game_over:
                board = copy.deepcopy(default_board)
                game_over = False
                turn = val_o
            #if board[mouse_pos_cell_y][mouse_pos_cell_x] == 0 and not game_over:
            elif board[mouse_pos_cell_y][mouse_pos_cell_x] == 0:
                board[mouse_pos_cell_y][mouse_pos_cell_x] = turn
                turn *= -1
    
    #更新
    pygame.display.update()

#画面処理メインループ終了######################

pygame.quit()

#今後の改善案
#優先度高：引き分けになった場合のリセット
#優先度中：ヘッダ部分の表示：ターン表示
#優先度中：リセットボタン：ボタンの追加について調べる。
#優先度低：時間制