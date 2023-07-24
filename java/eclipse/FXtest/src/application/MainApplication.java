package application;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.input.KeyEvent;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public abstract class MainApplication extends Application {

	private int			_scWidth; // Sceneの幅
	private int			_scHeight; // Sceneの高さ
	private Color			_backColor; // 背景色
	private int			_cvWidth; // Canvasの幅
	private int			_cvHeight; // Canvasの高さ
	private int			_fps; // FPS
	private boolean		_isDaemon; // デーモン化

	private Group		_root;
	private Stage		_stage;
	private Scene		_scene;
	private Canvas		_canvas;
	private GraphicsContext		_gc;


	@Override
	public void start(Stage stage) throws Exception {

		_root = new Group();	//元となるrootGroup作成
		_scene = new Scene(_root,getScWidth(),getScHeight(),getBackColor());
			//Scene作成
		_canvas = new Canvas(getCvWidth(), getCvHeight()); // Canvasを作成
		_gc = _canvas.getGraphicsContext2D(); // CanvasのGraphicsContextを取得

		_root.getChildren().add(_canvas); // rootにCanvasを追加

		_stage = stage;
		_stage.setOnCloseRequest(req -> Platform.exit());
		_stage.setScene(_scene);	//作成したsceneを追加
		_stage.show();			//ウィンドウ表示

		// メインスレッドの定義部
		Thread thread = new Thread(() -> {
			long now = System.currentTimeMillis() << 16;
			long old;
			long err = 0; // 誤差時間（ms）
			long slp; // 休止時間（ms）
			long frm = (1000 << 16) / getFps(); // １フレームの時間（ms）

			while(true) {
				old = now;

				Platform.runLater(() -> {
//					System.out.println("メインループしています。");
					ofMain(_gc);
				});

				now = System.currentTimeMillis() << 16;
				slp = frm - (now - old) - err;
				if(slp < 0x20000) slp = 0x20000;
				old = now;
				try {
					Thread.sleep(slp >> 16);
				}catch(Exception e) {
				}
				now = System.currentTimeMillis() << 16;
				err = now - old - slp;
			}
		});

		thread.setDaemon(getIsDaemon()); // スレッドをデーモン化
		thread.start(); // スレッドを開始

		//キー押下処理
		_scene.setOnKeyPressed(e -> {
			ofKeyPressed(e);
		});

		//キー離上処理
		_scene.setOnKeyReleased(e -> {
			ofKeyReleased(e);
		});
	}

	public void changeBackColor(Color color) {
		_scene.setFill(color);
		_stage.setScene(_scene);	//作成したsceneを追加
		_stage.show();			//ウィンドウ表示
	}

	/**
	 * 毎フレームごとに行う処理を記述
	 * @param gc 描画を行うCanvasのGraphicsContextオブジェクト
	 */
	protected abstract void ofMain(GraphicsContext gc);

	protected abstract void ofKeyPressed(KeyEvent e);

	protected abstract void ofKeyReleased(KeyEvent e);

	//ゲッター(getter)

	public int getFps() {
		return _fps;
	}

	public boolean getIsDaemon() {
		return _isDaemon;
	}

	public int getScWidth() {
		return _scWidth;
	}

	public int getScHeight() {
		return _scHeight;
	}

	public Color getBackColor() {
		return _backColor;
	}

	public int getCvWidth() {
		return _cvWidth;
	}

	public int getCvHeight() {
		return _cvHeight;
	}

	//セッター(setter)
	public void setFps(int value) {
		_fps = value;
	}

	public void setIsDaemon(boolean value) {
		_isDaemon = value;
	}

	public void setScWidth(int value) {
		_scWidth = value;
	}

	public void setScHeight(int value) {
		_scHeight = value;
	}

	public void setBackColor(Color value) {
		_backColor = value;
	}

	public void setCvWidth(int value) {
		_cvWidth = value;
	}

	public void setCvHeight(int value) {
		_cvHeight = value;
	}
}
