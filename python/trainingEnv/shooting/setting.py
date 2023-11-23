#タイトル設定
caption_text = 'shooting game'

#FPS設定
FPS = 60

#色設定
COLOR_BLACK = (0,0,0)
COLOR_WHITE = (255,255,255)
COLOR_RED   = (255,0,0)
COLOR_GREEN = (0,255,0)
COLOR_BLUE  = (0,0,255)

#ウィンドウサイズ
screen_width = 600
screen_height = 600

##画像設定
#拡張子
image_extension = '.png'

#背景設定
bg_image_path = 'assets/img/background/bg.png'
scroll_speed = 0.5

#自機設定
player_speed = 5
player_health = 3
player_image_path = 'assets/img/player/'
player_image_size = (50,50)
player_default_pos_x = 300
player_default_pos_y = 500
#画像番号 0:正面,1:左,2:右
player_image_index_straight = 0
player_image_index_left = 1
player_image_index_right = 2

#自機弾設定
bullet_speed = 5
bullet_power = 1
bullet_image_path = 'assets/img/bullet/'
bullet_image_size = (24,48)
bullet_cooldown_time = 10
#画像番号 0:正面,1:左,2:右
bullet_image_index_0 = 0
bullet_image_index_1 = 1

#敵機設定
enemy_speed = 1
enemy_health = 3
enemy_power = 1
enemy_image_path = 'assets/img/enemy/'
enemy_image_size = (50,50)
enemy_image_index_count = 5
enemy_image_index_def = 0
enemy_animation_speed = 0.15  # アニメーションの速度（秒単位）
enemy_default_pos_x = 300
enemy_spawn_x_margin = 50
enemy_default_pos_y = 0

#敵爆発設定
explosion_image_path = 'assets/img/explosion/'
explosion_image_size = (50,50)
explosion_image_index_count = 5
explosion_image_index_def = 0
explosion_animation_speed = 0.1  # アニメーションの速度（秒単位）