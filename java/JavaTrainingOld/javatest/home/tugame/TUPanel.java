package home.tugame;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;

import javax.swing.JPanel;

//JApplet�ŗL�̃N���X
public class TUPanel extends JPanel
{
	public	Graphics	m_g;
	TUGame		m_tug;

	/**
	 * �R���X�g���N�^
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
		requestFocusInWindow();		//�L�[�L����
		m_g = g;
		wmPaint();
	}

	/**
	 * �L�[�����C�x���g
	 * @param code �Ăяo�����ƂŎ擾�����L�[�R�[�h
	 */
	public void wmKeyDown(int code)
	{
		m_tug.wmKeyDown(code);
	}

	/**
	 * �y�C���g���\�b�h�i�w�i�F�A�����`�A�L�����`��j
	 */
	public void wmPaint() {
		m_tug.wmPaint();
	}

	/**
	 * �����`�`��
	 * @param x x���W
	 * @param y y���W
	 * @param width ��
	 * @param height ����
	 */
	public void fillRect(int x, int y, int width, int height){
		m_g.fillRect(x, y, width, height);
	}

	/**
	 * �L�����`��
	 * @param s �L�����`�b�v
	 */
	public void draw(Sprite s) {
		s.draw( m_g );
	}

	public void draw(String str, int x, int y) {
		m_g.drawString(str,x,y);
	}

	/**
	 * �w�i�F�w��
	 * @param rgb RGB�l
	 */
	public void setBackground(int rgb) {
		setBackground( new Color(rgb) );
	}

	/**
	 * ���C���F�w��
	 * @param rgb RGB�l
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