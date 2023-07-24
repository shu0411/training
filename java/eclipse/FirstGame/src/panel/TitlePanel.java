package panel;

import java.awt.Color;
import java.awt.Font;
import java.awt.event.KeyEvent;

import javax.swing.JLabel;

import base.MyPanel;
import enums.WindowMode;
import main.MainFrame;

public class TitlePanel extends MyPanel {

	public TitlePanel(MainFrame mf) {
		super(mf);
		JLabel jl1 = new JLabel( "Hello World!" );
		Font 	f1 = new Font( 	Font.SANS_SERIF,
								0,
								50);
		jl1.setFont( f1 );
		jl1.setForeground( Color.WHITE );
		this.add( jl1 );
	}

	//行動処理
	@Override protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED )
		{
			System.out.println("キー" + e.getKeyCode() +  "が押された!");
			PanelChange(WindowMode.BATTLE);
		}
	}



}
