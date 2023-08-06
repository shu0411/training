package base;

import java.awt.Color;
import java.awt.event.KeyEvent;

import javax.swing.JPanel;

import enums.WindowMode;
import main.MainFrame;

public abstract class MyPanel extends JPanel {
	protected	MainFrame	mainFrame;

	public MyPanel() {
		super();
	}

	public MyPanel(MainFrame mf) {
		mainFrame = mf;
		setBackground(Color.black);
		setPreferredSize( new java.awt.Dimension( 940,540 ) );
		enableEvents(java.awt.AWTEvent.KEY_EVENT_MASK);
	}

	protected abstract void processKeyEvent(KeyEvent e);

	public void PanelChange(WindowMode windowMode) {
		mainFrame.PanelChange(windowMode);
	}
}
