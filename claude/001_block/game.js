const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const W = canvas.width;
const H = canvas.height;

// ブロック設定
const COLS = 8;
const ROWS = 5;
const BLOCK_W = 52;
const BLOCK_H = 20;
const BLOCK_PAD = 4;
const BLOCK_OFFSET_X = (W - (COLS * (BLOCK_W + BLOCK_PAD) - BLOCK_PAD)) / 2;
const BLOCK_OFFSET_Y = 60;
const ROW_COLORS = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#3498db'];
const ROW_SCORES = [50, 40, 30, 20, 10];

// パドル・ボール固定値
const PADDLE_H = 12;
const PADDLE_Y = H - 50;
const PADDLE_SPEED = 6;
const BALL_R = 8;

// レベルごとの設定
const LEVEL_CONFIG = [
  { paddleW: 80, baseSpeed: 4, speedInc: 0.0005 },
  { paddleW: 70, baseSpeed: 5, speedInc: 0.001  },
  { paddleW: 60, baseSpeed: 6, speedInc: 0.002  },
];

// 盤面レイアウト (1=ブロック, 0=空き)
// Lv1: 各600点  Lv2: 各840点  Lv3(ボス): 1040点
const LEVEL_LAYOUTS = [
  // --- Lv1 ---
  [
    // ダイヤモンド (2-4-8-4-2)
    [
      [0,0,0,1,1,0,0,0],
      [0,0,1,1,1,1,0,0],
      [1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,0,0],
      [0,0,0,1,1,0,0,0],
    ],
    // チェッカー (4-4-4-4-4)
    [
      [1,0,1,0,1,0,1,0],
      [0,1,0,1,0,1,0,1],
      [1,0,1,0,1,0,1,0],
      [0,1,0,1,0,1,0,1],
      [1,0,1,0,1,0,1,0],
    ],
    // 砂時計 (2-4-8-4-2 両端)
    [
      [1,0,0,0,0,0,0,1],
      [1,1,0,0,0,0,1,1],
      [1,1,1,1,1,1,1,1],
      [1,1,0,0,0,0,1,1],
      [1,0,0,0,0,0,0,1],
    ],
  ],
  // --- Lv2 ---
  [
    // 大ダイヤモンド (4-6-8-6-4)
    [
      [0,0,1,1,1,1,0,0],
      [0,1,1,1,1,1,1,0],
      [1,1,1,1,1,1,1,1],
      [0,1,1,1,1,1,1,0],
      [0,0,1,1,1,1,0,0],
    ],
    // ウィング (4-6-8-6-4 翼型)
    [
      [0,0,1,1,1,1,0,0],
      [1,1,0,1,1,0,1,1],
      [1,1,1,1,1,1,1,1],
      [1,1,0,1,1,0,1,1],
      [0,0,1,1,1,1,0,0],
    ],
    // 城壁 (4-8-8-4-0)
    [
      [1,0,1,0,1,0,1,0],
      [1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1],
      [1,1,0,0,0,0,1,1],
      [0,0,0,0,0,0,0,0],
    ],
  ],
  // --- Lv3 ボス (固定1種) ---
  [
    // ボスフェイス (8-6-8-4-8)
    [
      [1,1,1,1,1,1,1,1],
      [1,0,1,1,1,1,0,1],
      [1,1,1,1,1,1,1,1],
      [1,0,0,1,1,0,0,1],
      [1,1,1,1,1,1,1,1],
    ],
  ],
];

// ゲーム状態
let state; // 'idle'|'playing'|'paused'|'dead'|'levelup'|'gameover'|'gameclear'
let score, lives, level, blocks, paddle, ball, speed, paddleW, pauseMenuIndex;
const keys = {};

function buildBlocks(layout) {
  blocks = [];
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (!layout[r][c]) continue;
      blocks.push({
        x: BLOCK_OFFSET_X + c * (BLOCK_W + BLOCK_PAD),
        y: BLOCK_OFFSET_Y + r * (BLOCK_H + BLOCK_PAD),
        w: BLOCK_W, h: BLOCK_H,
        color: ROW_COLORS[r], score: ROW_SCORES[r],
        alive: true,
      });
    }
  }
}

function resetBall() {
  const angle = (Math.random() * 60 + 60) * (Math.PI / 180);
  ball = {
    x: paddle.x + paddleW / 2,
    y: paddle.y - BALL_R - 1,
    dx: speed * Math.cos(angle) * (Math.random() < 0.5 ? 1 : -1),
    dy: -speed * Math.sin(angle),
  };
}

function initGame() {
  level = 1;
  score = 0;
  lives = 3;
  const cfg = LEVEL_CONFIG[0];
  paddleW = cfg.paddleW;
  speed = cfg.baseSpeed;
  paddle = { x: W / 2 - paddleW / 2, y: PADDLE_Y };
  resetBall();
  blocks = [];
  state = 'idle';
}

function startLevel(n) {
  level = n;
  const cfg = LEVEL_CONFIG[n - 1];
  paddleW = cfg.paddleW;
  speed = cfg.baseSpeed;
  paddle = { x: W / 2 - paddleW / 2, y: PADDLE_Y };
  resetBall();
  const layouts = LEVEL_LAYOUTS[n - 1];
  buildBlocks(layouts[Math.floor(Math.random() * layouts.length)]);
  state = 'playing';
}

// 入力
document.addEventListener('keydown', e => {
  keys[e.code] = true;

  if (e.code === 'Space') {
    if (state === 'idle')      { startLevel(1); }
    else if (state === 'dead') { resetBall(); state = 'playing'; }
    else if (state === 'levelup')   { startLevel(level + 1); }
    else if (state === 'gameover')  { initGame(); }
    else if (state === 'gameclear') { initGame(); }
  }

  if (e.code === 'Escape') {
    if (state === 'playing') { state = 'paused'; pauseMenuIndex = 0; }
    else if (state === 'paused') state = 'playing';
  }

  if (state === 'paused') {
    if (e.code === 'ArrowUp'   || e.code === 'KeyW') pauseMenuIndex = (pauseMenuIndex - 1 + 3) % 3;
    if (e.code === 'ArrowDown' || e.code === 'KeyS') pauseMenuIndex = (pauseMenuIndex + 1) % 3;
    if (e.code === 'Space') {
      if (pauseMenuIndex === 0) state = 'playing';
      else if (pauseMenuIndex === 1) { score = 0; lives = 3; startLevel(1); }
      else if (pauseMenuIndex === 2) initGame();
    }
  }

  if (['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Space'].includes(e.code)) {
    e.preventDefault();
  }
});
document.addEventListener('keyup', e => { keys[e.code] = false; });

function update() {
  if (state !== 'playing') return;

  speed += LEVEL_CONFIG[level - 1].speedInc;

  // パドル移動
  if (keys['ArrowLeft'] || keys['KeyA']) paddle.x = Math.max(0, paddle.x - PADDLE_SPEED);
  if (keys['ArrowRight'] || keys['KeyD']) paddle.x = Math.min(W - paddleW, paddle.x + PADDLE_SPEED);

  // ボール移動 (速度を一定に保つ)
  const spd = Math.hypot(ball.dx, ball.dy);
  ball.dx = ball.dx / spd * speed;
  ball.dy = ball.dy / spd * speed;
  ball.x += ball.dx;
  ball.y += ball.dy;

  // 壁反射
  if (ball.x - BALL_R < 0) { ball.x = BALL_R; ball.dx = Math.abs(ball.dx); }
  if (ball.x + BALL_R > W) { ball.x = W - BALL_R; ball.dx = -Math.abs(ball.dx); }
  if (ball.y - BALL_R < 0) { ball.y = BALL_R; ball.dy = Math.abs(ball.dy); }

  // ボール落下
  if (ball.y - BALL_R > H) {
    lives--;
    if (lives <= 0) {
      state = 'gameover';
    } else {
      speed = LEVEL_CONFIG[level - 1].baseSpeed;
      state = 'dead';
    }
    return;
  }

  // パドル衝突
  if (
    ball.dy > 0 &&
    ball.x > paddle.x &&
    ball.x < paddle.x + paddleW &&
    ball.y + BALL_R >= paddle.y &&
    ball.y + BALL_R <= paddle.y + PADDLE_H + Math.abs(ball.dy)
  ) {
    ball.y = paddle.y - BALL_R;
    const hit = (ball.x - (paddle.x + paddleW / 2)) / (paddleW / 2);
    const angle = hit * (70 * Math.PI / 180);
    ball.dx = speed * Math.sin(angle);
    ball.dy = -speed * Math.cos(angle);
  }

  // ブロック衝突
  for (const b of blocks) {
    if (!b.alive) continue;
    if (
      ball.x + BALL_R > b.x && ball.x - BALL_R < b.x + b.w &&
      ball.y + BALL_R > b.y && ball.y - BALL_R < b.y + b.h
    ) {
      b.alive = false;
      score += b.score;
      // 進行方向から入ってきた辺のオーバーラップだけを比較して正確に反射面を決定
      const hOverlap = ball.dx > 0
        ? (ball.x + BALL_R) - b.x
        : (b.x + b.w) - (ball.x - BALL_R);
      const vOverlap = ball.dy > 0
        ? (ball.y + BALL_R) - b.y
        : (b.y + b.h) - (ball.y - BALL_R);
      if (hOverlap < vOverlap) ball.dx = -ball.dx;
      else ball.dy = -ball.dy;
      break;
    }
  }

  // クリア判定
  if (blocks.every(b => !b.alive)) {
    state = level < 3 ? 'levelup' : 'gameclear';
  }
}

function draw() {
  ctx.clearRect(0, 0, W, H);
  ctx.fillStyle = (level === 3 && state === 'playing') ? '#1a0000' : '#1a1a2e';
  ctx.fillRect(0, 0, W, H);

  // ブロック
  for (const b of blocks) {
    if (!b.alive) continue;
    ctx.fillStyle = b.color;
    ctx.fillRect(b.x, b.y, b.w, b.h);
    ctx.strokeStyle = 'rgba(0,0,0,0.3)';
    ctx.lineWidth = 1;
    ctx.strokeRect(b.x + 0.5, b.y + 0.5, b.w - 1, b.h - 1);
  }

  // パドル
  ctx.fillStyle = '#ecf0f1';
  ctx.beginPath();
  ctx.roundRect(paddle.x, paddle.y, paddleW, PADDLE_H, 6);
  ctx.fill();

  // ボール
  ctx.fillStyle = '#ecf0f1';
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, BALL_R, 0, Math.PI * 2);
  ctx.fill();

  // UI: スコア / レベル / ライフ
  ctx.font = '16px monospace';
  ctx.textAlign = 'left';
  ctx.fillStyle = '#ecf0f1';
  ctx.fillText(`SCORE: ${score}`, 12, 22);

  ctx.textAlign = 'center';
  if (level === 3 && state === 'playing') {
    ctx.fillStyle = '#e74c3c';
    ctx.font = 'bold 16px monospace';
    ctx.fillText('FINAL BOSS', W / 2, 22);
  } else {
    ctx.fillStyle = '#ecf0f1';
    ctx.fillText(`LEVEL ${level}`, W / 2, 22);
  }

  ctx.textAlign = 'right';
  ctx.fillStyle = '#ecf0f1';
  ctx.font = '16px monospace';
  ctx.fillText(`LIFE: ${'♥'.repeat(lives)}`, W - 12, 22);

  // オーバーレイ
  if (state === 'idle') {
    drawOverlay('BLOCK BREAKER', 'スペースキーでスタート');
  } else if (state === 'dead') {
    drawOverlay(`残り ${lives} 機`, 'スペースキーで続ける');
  } else if (state === 'gameover') {
    drawOverlay('GAME OVER', `SCORE: ${score}\nスペースキーでリスタート`);
  } else if (state === 'levelup') {
    const nextTitle = level + 1 === 3 ? 'FINAL BOSS' : `LEVEL ${level + 1}`;
    drawOverlay(`LEVEL ${level} CLEAR!`, `SCORE: ${score}\n\n次は ${nextTitle}\nスペースキーで挑戦`);
  } else if (state === 'gameclear') {
    drawOverlay('ALL CLEAR!!', `全ステージ制覇!\nFINAL SCORE: ${score}\nスペースキーでタイトルへ`);
  } else if (state === 'paused') {
    drawPauseMenu();
  }
}

function drawOverlay(title, sub) {
  ctx.fillStyle = 'rgba(0,0,0,0.65)';
  ctx.fillRect(0, 0, W, H);

  ctx.fillStyle = '#f1c40f';
  ctx.font = 'bold 36px monospace';
  ctx.textAlign = 'center';
  ctx.fillText(title, W / 2, H / 2 - 20);

  ctx.fillStyle = '#ecf0f1';
  ctx.font = '18px monospace';
  sub.split('\n').forEach((line, i) => {
    ctx.fillText(line, W / 2, H / 2 + 20 + i * 28);
  });
}

function drawPauseMenu() {
  ctx.fillStyle = 'rgba(0,0,0,0.65)';
  ctx.fillRect(0, 0, W, H);

  ctx.fillStyle = '#f1c40f';
  ctx.font = 'bold 36px monospace';
  ctx.textAlign = 'center';
  ctx.fillText('PAUSE', W / 2, H / 2 - 70);

  ['ゲームを続ける', '最初からやり直す', 'タイトルに戻る'].forEach((label, i) => {
    const selected = i === pauseMenuIndex;
    ctx.font = selected ? 'bold 20px monospace' : '20px monospace';
    ctx.fillStyle = selected ? '#f1c40f' : '#7f8c8d';
    ctx.textAlign = 'center';
    ctx.fillText((selected ? '▶  ' : '   ') + label, W / 2, H / 2 - 5 + i * 44);
  });

  ctx.fillStyle = '#555';
  ctx.font = '13px monospace';
  ctx.textAlign = 'center';
  ctx.fillText('↑↓ / W S で選択   Space で確定', W / 2, H / 2 + 125);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}

initGame();
loop();
