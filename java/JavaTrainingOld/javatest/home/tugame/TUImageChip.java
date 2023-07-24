package home.tugame;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class TUImageChip {

	public		int[]		m_map;
	private		Sprite[]	m_chip;
	private		int 		m_size;

	/**
	 * マップチップのコンストラクタ
	 * @param frame	用いるファイル名
	 * @param size
	 * @throws IOException
	 */
	public TUImageChip(String frame, int size) throws IOException
	{
		BufferedImage master = ImageIO.read( new File(frame) );	//ファイル読み込み
		m_size = size;
		int column = master.getWidth() / m_size;
		int row = master.getHeight() / m_size;
		m_chip = new Sprite[column * row];

		for(int i = 0, y = 0; y < row; y++) {
			for(int x= 0; x < column; x++, i++) {
				m_chip[i] = new Sprite(master, x*m_size, y*m_size, m_size, m_size);
			}
		}
	}

	/**
	 * マップの配置
	 * @param tug		TUGameインスタンス
	 * @param width		つくるマップの幅
	 * @param height	作るマップの高さ
	 */
	public void putMapChip(TUGame tug, int width,int height) {
		for (int y = 0; y < height; y++ ) {
			for (int x = 0; x < width; x++) {
				int i = m_map[ y * width + x ] ;
				m_chip[i].m_x = m_size * x;
				m_chip[i].m_y = m_size * y;
				tug.draw( m_chip[i] );
			}
		}
	}
}
