package panel;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JLabel;
import javax.swing.JPanel;

import base.Library;
import base.MyPanel;
import base.PanelLibrary;
import base.Player;
import enums.WindowMode;
import main.MainFrame;

public class BattlePanel extends MyPanel {

	Player	player= new Player();
	BufferedImage	all;
	JLabel 	jl1;
	JLabel	jlMain;
	JLabel	jlMsg3;
	JPanel	jp2;
	String	message;

	public BattlePanel(MainFrame mf) {
		super(mf);
		player = new Player();				//インスタンス化
		File file = new File("img/chara3.png");	//ファイル引用
		try {
			all = ImageIO.read( file );
		} catch (IOException e) {
			e.printStackTrace();
		}			//画像読込

		this.setBackground(Color.BLACK);
		//レイアウト1行目
		this.setPreferredSize( new java.awt.Dimension( 940, 540 ) );

		//親パネルにステータス画面を表示
		JPanel	jp1 = PanelLibrary.makePanel( Color.BLUE );
		jp1.setPreferredSize( new java.awt.Dimension( 940,80 ) );
		this.add( jp1 );

		//ステータス画面にラベルを表示
		jl1 = new JLabel(player.putStatus() );
		Font 	f1 = new Font( 	Font.SANS_SERIF,
								0,
								50);
		jl1.setFont( f1 );
		jl1.setForeground( Color.WHITE );
		jp1.add( jl1 );

		PanelLibrary.jpHR( this );	//区切り線

		//レイアウト2行目
		//子パネル2を親パネルに表示
		jp2 = PanelLibrary.makePanel ( Color.CYAN );
		this.add( jp2 );


		//選択肢を子パネル2に貼り付け
		jlMain = new JLabel(
		"<html>1: 挑戦<br>2: 訓練<br>3: 休憩");
		jlMain.setFont(f1);
		jp2.add(jlMain);

		PanelLibrary.jpHR( this );	//区切り線

		//レイアウト3行目
		//親パネルにラベルを表示
		message = "ようこそ!";
		jlMsg3 = new JLabel(message);
		Font 	f3 = new Font( 	Font.SERIF,
								Font.ITALIC,
								40);
		jlMsg3.setFont( f3 );
		jlMsg3.setForeground( Color.YELLOW );
		this.add( jlMsg3 );
	}


	Boolean isMenu = true;
	@Override protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED )
		{
			System.out.println("キー" + e.getKeyCode() +  "が押された!");
			if(mainFrame.windowMode == WindowMode.BATTLE) {
				if(isMenu) {
					switch(e.getKeyCode() ) {
						case KeyEvent.VK_1:
							isMenu = false;
							jlMsg3.setText("勝ちました!!!!!!!!");
							player = null;
							break;
						case KeyEvent.VK_2:
							isMenu = false;
							jp2.removeAll();
							Battle();
							break;
						case KeyEvent.VK_3:
							isMenu = false;
							Rest();
							break;
						case KeyEvent.VK_9:
							if (player != null){
								player = null;
							}
							PanelChange(WindowMode.TITLE);
					}
				}else {
					if(e.getKeyCode()  == KeyEvent.VK_ENTER){
						isMenu = true;
						if (player == null){
							jlMsg3.setText(
							"Restart!");
							jp2.removeAll();
							jp2.add(jlMain);
							player = new Player();
							jl1.setText(player.putStatus());
						} else {
							jlMsg3.setText("何をしますか？");
							jp2.removeAll();
							jp2.add(jlMain);
						}
					}
				}
			}
		}
	}

	/**
	 * 戦闘処理
	 */
	void Battle()
	{
		java.util.Random	r = new java.util.Random();//
		int		enemy = r.nextInt( 8 ) + 1;			//変数 敵出現数
		for( int i=0; i<enemy; i=i+1){
			Library.putChara(jp2,all,0,0);			//キャラ1出現
		}

		//hp減少
		int		damage = enemy * r.nextInt( 2 ) + 1;
		player.setHP( jl1, player.getHP() - damage) ;


		//メッセージ編集
		message =
		"<html>訓練だ!! "+
				player.getName() + "は" + enemy + "匹の敵に出会った<br>"+
				player.getName() + "は" + damage + "のダメージを受けた！！<br>" +
				player.getName() + "のHPは" + player.getHP() + "になった・・・。<br>" ;

		//ゲームオーバー処理
		if (player.getHP() <= 0) {
			player.setHP( jl1,0 ) ;
			player = null;
		}
		try{
			//lv上昇
			player.setFullHP( jl1, 15 + player.getLV() * 3 ) ;
			player.setLV( jl1, player.getLV() + 1 );
			message += player.getName() + "は、レベル" + player.getLV() + "になった!!</html>";
		}catch( NullPointerException e ){
			message += "ゲームオーバー!!Enterキーでリセット。</html>";
		}

		//メッセージ表示
		jlMsg3.setText (message);
	}

	/**
	 * 休憩処理
	 */
	void Rest(){
		if (player.getMoney() >= 10) {
			player.setMoney(player.getMoney() - 10) ;
			player.setHP(jl1 , player.getFullHP() );
			jlMsg3.setText("<html>zzzzzzzzzzzzzzzzzzzzzzz...<br>"
				+ player.getName() + "の体力は" + player.getHP() + "になった!!</html>");
		} else {
			jlMsg3.setText( "<html>お金が足りません!!<br>ここには泊まれません!!</html>" );
		}
	}

}
