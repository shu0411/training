package swingTest;
//�v���[���[�̏��Ɋւ���N���X

import javax.swing.JLabel;

public class player
{
	String name;					//�ϐ��u���O�v�̒�`
	private int lv;					//�ϐ��u���x���v
	private int hp;					//�ϐ��uHP�v
	private int fullhp;				//�ϐ��u�ő�HP�v
	int money;						//�ϐ��u�������v
	
	/**
	 * �v���[���[���̏�����
	 */
	public player ()
	{
		name = "�݂�";						//�ϐ��u���O�v�̐ݒ�
		lv = 5;								//�ϐ��u���x���v
		hp = 30;							//�ϐ��uHP�v
		fullhp = 30;						//�ϐ��u�ő�HP�v
		money = 100;						//�ϐ��u�������v
		
	
	}

	//�X�e�[�^�X�\���p�֐�
	public  String putStatus()
	{
		return( name + "  Lv." + lv + 
		"  HP " + hp + "/" + fullhp + "  " + money + " yen" );
	}
	
	//���x���Q�Ƃ��邽�߂̊֐�
	public int getLV(){
		return(lv);
	}
	
		
	//HP�Q�Ƃ��邽�߂̊֐�
	public int getHP(){
		return(hp);
	}
	
	//�ő�HP�Q�Ƃ��邽�߂̊֐�
	public int getFullHP(){
		return(fullhp);
	}
	
	//���x���ύX���邽�߂̊֐�
	public void setLV(JLabel jl1,int a){
		lv = a;
		jl1.setText(putStatus());
	}

	//HP�ύX���邽�߂̊֐�
	public void setHP(JLabel jl1,int a){
		hp = a;
		jl1.setText(putStatus());
	}
	
	//�ő�HP�ύX���邽�߂̊֐�
	public void setFullHP(JLabel jl1,int a){
		fullhp = a;
		jl1.setText(putStatus());
	}
}

