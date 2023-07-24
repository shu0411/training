package swingTest;

import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.ImageIcon;

public class MyFrame extends JFrame
{
	BufferedImage	all;
	JLabel 	jl1;
	JLabel	jlMain;
	JLabel	jlMsg3;
	JPanel	jp2;
	player	Player;
	String 	message;
	boolean main = true; //メイン画面判定
	
	public MyFrame() throws IOException
	{
		Player = new player();				//インスタンス化
		File file = new File("chara3.png");	//ファイル引用
		all = ImageIO.read( file );			//画像読込
		
		setBounds( 200, 120, 940, 540 );	//フレーム位置、サイズ設定
		setDefaultCloseOperation( EXIT_ON_CLOSE );	//×ボタン追加
		add( makeBasePanel() );				//親パネルをフレームに貼り付け
		setVisible(true);					//フレーム表示
		
		enableEvents(java.awt.AWTEvent.KEY_EVENT_MASK);		//キー有効化
	}
	
	
	
	/**
	 * 親パネル作成
	 */
	
	JPanel makeBasePanel()
	{
		JPanel	jp0 = Library.makePanel( Color.BLACK );
		
		//レイアウト1行目
		//親パネルにステータス画面を表示
		JPanel	jp1 = Library.makePanel( Color.BLUE );
		jp1.setPreferredSize( new java.awt.Dimension( 940,80 ) );
		jp0.add( jp1 );
		
		//ステータス画面にラベルを表示
		jl1 = new JLabel( Player.putStatus() );
		Font 	f1 = new Font( 	Font.SANS_SERIF, 
								0, 
								50);
		jl1.setFont( f1 );
		jl1.setForeground( Color.WHITE );
		jp1.add( jl1 );
		
		Library.jpHR( jp0 );	//区切り線
		
		//レイアウト2行目
		//子パネル2を親パネルに表示
		jp2 = Library.makePanel ( Color.CYAN );
		jp0.add( jp2 );
		
		
		//選択肢を子パネル2に貼り付け
		jlMain = new JLabel(
		"<html>1: 挑戦<br>2: 訓練<br>3: 休憩");
		jlMain.setFont(f1);
		jp2.add(jlMain);
		
		Library.jpHR( jp0 );	//区切り線
		
		//レイアウト3行目
		//親パネルにラベルを表示
		message = "ようこそ!";
		jlMsg3 = new JLabel(message);
		Font 	f3 = new Font( 	Font.SERIF, 
								Font.ITALIC, 
								40);
		jlMsg3.setFont( f3 );
		jlMsg3.setForeground( Color.YELLOW );
		jp0.add( jlMsg3 );
		
		
		return(jp0);
	}
	

	//行動処理
	protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED)
		{
			if(main == true){
				System.out.println("キー" + e.getKeyCode() +  "が押された!");
				if(e.getKeyCode() == KeyEvent.VK_1){
					main = false;
					jlMsg3.setText("勝ちました!!!!!!!!");
					Player = null;
				}
				if(e.getKeyCode() == KeyEvent.VK_2){
					main = false;
					jp2.removeAll();
					Battle();
					System.out.println(main);
				}
				if(e.getKeyCode() == KeyEvent.VK_3){
					main = false;
					if (Player.money >= 10) {
						Player.money -= 10 ;
						Player.setHP(jl1 , Player.getFullHP() );
//						Player.hp = Player.fullhp;
//						jl1.setText(Player.putStatus());
						jlMsg3.setText("<html>zzzzzzzzzzzzzzzzzzzzzzz...<br>"
							+ Player.name + "の体力は" + Player.getHP() + "になった!!</html>");
					} else {
						jlMsg3.setText( "<html>お金が足りません!!<br>ここには泊まれません!!</html>" );
					}
				}
			} 
			
			if(e.getKeyCode() == KeyEvent.VK_ENTER){
				if (Player == null){
					main = true;
					jlMsg3.setText(
					"Restart!");
					jp2.removeAll();
					jp2.add(jlMain);
					Player = new player();
					jl1.setText(Player.putStatus());
				} else {
					main = true;
					jlMsg3.setText("何をしますか？");
					jp2.removeAll();
					jp2.add(jlMain);
				}
			}
		}
	}
	
	/**
	 * たたかい
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
	 	Player.setHP( jl1, Player.getHP() - damage) ;
		
		
		//メッセージ編集
		message = 
		"<html>訓練だ!! "+
		Player.name + "は" + enemy + "匹の敵に出会った<br>"+
		Player.name + "は" + damage + "のダメージを受けた！！<br>" +
		Player.name + "のHPは" + Player.getHP() + "になった・・・。<br>" ;
		
		//ゲームオーバー処理
		if (Player.getHP() <= 0) {
			Player.setHP( jl1,0 ) ;
			Player = null;
		}
		try{
			//lv上昇
			Player.setFullHP( jl1, 15 + Player.getLV() * 3 ) ;
			Player.setLV( jl1,Player.getLV() + 1 );
			message += Player.name + "は、レベル" + Player.getLV() + "になった!!</html>";
		}catch( NullPointerException e ){
			message += "ゲームオーバー!!Enterキーでリセット。</html>";
		}
		
		//メッセージ表示
		jlMsg3.setText (message);
	}
}