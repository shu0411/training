package main;

import java.awt.Color;

import javax.swing.JFrame;
import javax.swing.JPanel;

import base.PanelLibrary;
import enums.WindowMode;
import panel.BattlePanel;
import panel.TitlePanel;
import panel.WalkPanel;

public class MainFrame extends JFrame {

	public WindowMode	windowMode = WindowMode.TITLE;

	JPanel	basePanel = PanelLibrary.makePanel( Color.BLACK );
	TitlePanel	titlePanel;
	WalkPanel	walkPanel;
	BattlePanel	battlePanel;

	public MainFrame(){

		setBounds( 200, 120, 940, 540 );	//フレーム位置、サイズ設定
		setDefaultCloseOperation( EXIT_ON_CLOSE );	//×ボタン追加
		add(basePanel);
		PanelChange(windowMode);				//親パネルをフレームに貼り付け
		setVisible(true);					//フレーム表示

	}

	/**
	 * パネル制御
	 */

	public void PanelChange(WindowMode changeMode) {
		basePanel.removeAll();
		windowMode = changeMode;
		switch(windowMode) {
			case WALK:
				walkPanel = new WalkPanel(this);
				basePanel.add(walkPanel);
				walkPanel.requestFocus();
				break;
			case BATTLE:
				battlePanel = new BattlePanel(this);
				basePanel.add(battlePanel);
				battlePanel.requestFocus();
				battlePanel.setFocusable(true);
				break;
			case TITLE:
			case ELSE:
			default:
				titlePanel = new TitlePanel(this);
				basePanel.add(titlePanel);
				titlePanel.requestFocus();
				titlePanel.setFocusable(true);
				break;
		}
		basePanel.revalidate();
	}
/*
	//行動処理
	@Override protected void processKeyEvent(KeyEvent e)
	{
		if(e.getID() == KeyEvent.KEY_PRESSED)
		{
			System.out.println("キー" + e.getKeyCode() +  "が押された!");
			switch(windowMode) {
				case TITLE:{
					windowMode = WindowMode.BATTLE;
					basePanel.removeAll();
					PanelChange(windowMode);
					revalidate(); // ここで再描画を要請
					break;
				}
				case BATTLE:
					battlePanel.mainKeyEvent( this, e.getKeyCode());
					revalidate(); // ここで再描画を要請
					break;
				case ELSE:
				default:
					break;
			}
		}
	}
*/
}
