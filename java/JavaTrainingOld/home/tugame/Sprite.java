package home.tugame;

import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Sprite
{
	BufferedImage   m_bi;
	int			 m_x;
	int			 m_y;

  //�v���C���[�摜�I��
	public Sprite( BufferedImage bi )
	{
		m_bi = bi;
	}

  //�v���C���[�摜�I��(BI�w��)
	public Sprite( BufferedImage bi, int x, int y, int w, int h )
	{
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * �v���C���[�摜�I���i�t�@�C���w��j
	 * @param file �L�����`�b�v�t�@�C��
	 * @param x ����������
	 * @param y �c��������
	 * @param w ��
	 * @param h ����
	 * @throws IOException
	 */
	public Sprite( File file, int x, int y, int w, int h ) throws IOException
	{
		BufferedImage bi = ImageIO.read( file );	//�摜�Ǎ�
		int xpx = (x-1)*48 ; //�s�N�Z���ɕϊ�
		int ypx = (y-1)*48 ; //�s�N�Z���ɕϊ�
		m_bi = bi.getSubimage( xpx, ypx, w, h );
	}

  //�v���C���[�`��
	public void draw( Graphics g )
	{
		g.drawImage(m_bi, m_x , m_y , null);
	}

  //�v���C���[�ړ�
	public void move( int kc )
	{
		if( kc == KeyEvent.VK_RIGHT ){
			m_x += 48;
		}
		if( kc == KeyEvent.VK_LEFT ){
			m_x -= 48;
		}
		if( kc == KeyEvent.VK_UP ){
			m_y -= 48;
		}
		if( kc == KeyEvent.VK_DOWN ){
			m_y += 48;
		}
	}

}