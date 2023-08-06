package swingTest;
import java.awt.Color;
import java.awt.Image;
import java.awt.image.BufferedImage;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.ImageIcon;


public class Library
{
	/**
	 * �p�l�����쐬���A�w�i�F��ݒ�
	 */
	
	static JPanel makePanel( Color c )
	{
		JPanel	jp = new JPanel();
		jp.setBackground( c );
		return( jp );
	}
	
	/**
	 * ��؂����\���B
	 * @param jp	�\���Ώۃp�l��
	 */
	static public void jpHR( JPanel jp )
	{ 
		JPanel	jpHR = Library.makePanel(Color.WHITE);
		jpHR.setPreferredSize( new java.awt.Dimension( 900,2 ) );
		jp.add( jpHR );
	}
	
	/*
	* �����X�^�[�\��
	* @param jp		�\���Ώۃp�l��
	* @param all	�摜�S�̃t�@�C��
	* @param x		�\������Z��X���W
	* @param y		�\������Z��X���W
	*/
	static void putChara(JPanel jp , BufferedImage all, int x, int y)
	{
		int cellw = 24;					//�Z���T�C�Y�E��
		int cellh = 32;					//�Z���T�C�Y�E����
		int sizew = cellw * 5;			//�\���T�C�Y�E��
		int sizeh = cellh * 5;			//�\���T�C�Y�E����
		BufferedImage cell = all.getSubimage(x*cellw, y*cellh, cellw, cellh);	//�摜�؂���
		Image chara = cell.getScaledInstance( sizew , sizeh , Image.SCALE_DEFAULT);
		ImageIcon ii = new ImageIcon( chara );			//JLabel�p�Ɍ^�ϊ�
		JLabel jlImage1 = new JLabel( ii );				//�摜���i���쐬
		jlImage1.setSize( sizew, sizeh );				//���i�T�C�Y��ݒ�
		jp.add( jlImage1 );							//���i��\��t��
	}
}