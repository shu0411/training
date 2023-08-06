package application;

import static application.Main.*;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;

public class Player {
	static final int R = 16;

	private float _x;	//プレイヤーのX座標
	private float _y;	//プレイヤーのY座標

	private float _vx; // プレイヤーの速度
	private float _vy; // プレイヤーの速度
	private float _jump; // ジャンプ時の速度
//	private float _m; // プレイヤーの重さ ※本当は落下速度の計算に重さは不要

	public void init() {
		setX(WIDTH / 4);
		setY(HEIGHT / 4);

		setJump(JUMP);
//		setM(M);
	}

	public void draw(GraphicsContext gc) {
		gc.setFill(Color.LIME);
		gc.fillOval(getX() - R, getY() - R, R * 2, R * 2);
		gc.setStroke(Color.BLACK);
		gc.strokeOval(getX() - R, getY() - R, R * 2, R * 2);
	}

	public void update() {
		//上の壁に当たったら跳ね返り
 		if(getY() < 16) {
			setY(16);
			setVy(2.0f);
			Key[KEY_SPACE] = -5;
		}

		//下の壁に当たったらその場に止まる
		if(getY() > HEIGHT - 16) {
			setY(HEIGHT - 16);
			setVy(getVy() * BOUND);
		}

		//スペースキーを押したら速度にジャンプ速度を加える
		if(Key[KEY_SPACE] >= 1) {
			setVy( getJump());
			Key[KEY_SPACE]++;
		}


//		setVy(getVy() + getM() * GRAVITY);	//重力の加算
		setVy(getVy() + GRAVITY);	//重力の加算

		setY(getY() + getVy());		//プレイヤーのY座標を変える

/*
		if(Key[KEY_LEFT] >= 1) {
			setVx(-5);
		}
		else if(Key[KEY_RIGHT] >= 1) {
			setVx(5);
		}else {
			setVx(0);
		}
		if(Key[KEY_UP] >= 1) {
			setVy(-5);
		}
		else if(Key[KEY_DOWN] >= 1) {
			setVy(5);
		}else {
			setVy(0);
		}
		setX(getX() + getVx());		//プレイヤーのX座標を変える
		setY(getY() + getVy());		//プレイヤーのY座標を変える
*/

	}

	//getter
	public float getX() {
		return _x;
	}

	public float getY() {
		return _y;
	}

	public float getVx() {
		return _vx;
	}

	public float getVy() {
		return _vy;
	}

	public float getJump() {
		return _jump;
	}

//	public float getM() {
//		return _m;
//	}

	//setter
	public void setX(float _x) {
		this._x = _x;
	}

	public void setY(float _y) {
		this._y = _y;
	}

	public void setVx(float _vx) {
		this._vx = _vx;
	}

	public void setVy(float _vy) {
		this._vy = _vy;
	}

	public void setJump(float _jump) {
		this._jump = _jump;
	}

//	public void setM(float _m) {
//		this._m = _m;
//	}



}
