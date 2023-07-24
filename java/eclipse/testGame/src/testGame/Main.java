package testGame;

public class Main {

	public static void main(String[] args) {
		//勇者登場
		Hero hero1 = new Hero();
		hero1.name = "たけし";
		hero1.hp = 100;
		System.out.println(hero1.name + "が登場！");

		//敵登場
		Enemy enemy1 = new Enemy();

		//座ったり転んだり逃げたり
		hero1.sit(5);
		hero1.slip();
		hero1.sit(25);
		hero1.run();
		//戦う

		Cleric cleric1 = new Cleric();
		cleric1.name = "test";
		cleric1.hp = 50;
		cleric1.mp = 20;
		System.out.println(cleric1.name + "が登場！");
		System.out.println("HP:" + cleric1.hp + "/MP:" + cleric1.mp);
		cleric1.selfAid();
		System.out.println("HP:" + cleric1.hp + "/MP:" + cleric1.mp);

		int plus;
		plus = cleric1.pray(2);
		System.out.println(cleric1.name + "は、祈ってMPを" + plus + "回復！");
		System.out.println("HP:" + cleric1.hp + "/MP:" + cleric1.mp);

		plus = cleric1.pray(2);
		System.out.println(cleric1.name + "は、祈ってMPを" + plus + "回復！");
		System.out.println("HP:" + cleric1.hp + "/MP:" + cleric1.mp);
		//敵逃げる
	}

}
