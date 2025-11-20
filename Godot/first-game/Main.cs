using Godot;
using System;
using System.IO;

public partial class Main : Node
{
	[Export]
	public PackedScene MobScene { get; set; }

	private int _score = 0;

	public void NewGame()
	{
		_score = 0;
		var player = GetNode<Player>("Player");
		var startPosition = GetNode<Marker2D>("StartPosition");
		player.Start(startPosition.Position);

		GetNode<Timer>("StartTimer").Start();

		var hud = GetNode<Hud>("HUD");
		hud.UpdateScore(_score);
		hud.ShowMessage("Get Ready!");
	}

	public void GameOver()
	{
		GetNode<Timer>("MobTimer").Stop();
		GetNode<Timer>("ScoreTimer").Stop();

		var hud = GetNode<Hud>("HUD");
		hud.ShowGameOver();
	}

	private void OnMobTimerTimeout()
	{
		//Mobシーンをインスタンス化
		Mob mob = MobScene.Instantiate<Mob>();

		//Mobの出現位置をランダムに設定
		var mobSpawnLocation = GetNode<PathFollow2D>("MobPath/MobSpawnLocation");
		mobSpawnLocation.ProgressRatio = GD.Randf();
		mob.Position = mobSpawnLocation.Position;

		//Mobの方向を設定
		float direction = mobSpawnLocation.Rotation + Mathf.Pi / 2; //開始位置の移動方向から90度右に向ける
		direction += (float)GD.RandRange(-Mathf.Pi / 4, Mathf.Pi / 4);  //少しランダムにずらす
		mob.Rotation = direction;

		//Mobの速度を設定
		var velocity = new Vector2((float)GD.RandRange(150.0, 250.0), 0);
		mob.LinearVelocity = velocity.Rotated(direction);       //方向に合わせて速度ベクトルを回転

		//Nodeの子としてモブを追加
		AddChild(mob);
	}

	private void OnScoreTimerTimeout()
	{
		_score++;
		var hud = GetNode<Hud>("HUD");
		hud.UpdateScore(_score);
	}

	private void OnStartTimerTimeout()
	{
		GetNode<Timer>("MobTimer").Start();
		GetNode<Timer>("ScoreTimer").Start();
	}

	// Called when the node enters the scene tree for the first time.
	public override void _Ready()
	{
	}

	// Called every frame. 'delta' is the elapsed time since the previous frame.
	public override void _Process(double delta)
	{
	}
}
