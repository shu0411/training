package application;

import static application.Main.*;

import java.util.Random;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Obstacle {
	private float _x; // 矩形のX座標
	private float _y; // 矩形のY座標
	private float _width; // 矩形の幅
	private float _height; // 矩形の高さ
	private Color _color; // 矩形の色

	private float _vx;	//矩形の移動速度
	private boolean exist;	//障害物の存在フラグ

	public void init() {
		setExist(false);
	}

	public void draw(GraphicsContext gc) {
		gc.setFill(getColor());
		gc.fillRect(getX(), getY(), getWidth(), getHeight());
		gc.setStroke(Color.BLACK);
		gc.strokeRect(getX(), getY(), getWidth(), getHeight());
	}

	public void generate() {
		Random random = new Random();	//ランダムインスタンス
		float r;	//ランダム値生成用変数

		setX(WIDTH);	//X座標は画面右端固定

		r = random.nextInt(HEIGHT * 7 / 8);
		setY(r); 		//Y座標を設定

		r = random.nextInt(WIDTH / 8) + WIDTH / 20;
		setWidth(r); // 幅を設定

		r = random.nextInt(HEIGHT  / 12) + HEIGHT / 15;
		setHeight(r); // 高さを設定

		r = (random.nextFloat() + 0.7f) * 1.9f;
		setVx(-r); // 速度を設定

		//RGB値それぞれの値をランダムに指定
		int rR,rG,rB;
		rR = random.nextInt(256);
		rG = random.nextInt(256);
		rB = random.nextInt(256);
		setColor(Color.rgb(rR,rG,rB)); // 色を設定

		setExist(true);
	}

	public void update() {
		setX(getX() + getVx());
		if(getX() + getWidth() < 0) {
			setExist(false);
		}
	}

	//	ゲッター(getter)
	public float getX() {
		return _x;
	}

	public float getY() {
		return _y;
	}

	public float getWidth() {
		return _width;
	}

	public float getHeight() {
		return _height;
	}

	public Color getColor() {
		return _color;
	}

	public float getVx() {
		return _vx;
	}

	public boolean getExist() {
		return exist;
	}

	//	セッター(setter)
	public void setX(float value) {
		_x = value;
	}

	public void setY(float value) {
		_y = value;
	}

	public void setWidth(float value) {
		_width = value;
	}

	public void setHeight(float value) {
		_height = value;
	}

	public void setColor(Color value) {
		_color = value;
	}

	public void setVx(float _vx) {
		this._vx = _vx;
	}

	public void setExist(boolean exist) {
		this.exist = exist;
	}
}
