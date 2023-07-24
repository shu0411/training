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

  //プレイヤー画像選択
	public Sprite( BufferedImage bi )
	{
		m_bi = bi;
	}

  //画像選択(BI指定)
	public Sprite( BufferedImage bi, int x, int y, int w, int h )
	{
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * 画像選択（ファイル指定）
	 * @param file キャラチップファイル
	 * @param x 横方向順番
	 * @param y 縦方向順番
	 * @param w 幅
	 * @param h 高さ
	 * @throws IOException
	 */
	public Sprite( File file, int x, int y, int w, int h ) throws IOException
	{
		BufferedImage bi = ImageIO.read( file );	//画像読込
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * 画像選択（ファイル名指定）
	 * @param file キャラチップファイル
	 * @param x 横方向順番
	 * @param y 縦方向順番
	 * @param w 幅
	 * @param h 高さ
	 * @throws IOException
	 */
	public Sprite( String file, int x, int y, int w, int h ) throws IOException
	{
		BufferedImage bi = ImageIO.read( new File(file) );	//画像読込
		m_bi = bi.getSubimage( x, y, w, h );
	}

	//プレイヤー描画
	public void draw( Graphics g )
	{
		g.drawImage(m_bi, m_x , m_y , null);
	}


}