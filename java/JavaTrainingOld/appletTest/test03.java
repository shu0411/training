package appletTest;

import java.io.File;

import home.tugame.Sprite;
import home.tugame.TUGame;

public class test03 extends TUGame
{
	Sprite	m_player;
	Sprite	m_other;

	@Override public void wmCreate()
	{
		System.out.println("Look at another window.");

		setBackground( 0x0000ff );					//?w?i?F????X

		try {
			File file = new File("6344152.png");	//?t?@?C?????p
			m_player = new Sprite(file,1,1,48,48);	//?L?????????
			m_other = new Sprite(file,7,1,48,48);	//?L?????????
		} catch (Exception e) {
			System.out.println("?????????????");
			e.printStackTrace();
			//TODO: handle exception
		}
	}

	/**
	 * ?L?[??????????
	 */
	@Override public void wmKeyDown(int code)
	{
		System.out.println("?L?[" + code + "????????!");
		m_player.move( code );
		repaint();				//paintComponent??????o??????`??
	}

	/**
	 * ???`??
	 */
	@Override public void wmPaint() {
		setColor( 0xffaa00 );
		fillRect(100,100,440,280);
		draw( m_player );
		draw( m_other );
	}

}
//Part70???