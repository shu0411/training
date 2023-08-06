package testGame;

public class Hero {
	String name;
	int hp;
	void sleep() {
		this.hp = 100;
		System.out.println(this.name + "は、眠って回復した！");
	}
	void sit(int sec) {
		this.hp += sec;
		System.out.println(this.name + "は、"+ sec + "秒座って、");
		System.out.println("HPが" + sec + "回復した！");
	}
	void slip() {
		this.hp -= 5;
		System.out.println(this.name + "は、転んで、5のダメージ！");
	}
	void run() {
		this.hp -= 5;
		System.out.println(this.name + "は、逃げた！");
		System.out.println("【GAMEOVER】");
		System.out.println("最終HP：" + this.hp);
	}
}
