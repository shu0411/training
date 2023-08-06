package swingTest;

import java.awt.Color;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.ImageIcon;

public class MyFrame extends JFrame
{
	BufferedImage	all;
	JLabel 	jl1;
	JLabel	jlMain;
	JLabel	jlMsg3;
	JPanel	jp2;
	player	Player;
	String 	message;
	boolean main = true; //���C����ʔ���
	
	public MyFrame() throws IOException
	{
		Player = new player();				//�C���X�^���X��
		File file = new File("chara3.png");	//�t�@�C�����p
		all = ImageIO.read( file );			//�摜�Ǎ�
		
		setBounds( 200, 120, 940, 540 );	//�t���[���ʒu�A�T�C�Y�ݒ�
		setDefaultCloseOperation( EXIT_ON_CLOSE );	//�~�{�^���ǉ�
		add( makeBasePanel() );				//�e�p�l�����t���[���ɓ\��t��
		setVisible(true);					//�t���[���\��
		
		enableEvents(java.awt.AWTEvent.KEY_EVENT_MASK);		//�L�[�L����
	}
	
	
	
	/**
	 * �e�p�l���쐬
	 */
	
	JPanel makeBasePanel()
	{
		JPanel	jp0 = Library.makePanel( Color.BLACK );
		
		//���C�A�E�g1�s��
		//�e�p�l���ɃX�e�[�^�X��ʂ�\��
		JPanel	jp1 = Library.makePanel( Color.BLUE );
		jp1.setPreferredSize( new java.awt.Dimension( 940,80 ) );
		jp0.add( jp1 );
		
		//�X�e�[�^�X��ʂɃ��x����\��
		jl1 = new JLabel( Player.putStatus() );
		Font 	f1 = new Font( 	Font.SANS_SERIF, 
								0, 
								50);
		jl1.setFont( f1 );
		jl1.setForeground( Color.WHITE );
		jp1.add( jl1 );
		
		Library.jpHR( jp0 );	//��؂��
		
		//���C�A�E�g2�s��
		//�q�p�l��2��e�p�l���ɕ\��
		jp2 = Library.makePanel ( Color.CYAN );
		jp0.add( jp2 );
		
		
		//�I�������q�p�l��2�ɓ\��t��
		jlMain = new JLabel(
		"<html>1: ����<br>2: �P��<br>3: �x�e");
		jlMain.setFont(f1);
		jp2.add(jlMain);
		
		Library.jpHR( jp0 );	//��؂��
		
		//���C�A�E�g3�s��
		//�e�p�l���Ƀ��x����\��
		message = "�悤����!";
		jlMsg3 = new JLabel(message);
		Font 	f3 = new Font( 	Font.SERIF, 
								Font.ITALIC, 
								40);
		jlMsg3.setFont( f3 );
		jlMsg3.setForeground( Color.YELLOW );
		jp0.add( jlMsg3 );
		
		
		return(jp0);
	}
	

	//�s������
	protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED)
		{
			if(main == true){
				System.out.println("�L�[" + e.getKeyCode() +  "�������ꂽ!");
				if(e.getKeyCode() == KeyEvent.VK_1){
					main = false;
					jlMsg3.setText("�����܂���!!!!!!!!");
					Player = null;
				}
				if(e.getKeyCode() == KeyEvent.VK_2){
					main = false;
					jp2.removeAll();
					Battle();
					System.out.println(main);
				}
				if(e.getKeyCode() == KeyEvent.VK_3){
					main = false;
					if (Player.money >= 10) {
						Player.money -= 10 ;
						Player.setHP(jl1 , Player.getFullHP() );
//						Player.hp = Player.fullhp;
//						jl1.setText(Player.putStatus());
						jlMsg3.setText("<html>zzzzzzzzzzzzzzzzzzzzzzz...<br>"
							+ Player.name + "�̗̑͂�" + Player.getHP() + "�ɂȂ���!!</html>");
					} else {
						jlMsg3.setText( "<html>����������܂���!!<br>�����ɂ͔��܂�܂���!!</html>" );
					}
				}
			} 
			
			if(e.getKeyCode() == KeyEvent.VK_ENTER){
				if (Player == null){
					main = true;
					jlMsg3.setText(
					"Restart!");
					jp2.removeAll();
					jp2.add(jlMain);
					Player = new player();
					jl1.setText(Player.putStatus());
				} else {
					main = true;
					jlMsg3.setText("�������܂����H");
					jp2.removeAll();
					jp2.add(jlMain);
				}
			}
		}
	}
	
	/**
	 * ��������
	 */
	void Battle()
	{
		java.util.Random	r = new java.util.Random();//
		int		enemy = r.nextInt( 8 ) + 1;			//�ϐ� �G�o����
		for( int i=0; i<enemy; i=i+1){
			Library.putChara(jp2,all,0,0);			//�L����1�o��
		}
		
		//hp����
		int		damage = enemy * r.nextInt( 2 ) + 1;
	 	Player.setHP( jl1, Player.getHP() - damage) ;
		
		
		//���b�Z�[�W�ҏW
		message = 
		"<html>�P����!! "+
		Player.name + "��" + enemy + "�C�̓G�ɏo�����<br>"+
		Player.name + "��" + damage + "�̃_���[�W���󂯂��I�I<br>" +
		Player.name + "��HP��" + Player.getHP() + "�ɂȂ����E�E�E�B<br>" ;
		
		//�Q�[���I�[�o�[����
		if (Player.getHP() <= 0) {
			Player.setHP( jl1,0 ) ;
			Player = null;
		}
		try{
			//lv�㏸
			Player.setFullHP( jl1, 15 + Player.getLV() * 3 ) ;
			Player.setLV( jl1,Player.getLV() + 1 );
			message += Player.name + "�́A���x��" + Player.getLV() + "�ɂȂ���!!</html>";
		}catch( NullPointerException e ){
			message += "�Q�[���I�[�o�[!!Enter�L�[�Ń��Z�b�g�B</html>";
		}
		
		//���b�Z�[�W�\��
		jlMsg3.setText (message);
	}
}