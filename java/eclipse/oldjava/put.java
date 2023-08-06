package firstTest;


public class put{
	
	
	//以下、特定の場面での関数。
	
	
	/**
	 * 序章を表示
	 * @param lv	プレイヤーのレベル
	 */
	
	public static void Prologue(int lv) {						
		test01.put("ゾンビがいる・・・");
		test01.put("強そうだ。");
		test01.put(test01.Player.name + "'s level is " + test01.Player.lv + ".");	//名前、レベルの確認
		test01.put("...");
	}
	
	/**
	 * レベル上げコマンドを表示。
	 * 1．"battle" ストーリー進行
	 * 2．"develop" レベル上げ
	 * 3．"rest" HPを最大HPに
	 */
	public static void Command() throws java.io.IOException{
		Status();									//ステータスを表示
		test01.put( "1: battle" );
		test01.put( "2: develop" );
		test01.put( "3: rest");
		switch (test01.Select()){
			case '1':{				break;	}
			case '2':{	Develop();	break;	}
			case '3':{	Rest();		break;	}
			default :{
				test01.put ("Press right key!!");
				Command();
			}
			
		}
	}

	/**
	 * レベル上げイベント表示
	 */
	public static void Develop() throws java.io.IOException {
		//敵出現
		java.util.Random	r = new java.util.Random();
		int		enemy = r.nextInt( 4 ) + 1;			//変数 敵出現数
	 	test01.put (test01.Player.name + " encounts " + enemy + " enemies.");
		String m = "● ";
		String e = "";
		for( int i=0; i<enemy; i=i+1){
			e = e + m;
		}
		test01.put (e);
		
		//hp減少
		int		damage = r.nextInt( 2 ) + 1;
	 	test01.Player.hp -= damage ;
		if (test01.Player.hp < 0) {
			test01.Player.hp = 0;
		}
		test01.put (test01.Player.name + " gets " + damage + " damage!");
		test01.put (test01.Player.name + "'s HP becomes " + test01.Player.hp + "...");
		
		//lv上昇
		test01.Player.lv += enemy ;
		test01.Player.fullhp = 15 + test01.Player.lv * 3 ;
		test01.put (test01.Player.name + "'s level becomes " + test01.Player.lv + "!!");
		
		if (test01.Player.hp > 0) {
			Command();
		}
	}
	
	/**
	 * 休憩イベント表示
	 */
	public static void Rest() throws java.io.IOException {
		if (test01.Player.money >= 10) {
			test01.Player.money -= 10 ;
			test01.Player.hp = test01.Player.fullhp;
			test01.put (test01.Player.name + "'s HP becomes " + test01.Player.hp + "!!");
		} else {
			test01.put( "You don't have enough money!!" );
			test01.put( "You can't stay here!!" );
		}
		Command();
	}
	
	/**
	 * 勝ちパターンの表示
	 * lv100，80の前後で分岐
	 */
	public static void Win() {							
		System.out.println(test01.Player.name + " beats Zombie.");
			if (test01.Player.lv >= 100){
				test01.put("It's very easy!!");
			} else if (test01.Player.lv >= 80) {
				test01.put("It's easy!");
			} else {
				test01.put("It's a little hard!");
			}
		test01.put("GAME CLEAR!!!!!");
	}
		
	/**
	 * 負けパターンの表示
	 * lv30の前後で分岐
	 */
	public static void Lose() {
		test01.put(test01.Player.name + " can't beat Zombie.");
			if (test01.Player.lv >= 30){
				test01.put(test01.Player.name + " is a little weak...");
			} else {
				test01.put(test01.Player.name + " is too weak......");
			}
		test01.put("GAME OVER...");	
	}
	
	
	/**
	 * ステータスを表示
	 */
	
	public static void Status()
	{
		test01.put (" ");
		test01.put("-------------------------------");
		test01.put(test01.Player.putStatus());
		test01.put("-------------------------------");
	}
}
	