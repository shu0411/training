package testGame;

import java.util.Random;

public class Cleric {
	String name;
	int hp = 100;
	final int maxHp = 100;
	int mp = 50;
	final int maxMp = 50;

	void selfAid() {
		System.out.println(this.name + "は、セルフエイドで回復！");
		mp -= 5;
		hp = maxHp;
	}

	int pray(int sec) {
		System.out.println(this.name + "は、" + sec + "秒祈った！");
		int plusMp;
		int actualPlusMp;
		plusMp = sec + new Random().nextInt(3);
		actualPlusMp = Math.min( plusMp , this.maxMp - this.mp );
		this.mp += actualPlusMp ;
		return actualPlusMp;
	}
}
