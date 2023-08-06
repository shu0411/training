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

  //プレイヤー画像選択
	public Sprite( BufferedImage bi )
	{
		m_bi = bi;
	}

  //プレイヤー画像選択(BI指定)
	public Sprite( BufferedImage bi, int x, int y, int w, int h )
	{
		m_bi = bi.getSubimage( x, y, w, h );
	}

	/**
	 * プレイヤー画像選択（ファイル指定）
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
		int xpx = (x-1)*48 ; //ピクセルに変換
		int ypx = (y-1)*48 ; //ピクセルに変換
		m_bi = bi.getSubimage( xpx, ypx, w, h );
	}

  //プレイヤー描画
	public void draw( Graphics g )
	{
		g.drawImage(m_bi, m_x , m_y , null);
	}

  //プレイヤー移動
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