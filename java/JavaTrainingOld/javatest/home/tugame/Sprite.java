package home.tugame;

import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Sprite
{
	public	BufferedImage   m_bi;
	public	int	m_x;
	public	int	m_y;

  //�v���C���[�摜�I��
	public Sprite( BufferedImage bi )
	{
		m_bi = bi;
	}

  //�摜�I��(BI�w��)
	public Sprite( BufferedImage bi, int x, int y, int w, int h )
	{
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * �摜�I���i�t�@�C���w��j
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
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * �摜�I���i�t�@�C�����w��j
	 * @param file �L�����`�b�v�t�@�C��
	 * @param x ����������
	 * @param y �c��������
	 * @param w ��
	 * @param h ����
	 * @throws IOException
	 */
	public Sprite( String file, int x, int y, int w, int h ) throws IOException
	{
		BufferedImage bi = ImageIO.read( new File(file) );	//�摜�Ǎ�
		m_bi = bi.getSubimage( x, y, w, h );
	}

	//�v���C���[�`��
	public void draw( Graphics g )
	{
		g.drawImage(m_bi, m_x , m_y , null);
	}


}