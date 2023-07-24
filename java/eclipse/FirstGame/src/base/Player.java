package base;
//プレーヤーの情報に関するクラス

import javax.swing.JLabel;

public class Player
{
	private		String	name;		//変数「名前」の定義
	private		int		lv;			//変数「レベル」
	private		int		hp;			//変数「HP」
	private		int		fullhp;		//変数「最大HP」
	private		int		money;		//変数「所持金」

	/**
	 * プレーヤー情報の初期化
	 */
	public Player ()
	{
		name = "みん";				//変数「名前」の設定
		lv = 5;						//変数「レベル」
		hp = 30;					//変数「HP」
		fullhp = 30;				//変数「最大HP」
		money = 100;				//変数「所持金」


	}

	//ステータス表示用関数
	public  String putStatus()
	{
		return( name + "  Lv." + lv +
		"  HP " + hp + "/" + fullhp + "  " + money + " yen" );
	}

	//以下ゲッターとセッター

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getMoney() {
		return money;
	}

	public void setMoney(int money) {
		this.money = money;
	}


	public int getLV(){
		return lv;
	}

	public void setLV(JLabel jl1,int lv){
		this.lv = lv;
		jl1.setText(putStatus());
	}

	public int getHP(){
		return hp;
	}

	public void setHP(JLabel jl1,int hp){
		this.hp = hp;
		jl1.setText(putStatus());
	}

	public int getFullHP(){
		return fullhp;
	}

	public void setFullHP(JLabel jl1,int fullhp){
		this.fullhp = fullhp;
		jl1.setText(putStatus());
	}
}

