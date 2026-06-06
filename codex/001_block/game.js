const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const levelEl = document.getElementById("level");
const scoreEl = document.getElementById("score");
const livesEl = document.getElementById("lives");
const overlay = document.getElementById("overlay");
const statusText = document.getElementById("statusText");
const pauseMenu = document.getElementById("pauseMenu");
const pauseButtons = Array.from(document.querySelectorAll(".pause-button"));

const WIDTH = canvas.width;
const HEIGHT = canvas.height;
const PADDLE_WIDTH = 118;
const PADDLE_HEIGHT = 16;
const BALL_RADIUS = 9;
const START_LIVES = 3;
const FINAL_LEVEL_INDEX = 2;

const brickConfig = {
  rows: 5,
  cols: 9,
  width: 72,
  height: 24,
  gap: 10,
  top: 78,
  left: 31,
};

const levels = [
  {
    name: "Level 1",
    label: "1",
    colors: ["#42d1a4", "#ffcc5c", "#5ab0ff", "#ff7a90", "#b18cff"],
    ballSpeed: { dx: 4.1, dy: -5.2 },
    paddleSpeed: 8,
    layouts: [
      [
        "111111111",
        "111111111",
        "111111111",
        "111111111",
        "000000000",
      ],
      [
        "111010111",
        "011111110",
        "111111111",
        "011111110",
        "101110101",
      ],
    ],
  },
  {
    name: "Level 2",
    label: "2",
    colors: ["#4ddad4", "#ffd166", "#7aa8ff", "#ff8ab3", "#c79cff"],
    ballSpeed: { dx: 4.8, dy: -6.1 },
    paddleSpeed: 8.8,
    layouts: [
      [
        "111111111",
        "111111111",
        "110111011",
        "111111111",
        "111010111",
      ],
      [
        "101111101",
        "111111111",
        "011111110",
        "111111111",
        "110101011",
      ],
    ],
  },
  {
    name: "Boss",
    label: "Boss",
    colors: ["#ff6b6b", "#ffcc5c"],
    ballSpeed: { dx: 5.1, dy: -6.4 },
    paddleSpeed: 9.2,
    boss: {
      x: 245,
      y: 78,
      width: 310,
      height: 82,
      hp: 18,
      color: "#ff6b6b",
      accent: "#ffcc5c",
    },
  },
];

let currentLevel = 0;
let score = 0;
let lives = START_LIVES;
let state = "ready";
let animationId = null;
let keys = new Set();
let bricks = [];
let boss = null;
let paddle;
let ball;
let selectedPauseIndex = 0;

function getLevel() {
  return levels[currentLevel];
}

function createBricks() {
  bricks = [];
  boss = null;

  const level = getLevel();
  if (level.boss) {
    boss = {
      ...level.boss,
      maxHp: level.boss.hp,
      active: true,
    };
    return;
  }

  const layout = level.layouts[Math.floor(Math.random() * level.layouts.length)];

  for (let row = 0; row < brickConfig.rows; row += 1) {
    for (let col = 0; col < brickConfig.cols; col += 1) {
      if (layout[row][col] !== "1") {
        continue;
      }

      bricks.push({
        x: brickConfig.left + col * (brickConfig.width + brickConfig.gap),
        y: brickConfig.top + row * (brickConfig.height + brickConfig.gap),
        width: brickConfig.width,
        height: brickConfig.height,
        color: level.colors[row % level.colors.length],
        active: true,
      });
    }
  }
}

function resetPositions() {
  const level = getLevel();

  paddle = {
    x: (WIDTH - PADDLE_WIDTH) / 2,
    y: HEIGHT - 44,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT,
    speed: level.paddleSpeed,
  };

  ball = {
    x: WIDTH / 2,
    y: paddle.y - BALL_RADIUS - 1,
    dx: level.ballSpeed.dx,
    dy: level.ballSpeed.dy,
    radius: BALL_RADIUS,
  };
}

function resetCampaignState() {
  currentLevel = 0;
  score = 0;
  lives = START_LIVES;
  state = "ready";
  createBricks();
  resetPositions();
  updateHud();
}

function resetGame() {
  resetCampaignState();
  showMessage("スペースキーまたはクリックで開始");
  draw();
}

function updateHud() {
  levelEl.textContent = getLevel().label;
  scoreEl.textContent = score.toString();
  livesEl.textContent = lives.toString();
}

function showMessage(message) {
  statusText.textContent = message;
  hidePauseMenu();
  overlay.classList.remove("hidden");
}

function hideMessage() {
  overlay.classList.add("hidden");
}

function showPauseMenu() {
  statusText.textContent = "一時停止";
  selectedPauseIndex = 0;
  pauseMenu.classList.remove("hidden");
  overlay.classList.remove("hidden");
  updatePauseSelection();
}

function hidePauseMenu() {
  pauseMenu.classList.add("hidden");
  pauseButtons.forEach((button) => {
    button.classList.remove("is-selected");
    button.setAttribute("tabindex", "-1");
  });
}

function startGame() {
  if (state === "playing" || state === "paused") {
    return;
  }

  if (state === "level-cleared") {
    startNextLevel();
    return;
  }

  if (state === "won" || state === "lost") {
    resetGame();
  }

  state = "playing";
  hideMessage();
  runLoop();
}

function startNextLevel() {
  currentLevel += 1;
  state = "playing";
  createBricks();
  resetPositions();
  updateHud();
  hideMessage();
  draw();
  runLoop();
}

function togglePause() {
  if (state === "playing") {
    state = "paused";
    keys.clear();
    if (animationId !== null) {
      cancelAnimationFrame(animationId);
      animationId = null;
    }
    showPauseMenu();
    draw();
    return;
  }

  if (state === "paused") {
    resumeGame();
  }
}

function resumeGame() {
  if (state !== "paused") {
    return;
  }

  state = "playing";
  hideMessage();
  runLoop();
}

function restartGame() {
  resetCampaignState();
  state = "playing";
  hideMessage();
  draw();
  runLoop();
}

function quitToTitle() {
  resetGame();
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
  } else {
    animationId = null;
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
  if (state !== "playing") {
    return;
  }

  collideWithBoss();
  if (state !== "playing") {
    return;
  }

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

  const rawHitPosition = (ball.x - (paddle.x + paddle.width / 2)) / (paddle.width / 2);
  const hitPosition = Math.max(-1, Math.min(1, rawHitPosition));
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
    bounceBallFromRect(brick);

    if (bricks.every((item) => !item.active)) {
      completeLevel();
    }

    break;
  }
}

function collideWithBoss() {
  if (!boss?.active || !circleRectOverlap(ball, boss)) {
    return;
  }

  boss.hp -= 1;
  score += 25;
  updateHud();
  bounceBallFromRect(boss);

  if (boss.hp <= 0) {
    boss.active = false;
    endGame("won", "完全クリア！スペースキーまたはクリックで最初から");
  }
}

function bounceBallFromRect(rect) {
  const overlapLeft = ball.x + ball.radius - rect.x;
  const overlapRight = rect.x + rect.width - (ball.x - ball.radius);
  const overlapTop = ball.y + ball.radius - rect.y;
  const overlapBottom = rect.y + rect.height - (ball.y - ball.radius);
  const minOverlap = Math.min(overlapLeft, overlapRight, overlapTop, overlapBottom);

  if (minOverlap === overlapLeft) {
    ball.x = rect.x - ball.radius;
    ball.dx = -Math.abs(ball.dx);
    return;
  }

  if (minOverlap === overlapRight) {
    ball.x = rect.x + rect.width + ball.radius;
    ball.dx = Math.abs(ball.dx);
    return;
  }

  if (minOverlap === overlapTop) {
    ball.y = rect.y - ball.radius;
    ball.dy = -Math.abs(ball.dy);
    return;
  }

  ball.y = rect.y + rect.height + ball.radius;
  ball.dy = Math.abs(ball.dy);
}

function completeLevel() {
  if (currentLevel === 0) {
    endGame("level-cleared", "レベル1クリア！スペースキーまたはクリックでレベル2へ");
    return;
  }

  if (currentLevel === 1) {
    endGame("level-cleared", "レベル2クリア！スペースキーまたはクリックでボス戦へ");
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
    endGame("lost", "ゲームオーバー。スペースキーまたはクリックで最初から");
    return;
  }

  state = "ready";
  resetPositions();
  showMessage("ミス！スペースキーまたはクリックで続行");
}

function endGame(nextState, message) {
  state = nextState;
  keys.clear();
  if (animationId !== null) {
    cancelAnimationFrame(animationId);
    animationId = null;
  }
  showMessage(message);
}

function draw() {
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
  drawBackground();
  drawStageLabel();
  drawBricks();
  drawBoss();
  drawPaddle();
  drawBall();
}

function drawBackground() {
  ctx.fillStyle = currentLevel === FINAL_LEVEL_INDEX ? "#1f1418" : "#171b22";
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

function drawStageLabel() {
  ctx.fillStyle = "rgba(255, 255, 255, 0.72)";
  ctx.font = "700 18px Arial, sans-serif";
  ctx.textAlign = "left";
  ctx.textBaseline = "top";
  ctx.fillText(getLevel().name, 24, 22);
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

function drawBoss() {
  if (!boss?.active) {
    return;
  }

  ctx.fillStyle = "rgba(255, 107, 107, 0.16)";
  roundRect(boss.x - 16, boss.y - 16, boss.width + 32, boss.height + 32, 12);
  ctx.fill();

  ctx.fillStyle = boss.color;
  roundRect(boss.x, boss.y, boss.width, boss.height, 10);
  ctx.fill();

  ctx.fillStyle = boss.accent;
  roundRect(boss.x + 18, boss.y + 14, boss.width - 36, 12, 6);
  ctx.fill();

  ctx.fillStyle = "rgba(17, 19, 24, 0.35)";
  roundRect(boss.x + 48, boss.y + 42, boss.width - 96, 18, 9);
  ctx.fill();

  drawBossHpBar();
}

function drawBossHpBar() {
  const barWidth = 360;
  const barHeight = 14;
  const x = (WIDTH - barWidth) / 2;
  const y = 24;
  const ratio = Math.max(0, boss.hp / boss.maxHp);

  ctx.fillStyle = "rgba(255, 255, 255, 0.14)";
  roundRect(x, y, barWidth, barHeight, 7);
  ctx.fill();

  ctx.fillStyle = "#ffcc5c";
  roundRect(x, y, barWidth * ratio, barHeight, 7);
  ctx.fill();

  ctx.fillStyle = "#f4f7fb";
  ctx.font = "700 13px Arial, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "bottom";
  ctx.fillText(`BOSS HP ${boss.hp}/${boss.maxHp}`, WIDTH / 2, y - 4);
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

  if (state === "ready") {
    ball.x = paddle.x + paddle.width / 2;
    ball.y = paddle.y - ball.radius - 1;
    draw();
  }
}

function updatePauseSelection() {
  pauseButtons.forEach((button, index) => {
    const isSelected = index === selectedPauseIndex;
    button.classList.toggle("is-selected", isSelected);
    button.setAttribute("tabindex", isSelected ? "0" : "-1");
  });

  pauseButtons[selectedPauseIndex]?.focus();
}

function movePauseSelection(direction) {
  selectedPauseIndex = (selectedPauseIndex + direction + pauseButtons.length) % pauseButtons.length;
  updatePauseSelection();
}

function activatePauseSelection() {
  const selectedButton = pauseButtons[selectedPauseIndex];
  if (selectedButton) {
    handlePauseAction(selectedButton.dataset.action);
  }
}

function handlePauseAction(action) {
  if (action === "resume") {
    resumeGame();
    return;
  }

  if (action === "restart") {
    restartGame();
    return;
  }

  if (action === "quit") {
    quitToTitle();
  }
}

document.addEventListener("keydown", (event) => {
  if (state === "paused") {
    if (event.code === "Escape") {
      event.preventDefault();
      resumeGame();
      return;
    }

    if (event.code === "ArrowUp") {
      event.preventDefault();
      movePauseSelection(-1);
      return;
    }

    if (event.code === "ArrowDown") {
      event.preventDefault();
      movePauseSelection(1);
      return;
    }

    if (event.code === "Enter" || event.code === "Space") {
      event.preventDefault();
      activatePauseSelection();
      return;
    }
  }

  if (["ArrowLeft", "ArrowRight", "KeyA", "KeyD"].includes(event.code)) {
    keys.add(event.code);
    event.preventDefault();
  }

  if (event.code === "Space") {
    event.preventDefault();
    startGame();
  }

  if (event.code === "Escape") {
    event.preventDefault();
    togglePause();
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

pauseButtons.forEach((button, index) => {
  button.addEventListener("click", () => {
    selectedPauseIndex = index;
    handlePauseAction(button.dataset.action);
  });

  button.addEventListener("mouseenter", () => {
    selectedPauseIndex = index;
    updatePauseSelection();
  });
});

resetGame();
