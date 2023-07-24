import home.tugame.Sprite;
import home.tugame.TUGame;

public class test03 extends TUGame
{
	Sprite	m_player;
	Sprite	m_other;

	@Override public void wmCreate()
	{
		System.out.println("Look at another window.");

		setBackground( 0x0000ff );					//背景色変更

		try {
			m_player = new Sprite("..\\jpg\\6344152.png",1,1,48,48);	//プレイヤー作成
			m_other = new Sprite("..\\jpg\\6344152.png",7,1,48,48);
		} catch (Exception e) {
			System.out.println("がぞうがないよ");
			e.printStackTrace();
			//TODO: handle exception
		}
	}

	/**
	 * キー押下イベント
	 */
	@Override public void wmKeyDown(int code)
	{
		System.out.println("キー" + code + "が押された");
		m_player.move( code );
		repaint();				//paintComponentを再呼び出し
	}

	/**
	 * 画像描画
	 */
	@Override public void wmPaint() {
		setColor( 0xffaa00 );
		fillRect(100,100,440,280);
		draw( m_player );
		draw( m_other );
	}

}
//Part70まで
