const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreEl = document.getElementById("score");
const livesEl = document.getElementById("lives");
const overlay = document.getElementById("overlay");
const statusText = document.getElementById("statusText");

const WIDTH = canvas.width;
const HEIGHT = canvas.height;
const PADDLE_WIDTH = 118;
const PADDLE_HEIGHT = 16;
const BALL_RADIUS = 9;
const START_LIVES = 3;

const brickConfig = {
  rows: 5,
  cols: 9,
  width: 72,
  height: 24,
  gap: 10,
  top: 78,
  left: 31,
};

const colors = ["#42d1a4", "#ffcc5c", "#5ab0ff", "#ff7a90", "#b18cff"];

let score = 0;
let lives = START_LIVES;
let state = "ready";
let animationId = null;
let keys = new Set();
let bricks = [];
let paddle;
let ball;

function createBricks() {
  bricks = [];

  for (let row = 0; row < brickConfig.rows; row += 1) {
    for (let col = 0; col < brickConfig.cols; col += 1) {
      bricks.push({
        x: brickConfig.left + col * (brickConfig.width + brickConfig.gap),
        y: brickConfig.top + row * (brickConfig.height + brickConfig.gap),
        width: brickConfig.width,
        height: brickConfig.height,
        color: colors[row % colors.length],
        active: true,
      });
    }
  }
}

function resetPositions() {
  paddle = {
    x: (WIDTH - PADDLE_WIDTH) / 2,
    y: HEIGHT - 44,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT,
    speed: 8,
  };

  ball = {
    x: WIDTH / 2,
    y: paddle.y - BALL_RADIUS - 1,
    dx: 4.1,
    dy: -5.2,
    radius: BALL_RADIUS,
  };
}

function resetGame() {
  score = 0;
  lives = START_LIVES;
  state = "ready";
  createBricks();
  resetPositions();
  updateHud();
  showMessage("Press Space or Click to Start");
  draw();
}

function updateHud() {
  scoreEl.textContent = score.toString();
  livesEl.textContent = lives.toString();
}

function showMessage(message) {
  statusText.textContent = message;
  overlay.classList.remove("hidden");
}

function hideMessage() {
  overlay.classList.add("hidden");
}

function startGame() {
  if (state === "playing") {
    return;
  }

  if (state === "won" || state === "lost") {
    resetGame();
  }

  state = "playing";
  hideMessage();
  runLoop();
}

function runLoop() {
  if (animationId !== null) {
    cancelAnimationFrame(animationId);
  }

  animationId = requestAnimationFrame(loop);
}

function loop() {
  update();
  draw();

  if (state === "playing") {
    animationId = requestAnimationFrame(loop);
  }
}

function update() {
  if (state !== "playing") {
    return;
  }

  movePaddleByKeys();
  ball.x += ball.dx;
  ball.y += ball.dy;

  collideWithWalls();
  collideWithPaddle();
  collideWithBricks();
  checkMiss();
}

function movePaddleByKeys() {
  if (keys.has("ArrowLeft") || keys.has("KeyA")) {
    paddle.x -= paddle.speed;
  }

  if (keys.has("ArrowRight") || keys.has("KeyD")) {
    paddle.x += paddle.speed;
  }

  clampPaddle();
}

function clampPaddle() {
  paddle.x = Math.max(0, Math.min(WIDTH - paddle.width, paddle.x));
}

function collideWithWalls() {
  if (ball.x - ball.radius <= 0) {
    ball.x = ball.radius;
    ball.dx *= -1;
  }

  if (ball.x + ball.radius >= WIDTH) {
    ball.x = WIDTH - ball.radius;
    ball.dx *= -1;
  }

  if (ball.y - ball.radius <= 0) {
    ball.y = ball.radius;
    ball.dy *= -1;
  }
}

function collideWithPaddle() {
  const isFalling = ball.dy > 0;
  const hitsPaddle =
    ball.x + ball.radius >= paddle.x &&
    ball.x - ball.radius <= paddle.x + paddle.width &&
    ball.y + ball.radius >= paddle.y &&
    ball.y - ball.radius <= paddle.y + paddle.height;

  if (!isFalling || !hitsPaddle) {
    return;
  }

  const hitPosition = (ball.x - (paddle.x + paddle.width / 2)) / (paddle.width / 2);
  ball.x = Math.max(paddle.x + ball.radius, Math.min(paddle.x + paddle.width - ball.radius, ball.x));
  ball.y = paddle.y - ball.radius;
  ball.dx = hitPosition * 6.2;
  ball.dy = -Math.max(4.7, Math.abs(ball.dy) * 1.02);
}

function collideWithBricks() {
  for (const brick of bricks) {
    if (!brick.active || !circleRectOverlap(ball, brick)) {
      continue;
    }

    brick.active = false;
    score += 10;
    updateHud();

    const overlapLeft = ball.x + ball.radius - brick.x;
    const overlapRight = brick.x + brick.width - (ball.x - ball.radius);
    const overlapTop = ball.y + ball.radius - brick.y;
    const overlapBottom = brick.y + brick.height - (ball.y - ball.radius);
    const minOverlap = Math.min(overlapLeft, overlapRight, overlapTop, overlapBottom);

    if (minOverlap === overlapLeft || minOverlap === overlapRight) {
      ball.dx *= -1;
    } else {
      ball.dy *= -1;
    }

    if (bricks.every((item) => !item.active)) {
      endGame("won", "Clear! Click or Press Space to Restart");
    }

    break;
  }
}

function circleRectOverlap(circle, rect) {
  const closestX = Math.max(rect.x, Math.min(circle.x, rect.x + rect.width));
  const closestY = Math.max(rect.y, Math.min(circle.y, rect.y + rect.height));
  const distanceX = circle.x - closestX;
  const distanceY = circle.y - closestY;

  return distanceX * distanceX + distanceY * distanceY <= circle.radius * circle.radius;
}

function checkMiss() {
  if (ball.y - ball.radius <= HEIGHT) {
    return;
  }

  lives -= 1;
  updateHud();

  if (lives <= 0) {
    endGame("lost", "Game Over. Click or Press Space to Restart");
    return;
  }

  state = "ready";
  resetPositions();
  showMessage("Life Lost. Click or Press Space to Continue");
}

function endGame(nextState, message) {
  state = nextState;
  showMessage(message);
}

function draw() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
  drawBackground();
  drawBricks();
  drawPaddle();
  drawBall();
}

function drawBackground() {
  ctx.fillStyle = "#171b22";
  ctx.fillRect(0, 0, WIDTH, HEIGHT);

  ctx.strokeStyle = "rgba(255, 255, 255, 0.06)";
  ctx.lineWidth = 1;

  for (let x = 0; x <= WIDTH; x += 40) {
    ctx.beginPath();
    ctx.moveTo(x, 0);
    ctx.lineTo(x, HEIGHT);
    ctx.stroke();
  }

  for (let y = 0; y <= HEIGHT; y += 40) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(WIDTH, y);
    ctx.stroke();
  }
}

function drawBricks() {
  for (const brick of bricks) {
    if (!brick.active) {
      continue;
    }

    ctx.fillStyle = brick.color;
    roundRect(brick.x, brick.y, brick.width, brick.height, 5);
    ctx.fill();

    ctx.fillStyle = "rgba(255, 255, 255, 0.25)";
    roundRect(brick.x + 5, brick.y + 4, brick.width - 10, 5, 3);
    ctx.fill();
  }
}

function drawPaddle() {
  ctx.fillStyle = "#f4f7fb";
  roundRect(paddle.x, paddle.y, paddle.width, paddle.height, 8);
  ctx.fill();

  ctx.fillStyle = "#42d1a4";
  roundRect(paddle.x + 9, paddle.y + 4, paddle.width - 18, 4, 3);
  ctx.fill();
}

function drawBall() {
  const gradient = ctx.createRadialGradient(ball.x - 3, ball.y - 4, 2, ball.x, ball.y, ball.radius);
  gradient.addColorStop(0, "#ffffff");
  gradient.addColorStop(1, "#ffcc5c");
  ctx.fillStyle = gradient;
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fill();
}

function roundRect(x, y, width, height, radius) {
  const size = Math.min(radius, width / 2, height / 2);
  ctx.beginPath();
  ctx.moveTo(x + size, y);
  ctx.lineTo(x + width - size, y);
  ctx.quadraticCurveTo(x + width, y, x + width, y + size);
  ctx.lineTo(x + width, y + height - size);
  ctx.quadraticCurveTo(x + width, y + height, x + width - size, y + height);
  ctx.lineTo(x + size, y + height);
  ctx.quadraticCurveTo(x, y + height, x, y + height - size);
  ctx.lineTo(x, y + size);
  ctx.quadraticCurveTo(x, y, x + size, y);
  ctx.closePath();
}

function movePaddleToClientX(clientX) {
  const rect = canvas.getBoundingClientRect();
  const scale = WIDTH / rect.width;
  paddle.x = (clientX - rect.left) * scale - paddle.width / 2;
  clampPaddle();

  if (state !== "playing") {
    ball.x = paddle.x + paddle.width / 2;
    ball.y = paddle.y - ball.radius - 1;
    draw();
  }
}

document.addEventListener("keydown", (event) => {
  if (["ArrowLeft", "ArrowRight", "KeyA", "KeyD"].includes(event.code)) {
    keys.add(event.code);
    event.preventDefault();
  }

  if (event.code === "Space") {
    event.preventDefault();
    startGame();
  }
});

document.addEventListener("keyup", (event) => {
  keys.delete(event.code);
});

canvas.addEventListener("mousemove", (event) => {
  movePaddleToClientX(event.clientX);
});

canvas.addEventListener("touchstart", (event) => {
  event.preventDefault();
  movePaddleToClientX(event.touches[0].clientX);
  startGame();
}, { passive: false });

canvas.addEventListener("touchmove", (event) => {
  event.preventDefault();
  movePaddleToClientX(event.touches[0].clientX);
}, { passive: false });

canvas.addEventListener("click", startGame);

resetGame();
