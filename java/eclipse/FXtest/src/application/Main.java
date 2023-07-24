package application;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.KeyEvent;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;

public class Main extends MainApplication {
	static final int		FPS		= 60; // 固定値FPS（デフォルト値： 60）
	static final boolean	ISDAEMON	= true; // デーモン化（デフォルト値： true）
	static final int WIDTH	= 960;
	static final int HEIGHT	= 540;

	static final float GRAVITY = 9.8f / 60 * 1.8f;
	static final float BOUND = -0.7f;		//地面に当たった時の跳ね返り
	static final float JUMP = -3f;		//ジャンプ時の初期速度
//	static final float M = 1f;			//プレイヤーの初期重さ

	//各キーの配列
	static final byte KEY_SPACE = 0;
	static final byte KEY_ENTER = 1;
	static final byte KEY_UP = 2;
	static final byte KEY_DOWN = 3;
	static final byte KEY_LEFT = 4;
	static final byte KEY_RIGHT = 5;
	static byte[] Key = new byte[6];	//キー押下判定に用いる配列

	static final int MAX_OBSTACLE = 10;

	private Player _player;
	private Obstacle[] _obstacle = new Obstacle[MAX_OBSTACLE] ;

	private long _cnt;
	private boolean _isHit;
	private int _score;

	static enum State {
		TITLE,
		GAME,
		END,
	}
	static State state;

	@Override public void init() {
		setScWidth(WIDTH);		//Sceneの幅
		setScHeight(HEIGHT);	//Sceneの高さ
		setBackColor(Color.BLACK);	//背景色
		setCvWidth(WIDTH);		// Canvasの幅
		setCvHeight(HEIGHT);	// Canvasの高さ

		setFps(FPS);			//FPS
		setIsDaemon(ISDAEMON);	//デーモン化設定

		state = State.TITLE;	//タイトル画面
	}

	@Override
	protected void ofMain(GraphicsContext gc) {
		gc.clearRect(0, 0, WIDTH, HEIGHT);

		switch (state) {
			case TITLE:
				changeBackColor(Color.BLACK);	//背景色
				gc.setFill(Color.WHITE);
				gc.setFont(new Font(60));
				gc.fillText("テストゲーム", WIDTH / 2 -150, HEIGHT / 2 - 30);
				gc.setFont(new Font(20));
				gc.fillText("Enterキーを押してください。", WIDTH / 2 -100, HEIGHT / 2 + 40);
				if(Key[KEY_ENTER] == 1) {
					state = State.GAME;
					Key[KEY_ENTER] = 0;
					gameInit();
				}
				break;

			case GAME:
				changeBackColor(Color.LIGHTGRAY);	//背景色



				gc.setFont(new Font(20));
				gc.setFill(Color.BLACK);

				if(getIsHit()) {
					gc.setFont(new Font(40));
					gc.setFill(Color.RED);
					gc.fillText("Hit!!",50,120);
					setIsHit(false);
				}

				gc.fillText("vy=" + String.valueOf(getPlayer().getVy()) + "\r\n"
							+ "y=" + String.valueOf(getPlayer().getY()) + "\r\n"
							+ "スコア：" + String.valueOf(getScore()) , 50, 50);
				getPlayer().draw(gc);	//プレイヤー描画
				getPlayer().update();	//プレイヤーの更新

				for(Obstacle o : getObstacles()) {
					o.update();
					o.draw(gc);
				}

				judge(getPlayer());	//当たり判定

				if(getCnt() % 60 == 0) {
					for(Obstacle o : getObstacles()) {
						if(!o.getExist()) { // 存在していないなら
							o.generate();
						}
					}
				}

				setScore( getScore() + 1 );
				setCnt(getCnt() + 1);
				break;

			case END:
				changeBackColor(Color.RED);	//背景色
				gc.setFill(Color.WHITE);
				gc.setFont(new Font(60));
				gc.fillText("GAME OVER!" + "\r\n"
						+ "スコア：" + getScore()
						, WIDTH / 2 -150, HEIGHT / 2 - 30);
				if(Key[KEY_ENTER] == 1) {
					state = State.TITLE;
					Key[KEY_ENTER] = 0;
					gameInit();
					gc.clearRect(0, 0, WIDTH, HEIGHT);
				}
			default:

		}

	}

	private void gameInit() {
		setIsHit(false);

		setPlayer(new Player());	//Playerをインスタンス化して_playerにいれる
		getPlayer().init();			//プレイヤーの初期化
		setScore(0);				//スコアを初期化
		for(int i = 0; i < MAX_OBSTACLE; i++) {
			setObstacle(i,new Obstacle());
			getObstacle(i).init();			//プレイヤーの初期化
		}
	}

	//当たり判定
	private void judge(Player p) {
		float xLeft,xRight,yUp,yDown;
		float len;

		for(Obstacle o : getObstacles()) {
			if(o.getExist()) {
				xLeft = o.getX();
				xRight = o.getX() + o.getWidth();
				yUp = o.getY();
				yDown = o.getY() + o.getHeight();;

				/*
				if(xLeft < p.getX() + Player.R && p.getX() - Player.R < xRight
				   && yUp < p.getY() + Player.R && p.getY() - Player.R < yDown) {
					float x[] = {xLeft, xRight, xLeft, xRight};
					float y[] = {yUp, yUp, yDown, yDown};
					for(int i = 0; i < 4; i++ ) {
						len = (float) Math.sqrt(Math.pow(Math.abs(p.getX() - x[i]),2)
												+ Math.pow(Math.abs(p.getY() - y[i]),2));
						if(len < Player.R) {
							System.out.println("Hit!");
						}
					}
				}
				*/

				//上下端
				if(xLeft < p.getX() && p.getX() < xRight
					&& yUp - Player.R < p.getY() && p.getY() < yDown + Player.R) {
					state = State.END;
					return;
				}

				//左右端
				if(xLeft - Player.R < p.getX() && p.getX() < xRight + Player.R
					&& yUp < p.getY() && p.getY() < yDown) {
					state = State.END;
					return;
				}

				//四隅の周り
				float x[] = {xLeft, xRight, xLeft, xRight};
				float y[] = {yUp, yUp, yDown, yDown};
				for(int i = 0; i < 4; i++ ) {
					len = (float) Math.sqrt(Math.pow(p.getX() - x[i],2)
							+ Math.pow(p.getY() - y[i],2));
					if(len < Player.R) {
						state = State.END;
						return;
					}
				}
			}
		}
	}

	@Override
	protected void ofKeyPressed(KeyEvent e) {
		System.out.println("キーコード：" + e.getCode().toString() );
		switch(e.getCode()) {
			case SPACE:
				Key[KEY_SPACE]++;
				break;
			case ENTER:
				Key[KEY_ENTER]++;
				break;
			case UP:
				Key[KEY_UP]++;
				break;
			case DOWN:
				Key[KEY_DOWN]++;
				break;
			case LEFT:
				Key[KEY_LEFT]++;
				break;
			case RIGHT:
				Key[KEY_RIGHT]++;
				break;
			default:
				break;
		}
	}

	@Override
	protected void ofKeyReleased(KeyEvent e) {
		System.out.println("キーから離した");
		switch(e.getCode()) {
			case SPACE:
				Key[KEY_SPACE] = 0;
				break;
			case ENTER:
				Key[KEY_ENTER] = 0;
				break;
			case UP:
				Key[KEY_UP] = 0;
				break;
			case DOWN:
				Key[KEY_DOWN] = 0;
				break;
			case LEFT:
				Key[KEY_LEFT] = 0;
				break;
			case RIGHT:
				Key[KEY_RIGHT] = 0;
				break;
			default:
				break;
	}
	}

	//getter
	public Player getPlayer() {
		return _player;
	}

	public Obstacle getObstacle(int index) {
		return _obstacle[index];
	}

	public Obstacle[] getObstacles() {
		return _obstacle;
	}

	public long getCnt() {
		return _cnt;
	}

	public boolean getIsHit() {
		return _isHit;
	}

	public int getScore() {
		return _score;
	}

	//setter
	public void setPlayer(Player value) {
		if(getPlayer() == null) { // Playerに値が代入されていなければ
			_player = value;
		}
	}

	public void setObstacle(int index,Obstacle obstacle) {
		this._obstacle[index] = obstacle;
	}

	public void setCnt(long _cnt) {
		this._cnt = _cnt;
	}

	public void setIsHit(boolean isHit) {
		this._isHit = isHit;
	}

	public void setScore(int _score) {
		this._score = _score;
	}
}
