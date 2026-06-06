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
const BOSS_HP_BY_ROW = [3, 2, 3, 1, 3]; // ボス各行のHP

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
const LEVEL_LAYOUTS = [
  // --- Lv1 ---
  [
    [
      [0,0,0,1,1,0,0,0],
      [0,0,1,1,1,1,0,0],
      [1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,0,0],
      [0,0,0,1,1,0,0,0],
    ],
    [
      [1,0,1,0,1,0,1,0],
      [0,1,0,1,0,1,0,1],
      [1,0,1,0,1,0,1,0],
      [0,1,0,1,0,1,0,1],
      [1,0,1,0,1,0,1,0],
    ],
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
    [
      [0,0,1,1,1,1,0,0],
      [0,1,1,1,1,1,1,0],
      [1,1,1,1,1,1,1,1],
      [0,1,1,1,1,1,1,0],
      [0,0,1,1,1,1,0,0],
    ],
    [
      [0,0,1,1,1,1,0,0],
      [1,1,0,1,1,0,1,1],
      [1,1,1,1,1,1,1,1],
      [1,1,0,1,1,0,1,1],
      [0,0,1,1,1,1,0,0],
    ],
    [
      [1,0,1,0,1,0,1,0],
      [1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1],
      [1,1,0,0,0,0,1,1],
      [0,0,0,0,0,0,0,0],
    ],
  ],
  // --- Lv3 ボス ---
  [
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
let state;
let score, lives, level, blocks, paddle, ball, speed, paddleW, pauseMenuIndex;
const keys = {};

// ボス専用状態
let bossHpTotal = 0;
let bossEnraged = false;
let shakeTimer = 0;
let enrageFlashAlpha = 0;
let bossOscTime = 0;

function buildBlocks(layout) {
  blocks = [];
  bossHpTotal = 0;
  bossEnraged = false;
  enrageFlashAlpha = 0;
  bossOscTime = 0;
  shakeTimer = 0;
  const isBoss = (level === 3);
  for (let r = 0; r < ROWS; r++) {
    for (let c = 0; c < COLS; c++) {
      if (!layout[r][c]) continue;
      const maxHp = isBoss ? BOSS_HP_BY_ROW[r] : 1;
      const baseX = BLOCK_OFFSET_X + c * (BLOCK_W + BLOCK_PAD);
      blocks.push({
        x: baseX,
        y: BLOCK_OFFSET_Y + r * (BLOCK_H + BLOCK_PAD),
        baseX,
        w: BLOCK_W, h: BLOCK_H,
        color: ROW_COLORS[r], score: ROW_SCORES[r],
        alive: true,
        hp: maxHp, maxHp,
        row: r,
        oscillates: isBoss && (r === 0 || r === 4),
      });
      if (isBoss) bossHpTotal += maxHp;
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
    if (state === 'idle')          { startLevel(1); }
    else if (state === 'dead')     { resetBall(); state = 'playing'; }
    else if (state === 'levelup')  { startLevel(level + 1); }
    else if (state === 'gameover') { initGame(); }
    else if (state === 'gameclear'){ initGame(); }
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

function updateBoss() {
  if (level !== 3 || state !== 'playing') return;

  if (shakeTimer > 0) shakeTimer--;
  if (enrageFlashAlpha > 0) enrageFlashAlpha = Math.max(0, enrageFlashAlpha - 0.015);

  // ブロック振動 (行0と行4が逆位相で揺れる)
  bossOscTime += bossEnraged ? 0.045 : 0.022;
  for (const b of blocks) {
    if (!b.alive || !b.oscillates) continue;
    const phase = b.row === 0 ? 0 : Math.PI;
    b.x = b.baseX + Math.sin(bossOscTime + phase) * 18;
  }

  // エンレイジ判定 (HP40%以下)
  if (!bossEnraged) {
    const hpLeft = blocks.reduce((s, b) => s + (b.alive ? b.hp : 0), 0);
    if (hpLeft <= Math.floor(bossHpTotal * 0.4)) {
      bossEnraged = true;
      enrageFlashAlpha = 0.75;
      speed = Math.max(speed, LEVEL_CONFIG[2].baseSpeed * 1.45);
    }
  }
}

function update() {
  if (state !== 'playing') return;

  updateBoss();

  speed += LEVEL_CONFIG[level - 1].speedInc;

  // パドル移動
  if (keys['ArrowLeft'] || keys['KeyA']) paddle.x = Math.max(0, paddle.x - PADDLE_SPEED);
  if (keys['ArrowRight'] || keys['KeyD']) paddle.x = Math.min(W - paddleW, paddle.x + PADDLE_SPEED);

  // ボール移動
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
      b.hp--;
      if (b.hp <= 0) {
        b.alive = false;
        score += b.score;
        if (level === 3) shakeTimer = Math.max(shakeTimer, 10);
      } else {
        if (level === 3) shakeTimer = Math.max(shakeTimer, 5);
      }
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

  const isBossActive = level === 3 && (state === 'playing' || state === 'dead' || state === 'paused');

  // 背景
  ctx.fillStyle = isBossActive ? '#1a0000' : '#1a1a2e';
  ctx.fillRect(0, 0, W, H);

  // ボス背景グリッド
  if (isBossActive) {
    ctx.strokeStyle = 'rgba(180,0,0,0.07)';
    ctx.lineWidth = 1;
    for (let gx = 0; gx < W; gx += 40) {
      ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, H); ctx.stroke();
    }
    for (let gy = 0; gy < H; gy += 40) {
      ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(W, gy); ctx.stroke();
    }
  }

  // スクリーンシェイク
  const sx = (level === 3 && shakeTimer > 0) ? (Math.random() - 0.5) * 7 : 0;
  const sy = (level === 3 && shakeTimer > 0) ? (Math.random() - 0.5) * 7 : 0;
  ctx.save();
  ctx.translate(sx, sy);

  // ブロック描画
  for (const b of blocks) {
    if (!b.alive) continue;
    ctx.fillStyle = b.color;
    ctx.fillRect(b.x, b.y, b.w, b.h);

    // ダメージ表現 (ボスのみ)
    if (b.maxHp > 1) {
      const crackCount = b.maxHp - b.hp;
      if (crackCount > 0) {
        ctx.fillStyle = `rgba(0,0,0,${crackCount * 0.25})`;
        ctx.fillRect(b.x, b.y, b.w, b.h);
        ctx.strokeStyle = 'rgba(255,255,255,0.5)';
        ctx.lineWidth = 1.5;
        if (crackCount >= 1) {
          ctx.beginPath();
          ctx.moveTo(b.x + b.w * 0.35, b.y + 2);
          ctx.lineTo(b.x + b.w * 0.55, b.y + b.h - 2);
          ctx.stroke();
        }
        if (crackCount >= 2) {
          ctx.beginPath();
          ctx.moveTo(b.x + b.w * 0.65, b.y + 2);
          ctx.lineTo(b.x + b.w * 0.8, b.y + b.h - 2);
          ctx.stroke();
        }
      }
    }

    ctx.strokeStyle = 'rgba(0,0,0,0.3)';
    ctx.lineWidth = 1;
    ctx.strokeRect(b.x + 0.5, b.y + 0.5, b.w - 1, b.h - 1);
  }

  // パドル
  ctx.fillStyle = (bossEnraged && level === 3) ? '#ff6b6b' : '#ecf0f1';
  ctx.beginPath();
  ctx.roundRect(paddle.x, paddle.y, paddleW, PADDLE_H, 6);
  ctx.fill();

  // ボール
  ctx.fillStyle = (bossEnraged && level === 3) ? '#ff4444' : '#ecf0f1';
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, BALL_R, 0, Math.PI * 2);
  ctx.fill();

  ctx.restore(); // シェイク終了

  // UI: スコア / レベル / ライフ
  ctx.font = '16px monospace';
  ctx.textAlign = 'left';
  ctx.fillStyle = '#ecf0f1';
  ctx.fillText(`SCORE: ${score}`, 12, 22);

  ctx.textAlign = 'center';
  if (isBossActive) {
    ctx.fillStyle = bossEnraged ? '#ff4444' : '#e74c3c';
    ctx.font = 'bold 16px monospace';
    ctx.fillText(bossEnraged ? '★ ENRAGED ★' : 'FINAL BOSS', W / 2, 22);
  } else {
    ctx.fillStyle = '#ecf0f1';
    ctx.font = '16px monospace';
    ctx.fillText(`LEVEL ${level}`, W / 2, 22);
  }

  ctx.textAlign = 'right';
  ctx.fillStyle = '#ecf0f1';
  ctx.font = '16px monospace';
  ctx.fillText(`LIFE: ${'♥'.repeat(lives)}`, W - 12, 22);

  // ボスHPバー
  if (isBossActive) {
    const hpLeft = blocks.reduce((s, b) => s + (b.alive ? b.hp : 0), 0);
    const ratio = bossHpTotal > 0 ? hpLeft / bossHpTotal : 0;
    const barX = 12, barY = 33, barW = W - 24, barH = 7;
    ctx.fillStyle = '#2c0000';
    ctx.fillRect(barX, barY, barW, barH);
    ctx.fillStyle = bossEnraged
      ? `hsl(${Math.floor(Date.now() / 80) % 30}, 100%, 55%)`
      : `hsl(${Math.floor(ratio * 40)}, 90%, 45%)`;
    ctx.fillRect(barX, barY, barW * ratio, barH);
    ctx.strokeStyle = '#550000';
    ctx.lineWidth = 1;
    ctx.strokeRect(barX, barY, barW, barH);
  }

  // エンレイジフラッシュ
  if (enrageFlashAlpha > 0) {
    ctx.fillStyle = `rgba(200,0,0,${enrageFlashAlpha})`;
    ctx.fillRect(0, 0, W, H);
    if (enrageFlashAlpha > 0.3) {
      ctx.fillStyle = `rgba(255,255,255,${(enrageFlashAlpha - 0.3) / 0.45})`;
      ctx.font = 'bold 52px monospace';
      ctx.textAlign = 'center';
      ctx.fillText('ENRAGED!', W / 2, H / 2);
    }
  }

  // オーバーレイ
  if (state === 'idle') {
    drawOverlay('BLOCK BREAKER', 'スペースキーでスタート');
  } else if (state === 'dead') {
    drawOverlay(`残り ${lives} 機`, 'スペースキーで続ける');
  } else if (state === 'gameover') {
    drawOverlay('GAME OVER', `SCORE: ${score}\nスペースキーでリスタート`);
  } else if (state === 'levelup') {
    if (level + 1 === 3) {
      drawBossWarning();
    } else {
      drawOverlay(`LEVEL ${level} CLEAR!`, `SCORE: ${score}\n\n次は LEVEL ${level + 1}\nスペースキーで挑戦`);
    }
  } else if (state === 'gameclear') {
    drawOverlay('ALL CLEAR!!', `全ステージ制覇!\nFINAL SCORE: ${score}\nスペースキーでタイトルへ`);
  } else if (state === 'paused') {
    drawPauseMenu();
  }
}

function drawBossWarning() {
  ctx.fillStyle = 'rgba(0,0,0,0.88)';
  ctx.fillRect(0, 0, W, H);

  // 赤いラインで縁取り
  ctx.strokeStyle = '#e74c3c';
  ctx.lineWidth = 4;
  ctx.strokeRect(8, 8, W - 16, H - 16);
  ctx.strokeStyle = 'rgba(231,76,60,0.3)';
  ctx.lineWidth = 2;
  ctx.strokeRect(16, 16, W - 32, H - 32);

  ctx.fillStyle = '#e74c3c';
  ctx.font = 'bold 18px monospace';
  ctx.textAlign = 'center';
  ctx.fillText('⚠  WARNING  ⚠', W / 2, H / 2 - 80);

  ctx.fillStyle = '#ff4444';
  ctx.font = 'bold 40px monospace';
  ctx.fillText('FINAL BOSS', W / 2, H / 2 - 30);

  ctx.fillStyle = '#ecf0f1';
  ctx.font = '17px monospace';
  ctx.fillText('最後の強敵が待ち受ける...', W / 2, H / 2 + 18);
  ctx.fillText(`現在のスコア: ${score}`, W / 2, H / 2 + 50);

  ctx.fillStyle = '#f1c40f';
  ctx.font = 'bold 18px monospace';
  ctx.fillText('スペースキーで挑戦', W / 2, H / 2 + 95);
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
