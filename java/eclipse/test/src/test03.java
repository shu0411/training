import home.tugame.Sprite;
import home.tugame.TUGame;

public class test03 extends TUGame
{
	Sprite	m_player;
	Sprite	m_other;

	@Override public void wmCreate()
	{
		System.out.println("Look at another window.");

		setBackground( 0x0000ff );					//�w�i�F�ύX

		try {
			m_player = new Sprite("..\\jpg\\6344152.png",1,1,48,48);	//�v���C���[�쐬
			m_other = new Sprite("..\\jpg\\6344152.png",7,1,48,48);
		} catch (Exception e) {
			System.out.println("���������Ȃ���");
			e.printStackTrace();
			//TODO: handle exception
		}
	}

	/**
	 * �L�[�����C�x���g
	 */
	@Override public void wmKeyDown(int code)
	{
		System.out.println("�L�[" + code + "�������ꂽ");
		m_player.move( code );
		repaint();				//paintComponent���ČĂяo��
	}

	/**
	 * �摜�`��
	 */
	@Override public void wmPaint() {
		setColor( 0xffaa00 );
		fillRect(100,100,440,280);
		draw( m_player );
		draw( m_other );
	}

}
//Part70�܂�
