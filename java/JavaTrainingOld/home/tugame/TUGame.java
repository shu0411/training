package home.tugame;

public class TUGame extends javax.swing.JApplet
{
	TUPanel	m_tup;
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
		m_tup.setColor( 0xffaa00 );
	}

	public void fillRect(int x, int y, int width, int height){
		m_tup.fillRect(100,100,440,280);
	}

	public void draw(Sprite s) {
		m_tup.draw( s );
	}
}
//Part70まで