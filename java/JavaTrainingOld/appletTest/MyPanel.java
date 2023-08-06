package appletTest;

import java.io.File;

import home.tugame.Sprite;
import home.tugame.TUPanel;

//java���ʂ̃N���X
public class MyPanel extends TUPanel
{
	Sprite		m_player;

	public MyPanel()
	{
//		setBackground( Color.BLUE );
		setBackground( 0x0000ff );

//		JLabel jl = new JLabel("Hello World!!!");
//		jl.setFont( new Font(Font.MONOSPACED, Font.BOLD, 40 ));
//		jl.setForeground( Color.WHITE );
//		add( jl );

		try {
			File file = new File("6344152.png");   //�t�@�C�����p
			m_player = new Sprite(file,0,0,36,48); //�L�����؂���
		} catch (Exception e) {
			System.out.println("���������Ȃ���");
			e.printStackTrace();
			//TODO: handle exception
		}
	}

	@Override public void wmKeyDown(int code)
	{
		System.out.println("�L�[" + code + "�������ꂽ!");
		m_player.move( code );
		repaint();				//paintComponent�Ăяo�����ĕ`��
	}

	@Override public void wmPaint() {
		setColor( 0xffaa00 );
		fillRect(100,100,440,280);
		draw( m_player );
	}

}