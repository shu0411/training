using Godot;
using System;

public partial class Hud : CanvasLayer
{
    [Signal]
    public delegate void StartGameEventHandler();


    public void ShowMessage(string message)
    {
        var messageLabel = GetNode<Label>("MessageLabel");
        messageLabel.Text = message;
        messageLabel.Show();

        GetNode<Timer>("MessageTimer").Start();
    }

    async public void ShowGameOver()
    {
        ShowMessage("Game Over!");

        var messageTimer = GetNode<Timer>("MessageTimer");
        await ToSignal(messageTimer, Timer.SignalName.Timeout);

        var messageLabel = GetNode<Label>("MessageLabel");
        messageLabel.Text = "Dodge the Creeps!";
        messageLabel.Show();

        await ToSignal(GetTree().CreateTimer(1.0f), SceneTreeTimer.SignalName.Timeout);
        GetNode<Button>("StartButton").Show();
    }

    public void UpdateScore(int score)
    {
        var scoreLabel = GetNode<Label>("ScoreLabel");
        scoreLabel.Text = score.ToString();
    }

    private void OnStartButtonPressed()
    {
        GetNode<Button>("StartButton").Hide();
        GetNode<Label>("MessageLabel").Hide();
        EmitSignal(SignalName.StartGame);
    }

    private void OnMessageTimerTimeout()
    {
        var messageLabel = GetNode<Label>("MessageLabel");
        messageLabel.Hide();
    }
}
