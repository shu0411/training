package swingTest;
//プレーヤーの情報に関するクラス

import javax.swing.JLabel;

public class player
{
	String name;					//変数「名前」の定義
	private int lv;					//変数「レベル」
	private int hp;					//変数「HP」
	private int fullhp;				//変数「最大HP」
	int money;						//変数「所持金」
	
	/**
	 * プレーヤー情報の初期化
	 */
	public player ()
	{
		name = "みん";						//変数「名前」の設定
		lv = 5;								//変数「レベル」
		hp = 30;							//変数「HP」
		fullhp = 30;						//変数「最大HP」
		money = 100;						//変数「所持金」
		
	
	}

	//ステータス表示用関数
	public  String putStatus()
	{
		return( name + "  Lv." + lv + 
		"  HP " + hp + "/" + fullhp + "  " + money + " yen" );
	}
	
	//レベル参照するための関数
	public int getLV(){
		return(lv);
	}
	
		
	//HP参照するための関数
	public int getHP(){
		return(hp);
	}
	
	//最大HP参照するための関数
	public int getFullHP(){
		return(fullhp);
	}
	
	//レベル変更するための関数
	public void setLV(JLabel jl1,int a){
		lv = a;
		jl1.setText(putStatus());
	}

	//HP変更するための関数
	public void setHP(JLabel jl1,int a){
		hp = a;
		jl1.setText(putStatus());
	}
	
	//最大HP変更するための関数
	public void setFullHP(JLabel jl1,int a){
		fullhp = a;
		jl1.setText(putStatus());
	}
}

