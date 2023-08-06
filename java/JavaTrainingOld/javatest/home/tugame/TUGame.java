package home.tugame;

import java.awt.Font;

public class TUGame extends javax.swing.JApplet
{
	public TUPanel	m_tup;

	public void init()
	{
		m_tup = new TUPanel( this );
		getContentPane().add( m_tup );
		wmCreate();
	}

	public void wmCreate() {
	}

	public void wmKeyDown(int code){
	}

	public void wmPaint() {
	}

	public void setBackground( int rgb ) {
		m_tup.setBackground(rgb);
	}

	public void setColor(int rgb) {
		m_tup.setColor( rgb );
	}

	public void setColor(int argb, boolean hasalpha) {
		m_tup.setColor( argb, hasalpha );
	}

	public void setGraphicsFont( Font font ) {
		m_tup.setGraphicsFont(font);
	}

	public void setGraphicsFontSize(int size ) {
		m_tup.setGraphicsFontSize(size);
	}

	public void fillRect(int x, int y, int width, int height){
		m_tup.fillRect(x, y, width, height);
	}

	public void draw(Sprite s) {
		m_tup.draw( s );
	}

	public void draw(String str, int x, int y) {
		m_tup.draw( str, x, y );
	}
}
//Part70まで