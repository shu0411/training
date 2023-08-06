package base;

import java.awt.Image;
import java.awt.image.BufferedImage;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;


public class Library
{
	/*
	* モンスター表示
	* @param jp		表示対象パネル
	* @param all	画像全体ファイル
	* @param x		表示するセルX座標
	* @param y		表示するセルX座標
	*/
	public static void putChara(JPanel jp , BufferedImage all, int x, int y)
	{
		int cellw = 24;					//セルサイズ・幅
		int cellh = 32;					//セルサイズ・高さ
		int sizew = cellw * 5;			//表示サイズ・幅
		int sizeh = cellh * 5;			//表示サイズ・高さ
		BufferedImage cell = all.getSubimage(x*cellw, y*cellh, cellw, cellh);	//画像切り取り
		Image chara = cell.getScaledInstance( sizew , sizeh , Image.SCALE_DEFAULT);
		ImageIcon ii = new ImageIcon( chara );			//JLabel用に型変換
		JLabel jlImage1 = new JLabel( ii );				//画像部品を作成
		jlImage1.setSize( sizew, sizeh );				//部品サイズを設定
		jp.add( jlImage1 );							//部品を貼り付け
	}
}