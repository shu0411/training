package home.tugame;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;

import javax.swing.JPanel;

//JApplet固有のクラス
public class TUPanel extends JPanel
{
	public	Graphics	m_g;
	TUGame		m_tug;

	/**
	 * コンストラクタ
	 * @param t
	 */
	public TUPanel( TUGame	tug ){
		m_tug = tug;
	}

	/**
	 *
	 */
	@Override protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED){
			wmKeyDown( e.getKeyCode());
		}
	}

	/**
	 *
	 */
	@Override protected void paintComponent(Graphics g)
	{
		super.paintComponent(g);
		requestFocusInWindow();		//キー有効化
		m_g = g;
		wmPaint();
	}

	/**
	 * キー押下イベント
	 * @param code 呼び出しもとで取得したキーコード
	 */
	public void wmKeyDown(int code)
	{
		m_tug.wmKeyDown(code);
	}

	/**
	 * ペイントメソッド（背景色、長方形、キャラ描画）
	 */
	public void wmPaint() {
		m_tug.wmPaint();
	}

	/**
	 * 長方形描画
	 * @param x x座標
	 * @param y y座標
	 * @param width 幅
	 * @param height 高さ
	 */
	public void fillRect(int x, int y, int width, int height){
		m_g.fillRect(x, y, width, height);
	}

	/**
	 * キャラ描画
	 * @param s キャラチップ
	 */
	public void draw(Sprite s) {
		s.draw( m_g );
	}

	public void draw(String str, int x, int y) {
		m_g.drawString(str,x,y);
	}

	/**
	 * 背景色指定
	 * @param rgb RGB値
	 */
	public void setBackground(int rgb) {
		setBackground( new Color(rgb) );
	}

	/**
	 * メイン色指定
	 * @param rgb RGB値
	 */
	public void setColor(int rgb) {
		m_g.setColor( new Color(rgb));
	}

	public void setColor(int argb, boolean hasalpha) {
		m_g.setColor( new Color(argb, hasalpha));
	}

	public void setGraphicsFont(Font font) {
		m_g.setFont(font);
	}

	public void setGraphicsFontSize(int size) {
		Font	font = new Font(Font.DIALOG, Font.PLAIN, size);
		setGraphicsFont(font);
	}

}