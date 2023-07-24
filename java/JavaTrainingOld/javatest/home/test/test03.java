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

	//プレイヤー移動
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

	//プレイヤー描画
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
		{	//メッセージ内容が存在する場合
			//ステータス帯を作成
			m_tug.setColor(i_WindowColor, true);
			m_tug.fillRect(m_x, m_y, m_width, m_height);

			//メッセージを表示
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
		{	//エンターキーが押された場合
			switch(test03.m_fight) {
				case APPEAR:
					test03.m_fight = Fight.EXEC;
					int iDamage = 3 + test03.r.nextInt(3);
					test03.iHP -= iDamage;
					sMessage = "敵の攻撃！" + Integer.toString(iDamage) + "のダメージ！！";
					break;
				case EXEC:
					test03.m_fight = Fight.WIN;
					sMessage = "敵をやっつけた！";
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

		setBackground( 0x000000 );					//背景色変更

		try {
			m_player = new MySprite("cat_resized.png",0,0,32,32);	//プレイヤー作成
			m_tuic = new TUImageChip("BaseChip_pipo.png",unit);	//マップチップ読み込み
			int chipWidth = 8;
			//マップチップ選択（chipWidth*(上から何番目 - 1）+ (左から何番目 - 1)
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
			System.out.println("がぞうがないよ");
			e.printStackTrace();
		}
	}


	/**
	 * キー押下イベント
	 */
	@Override public void wmKeyDown(int code)
	{
		System.out.println("キー" + code + "が押された");

		//メッセージの存在チェック
		if(myMessage.MessageIsExists())
		{	//メッセージが存在する場合
			myMessage.wmKeyDown(code);	//メッセージの表示処理
			repaint();					//再描画
			return;						//後続処理をスキップ
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
				{	//HPが0以下だったらゲームオーバー画面に
					iHP = 0;
					m_state = State.GAMEOVER;
				}
				if(m_player.getMapC() == 8*(7-1)+(8-1))
				{	//花のマスに移動したらクリア画面に
					m_state = State.CLEAR;
				}
				if(m_player.getMapC() == 8*(9-1)+(5-1)) {
					iHP = iMaxHP;
					myMessage.sMessage = "HPが回復した！";
				}else {
					if( r.nextInt(5) == 0 ) {
						m_fight = Fight.APPEAR;
						myMessage.sMessage = "敵が現れた！";
					}
				}
				break;
			case GAMEOVER:
			case CLEAR:
				if(code == 10) {
					//HPを戻す
					iHP = iMaxHP;
					//初期位置に戻す
					m_player.m_x = 0;
					m_player.m_y = 0;
					//ゲーム画面に戻す
					m_state = State.MAIN;
					break;
				}
				return;
			default:
				break;
		}
		repaint();				//paintComponentを再呼び出し
	}

	/**
	 * 画像描画
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
				//タイトル画面の表示
				setGraphicsFontSize(64);
				setColor( 0xff4444 );
				draw("NEW GAME",100,100);

				setGraphicsFontSize(32);
				setColor( 0xffffff );
				draw("何かキーを押してね",100,300);
				break;

			case MAIN:
				//ゲーム画面の表示
				m_tuic.putMapChip(this, 640 / unit, 480 / unit );		//マップ描画
				draw( m_player );

				//ステータス帯を作成
				setColor(0x66000000, true);
				fillRect(0,0,640,40);

				//HP表示
				setGraphicsFontSize(32);
				setColor( 0xffffff );
				draw( "HP : " + Integer.toString(iHP) + "/" + Integer.toString(iMaxHP),
						10, 32);

				//メッセージ表示
				myMessage.draw();
				break;

			case CLEAR:
				//ゲームクリア画面の表示
				setColor( 0xffffff );
				setGraphicsFontSize(64);
				draw("GAME CLEAR!",100,100);
				break;

			case GAMEOVER:
				//ゲームオーバー画面の表示
				setColor( 0xffffff );
				setGraphicsFontSize(64);
				draw("GAME OVER!",100,100);
				break;

			default:
				break;
		}
	}

}
//Part100まで
