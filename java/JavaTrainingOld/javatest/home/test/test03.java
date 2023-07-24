package home.test;

import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.util.Random;

import home.tugame.Sprite;
import home.tugame.TUGame;
import home.tugame.TUImageChip;

enum	State
{
	TITLE,
	MAIN,
	CLEAR,
	GAMEOVER
	;
}

enum	Fight
{
	APPEAR,
	EXEC,
	WIN,
	NOTFIGHT
	;
}

class MySprite extends Sprite
{
	public final int unit = test03.unit;
	public MySprite( String file, int x, int y, int w, int h ) throws IOException
	{
		super( file , x, y, w, h );
	}

	public int getMapC() {
		return test03.m_tuic.m_map[getMapY() * 640 / unit + getMapX()];
	}

	public int getMapX() {
		return m_x / unit;
	}

	public int getMapY() {
		return m_y / unit;
	}

	//�v���C���[�ړ�
	public void move( int kc )
	{
		if( kc == KeyEvent.VK_RIGHT ){
			m_x += unit;
		}
		if( kc == KeyEvent.VK_LEFT ){
			m_x -= unit;
		}
		if( kc == KeyEvent.VK_UP ){
			m_y -= unit;
		}
		if( kc == KeyEvent.VK_DOWN ){
			m_y += unit;
		}
	}

	//�v���C���[�`��
	@Override public void draw( Graphics g )
	{
		g.drawImage(m_bi, m_x , m_y - 5 , null);
	}
}

abstract class MyWindow{
	private		int		i_WindowColor = 0x88000000;
	private		int		m_x = 40;
	private		int		m_y = 360;
	private		int		m_width = 560;
	private		int		m_height = 80;
	private		int		i_MessageColor = 0xffffff;
	private		int		m_stringX = 50;
	private		int		m_stringY = 392;
	protected	String	sMessage;
	private		TUGame	m_tug;

	public MyWindow(TUGame tug) {
		m_tug = tug;
	}

	public void draw() {
		if( sMessage != null && !sMessage.isEmpty() )
		{	//���b�Z�[�W���e�����݂���ꍇ
			//�X�e�[�^�X�т��쐬
			m_tug.setColor(i_WindowColor, true);
			m_tug.fillRect(m_x, m_y, m_width, m_height);

			//���b�Z�[�W��\��
			m_tug.setGraphicsFontSize(32);
			m_tug.setColor( i_MessageColor );
			m_tug.draw( sMessage ,m_stringX , m_stringY);
		}
	}

	abstract void wmKeyDown(int code);

	public boolean MessageIsExists(){
		if(sMessage != null && !sMessage.isEmpty()){
			return true;
		}
		return false;
	}
}

class MyMessage extends MyWindow{

	public MyMessage(TUGame tug) {
		super(tug);
	}

	public void wmKeyDown(int code) {
		if(code == 10)
		{	//�G���^�[�L�[�������ꂽ�ꍇ
			switch(test03.m_fight) {
				case APPEAR:
					test03.m_fight = Fight.EXEC;
					int iDamage = 3 + test03.r.nextInt(3);
					test03.iHP -= iDamage;
					sMessage = "�G�̍U���I" + Integer.toString(iDamage) + "�̃_���[�W�I�I";
					break;
				case EXEC:
					test03.m_fight = Fight.WIN;
					sMessage = "�G����������I";
					break;
				case WIN:
				default:
					sMessage = null;
					break;
			}
		}
		return;
	}

}

public class test03 extends TUGame
{
	MySprite		m_player;
	static			TUImageChip	m_tuic;
	public static final int	unit = 32;
	State			m_state = State.TITLE;
	static	Fight	m_fight = Fight.NOTFIGHT;
	static	int		iMaxHP = 25;
	static	int		iHP = iMaxHP;
	static	Random	r = new Random();
	MyMessage	myMessage = new MyMessage(this);

	@Override public void wmCreate()
	{
		System.out.println("Look at another window.");

		setBackground( 0x000000 );					//�w�i�F�ύX

		try {
			m_player = new MySprite("cat_resized.png",0,0,32,32);	//�v���C���[�쐬
			m_tuic = new TUImageChip("BaseChip_pipo.png",unit);	//�}�b�v�`�b�v�ǂݍ���
			int chipWidth = 8;
			//�}�b�v�`�b�v�I���ichipWidth*(�ォ�牽�Ԗ� - 1�j+ (�����牽�Ԗ� - 1)
			int g = chipWidth*(1-1)+(1-1);
			int w = chipWidth*(1-1)+(5-1);
			int r = chipWidth*(1-1)+(8-1);
			int f = chipWidth*(9-1)+(5-1);
			int c = chipWidth*(7-1)+(8-1);
			m_tuic.m_map = new int[] {
								f ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,f ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,c ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,w ,w ,w ,w ,w ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,w ,w ,w ,w ,w ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,w ,w ,w ,w ,w ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,w ,w ,w ,w ,w ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,w ,w ,w ,w ,w ,g ,g ,g ,g ,
								g ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,
								f ,g ,g ,r ,r ,r ,r ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,g ,f ,
			};

		} catch (Exception e) {
			System.out.println("���������Ȃ���");
			e.printStackTrace();
		}
	}


	/**
	 * �L�[�����C�x���g
	 */
	@Override public void wmKeyDown(int code)
	{
		System.out.println("�L�[" + code + "�������ꂽ");

		//���b�Z�[�W�̑��݃`�F�b�N
		if(myMessage.MessageIsExists())
		{	//���b�Z�[�W�����݂���ꍇ
			myMessage.wmKeyDown(code);	//���b�Z�[�W�̕\������
			repaint();					//�ĕ`��
			return;						//�㑱�������X�L�b�v
		};

		switch(m_state) {
			case TITLE:
				if(code == 10) {
					m_state = State.MAIN;
					break;
				}
				return;
			case MAIN:
				m_player.move( code );
				if(iHP <= 0)
				{	//HP��0�ȉ���������Q�[���I�[�o�[��ʂ�
					iHP = 0;
					m_state = State.GAMEOVER;
				}
				if(m_player.getMapC() == 8*(7-1)+(8-1))
				{	//�Ԃ̃}�X�Ɉړ�������N���A��ʂ�
					m_state = State.CLEAR;
				}
				if(m_player.getMapC() == 8*(9-1)+(5-1)) {
					iHP = iMaxHP;
					myMessage.sMessage = "HP���񕜂����I";
				}else {
					if( r.nextInt(5) == 0 ) {
						m_fight = Fight.APPEAR;
						myMessage.sMessage = "�G�����ꂽ�I";
					}
				}
				break;
			case GAMEOVER:
			case CLEAR:
				if(code == 10) {
					//HP��߂�
					iHP = iMaxHP;
					//�����ʒu�ɖ߂�
					m_player.m_x = 0;
					m_player.m_y = 0;
					//�Q�[����ʂɖ߂�
					m_state = State.MAIN;
					break;
				}
				return;
			default:
				break;
		}
		repaint();				//paintComponent���ČĂяo��
	}

	/**
	 * �摜�`��
	 */
	@Override public void wmPaint() {

		System.out.println("x=" + m_player.m_x
				+ ",y=" + m_player.m_y
				+ ",mx=" + m_player.getMapX()
				+ ",my=" + m_player.getMapY()
				+ ",mc=" + m_player.getMapC()
				);

		switch (m_state) {
			case TITLE:
				//�^�C�g����ʂ̕\��
				setGraphicsFontSize(64);
				setColor( 0xff4444 );
				draw("NEW GAME",100,100);

				setGraphicsFontSize(32);
				setColor( 0xffffff );
				draw("�����L�[�������Ă�",100,300);
				break;

			case MAIN:
				//�Q�[����ʂ̕\��
				m_tuic.putMapChip(this, 640 / unit, 480 / unit );		//�}�b�v�`��
				draw( m_player );

				//�X�e�[�^�X�т��쐬
				setColor(0x66000000, true);
				fillRect(0,0,640,40);

				//HP�\��
				setGraphicsFontSize(32);
				setColor( 0xffffff );
				draw( "HP : " + Integer.toString(iHP) + "/" + Integer.toString(iMaxHP),
						10, 32);

				//���b�Z�[�W�\��
				myMessage.draw();
				break;

			case CLEAR:
				//�Q�[���N���A��ʂ̕\��
				setColor( 0xffffff );
				setGraphicsFontSize(64);
				draw("GAME CLEAR!",100,100);
				break;

			case GAMEOVER:
				//�Q�[���I�[�o�[��ʂ̕\��
				setColor( 0xffffff );
				setGraphicsFontSize(64);
				draw("GAME OVER!",100,100);
				break;

			default:
				break;
		}
	}

}
//Part100�܂�
