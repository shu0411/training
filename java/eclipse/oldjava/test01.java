package firstTest;

public class test01{
	static player 	Player = new player();
	public static void main (String[] args ) throws java.io.IOException {

		put.Prologue( Player.lv );								//?��?��?��͂�\?��?��

		put.Command();									//?��R?��}?��?��?��h?��?��\?��?��

		if (Player.hp <= 0){
			put("GAME OVER...");
			return;
		}

		if (Player.lv >= 50){								//?��o?��g?��?��?���?��?��x?��?��?��?��?��?��
			put.Win();
		} else {
			put.Lose();
		}
	}

	//?��ȉ�?��A?��ėp?��?��?��?��?��?��?��?��?��֐�?��B

	/**
	 * ?��v?��?��?��C?��?��?��[?��?��?��?��?��͂�?��?��?��L?��[?��?��ǂݍ�?��ށB
	 * ?��?��?��̍ہAEnter?��L?��[?��̓�?��͖͂�?��?��?��?��?��?��?��B
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
	 * ?��?��?��͂�\?��?��?��?��?��?��B
	 * @param sentense	?��\?��?��?��?��?��镶?��?��?��?��
	 */
	public static void put(String sentense) {
		System.out.println(sentense);
	}

}
