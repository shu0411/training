package main;

public class Main {

	public static void main(String[] args) {

		new MainFrame();

	}

}

/*
今後の課題：

Titleで1～3を押すとBattleのイベントが進む→メインフレームでthis.revalidate
processKeyEventは、MainFrameで取得して、各パネルに渡してあげる方が適切（楽）か？

*/