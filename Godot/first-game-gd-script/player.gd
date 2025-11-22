extends Area2D

signal hit

@export var speed = 400
var screen_size

func _ready():
    screen_size = get_viewport_rect().size
    hide()

func _process(delta):
    # 入力に基づいて速度を計算
    var velocity = Vector2.ZERO
    if Input.is_action_pressed("move_right"):
        velocity.x += 1
    if Input.is_action_pressed("move_left"):
        velocity.x -= 1
    if Input.is_action_pressed("move_down"):
        velocity.y += 1
    if Input.is_action_pressed("move_up"):
        velocity.y -= 1
    
    # 速度を正規化してスピードを適用
    if velocity.length() > 0:
        velocity = velocity.normalized() * speed
        $AnimatedSprite2D.play()
    else:
        $AnimatedSprite2D.stop()
    
    # プレイヤーの位置を更新
    position += velocity * delta
    position = position.clamp(Vector2.ZERO, screen_size)

    # アニメーションの向きを更新
    if velocity.x != 0:
        $AnimatedSprite2D.animation = "walk"
        $AnimatedSprite2D.flip_v = false
        $AnimatedSprite2D.flip_h = velocity.x < 0
    elif velocity.y != 0:
        $AnimatedSprite2D.animation = "up"
        $AnimatedSprite2D.flip_v = velocity.y > 0
        $AnimatedSprite2D.flip_h = false


func _on_body_entered(_body) -> void:
    hide()
    hit.emit()
    $CollisionShape2D.set_deferred("disabled", true)

func start(pos):
    position = pos
    show()
    $CollisionShape2D.disabled = false
