package firstTest;

public class test01{
	static player 	Player = new player();
	public static void main (String[] args ) throws java.io.IOException {

		put.Prologue( Player.lv );								//?øΩ?øΩ?øΩÕÇÔøΩ\?øΩ?øΩ

		put.Command();									//?øΩR?øΩ}?øΩ?øΩ?øΩh?øΩ?øΩ\?øΩ?øΩ

		if (Player.hp <= 0){
			put("GAME OVER...");
			return;
		}

		if (Player.lv >= 50){								//?øΩo?øΩg?øΩ?øΩ?øΩÃ?øΩ?øΩx?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ
			put.Win();
		} else {
			put.Lose();
		}
	}

	//?øΩ»âÔøΩ?øΩA?øΩƒóp?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ÷êÔøΩ?øΩB

	/**
	 * ?øΩv?øΩ?øΩ?øΩC?øΩ?øΩ?øΩ[?øΩ?øΩ?øΩ?øΩ?øΩÕÇÔøΩ?øΩ?øΩ?øΩL?øΩ[?øΩ?øΩ«Ç›çÔøΩ?øΩﬁÅB
	 * ?øΩ?øΩ?øΩÃç€ÅAEnter?øΩL?øΩ[?øΩÃìÔøΩ?øΩÕÇÕñÔøΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩ?øΩB
	 */
	public static int Select() throws java.io.IOException{
		int c = System.in.read();
		if (c == 10 || c == 13) {
			return (Select());
		} else {
			return (c);
		}
	}

	/**
	 * ?øΩ?øΩ?øΩÕÇÔøΩ\?øΩ?øΩ?øΩ?øΩ?øΩ?øΩB
	 * @param sentense	?øΩ\?øΩ?øΩ?øΩ?øΩ?øΩÈï∂?øΩ?øΩ?øΩ?øΩ
	 */
	public static void put(String sentense) {
		System.out.println(sentense);
	}

}
