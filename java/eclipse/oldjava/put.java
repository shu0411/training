package firstTest;


public class put{
	
	
	//�ȉ��A����̏�ʂł̊֐��B
	
	
	/**
	 * ���͂�\��
	 * @param lv	�v���C���[�̃��x��
	 */
	
	public static void Prologue(int lv) {						
		test01.put("�]���r������E�E�E");
		test01.put("���������B");
		test01.put(test01.Player.name + "'s level is " + test01.Player.lv + ".");	//���O�A���x���̊m�F
		test01.put("...");
	}
	
	/**
	 * ���x���グ�R�}���h��\���B
	 * 1�D"battle" �X�g�[���[�i�s
	 * 2�D"develop" ���x���グ
	 * 3�D"rest" HP���ő�HP��
	 */
	public static void Command() throws java.io.IOException{
		Status();									//�X�e�[�^�X��\��
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
	 * ���x���グ�C�x���g�\��
	 */
	public static void Develop() throws java.io.IOException {
		//�G�o��
		java.util.Random	r = new java.util.Random();
		int		enemy = r.nextInt( 4 ) + 1;			//�ϐ� �G�o����
	 	test01.put (test01.Player.name + " encounts " + enemy + " enemies.");
		String m = "�� ";
		String e = "";
		for( int i=0; i<enemy; i=i+1){
			e = e + m;
		}
		test01.put (e);
		
		//hp����
		int		damage = r.nextInt( 2 ) + 1;
	 	test01.Player.hp -= damage ;
		if (test01.Player.hp < 0) {
			test01.Player.hp = 0;
		}
		test01.put (test01.Player.name + " gets " + damage + " damage!");
		test01.put (test01.Player.name + "'s HP becomes " + test01.Player.hp + "...");
		
		//lv�㏸
		test01.Player.lv += enemy ;
		test01.Player.fullhp = 15 + test01.Player.lv * 3 ;
		test01.put (test01.Player.name + "'s level becomes " + test01.Player.lv + "!!");
		
		if (test01.Player.hp > 0) {
			Command();
		}
	}
	
	/**
	 * �x�e�C�x���g�\��
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
	 * �����p�^�[���̕\��
	 * lv100�C80�̑O��ŕ���
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
	 * �����p�^�[���̕\��
	 * lv30�̑O��ŕ���
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
	 * �X�e�[�^�X��\��
	 */
	
	public static void Status()
	{
		test01.put (" ");
		test01.put("-------------------------------");
		test01.put(test01.Player.putStatus());
		test01.put("-------------------------------");
	}
}
	