package base;

import java.awt.Color;

import javax.swing.JPanel;

public class PanelLibrary{
	/**
	 * パネルを作成し、背景色を設定
	 * @param c 背景色
	 * @return 作成したパネル
	 */
	public static JPanel makePanel( Color c )
	{
		JPanel	jp = new JPanel();
		jp.setBackground( c );
		return( jp );
	}

	/**
	 * 区切り線を表示。
	 * @param jp	表示対象パネル
	 */
	public static void jpHR( JPanel jp )
	{
		JPanel	jpHR = makePanel(Color.WHITE);
		jpHR.setPreferredSize( new java.awt.Dimension( 940,2 ) );
		jp.add( jpHR );
	}

}
