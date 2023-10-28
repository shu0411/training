package com.example.janken

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.preference.PreferenceManager
import com.example.janken.databinding.ActivityResultBinding

class ResultActivity : AppCompatActivity() {
    val numGu = 0
    val numChoki = 1
    val numPa = 2

    private lateinit var binding: ActivityResultBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityResultBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val id = intent.getIntExtra("MY_HAND",0)

        //自分の手の状態を取得、表示
        val myHand: Int
        when(id){
            R.id.btnGu      -> {
                binding.imgMyHand.setImageResource(R.drawable.my_gu)
                myHand = numGu
            }
            R.id.btnChoki   -> {
                binding.imgMyHand.setImageResource(R.drawable.my_choki)
                myHand = numChoki
            }
            R.id.btnPa      -> {
                binding.imgMyHand.setImageResource(R.drawable.my_pa)
                myHand = numPa
            }
            else -> {
                myHand = numGu
            }
        }

        //相手の手を決定、表示
        val comHand = getHand()
        when(comHand) {
            numGu       ->{
                binding.imgComHand.setImageResource(R.drawable.com_gu)
            }
            numChoki    ->{
                binding.imgComHand.setImageResource(R.drawable.com_choki)
            }
            numPa   ->{
                binding.imgComHand.setImageResource(R.drawable.com_pa)
            }
        }

        //勝敗判定(グー：0、チョキ：1、パー：2)
        val gameResult = (comHand - myHand + 3) % 3
        val textResult = when(gameResult){
            0 -> R.string.text_result_draw  //引き分け
            1 -> R.string.text_result_win   //勝ち
            2 -> R.string.text_result_lose  //負け
            else -> R.string.text_result_draw
        }
        binding.lblResult.setText(textResult)
        binding.btnBack.setOnClickListener { finish() }

        //じゃんけんの結果を保存
        saveData(myHand, comHand, gameResult)
    }

    private fun saveData(myHand: Int, comHand: Int, gameResult: Int){
        val pref = PreferenceManager.getDefaultSharedPreferences(this)

        val gameCount           = pref.getInt("GAME_COUNT", 0)
        val winningStreakCount  = pref.getInt("WINNING_STREAK_COUNT", 0)
        val lastComHand         = pref.getInt("LAST_COM_HAND", 0)
        val lastGameResult      = pref.getInt("GAME_RESULT", -1)

        //連勝回数の値取得
        val edtWinningStreakCount: Int =
            if(lastGameResult == 2 && gameResult == 2) {
                 winningStreakCount + 1
            }
            else{
                0
            }

        //各Preferenceの更新
        val editor = pref.edit()
        editor
            .putInt("GAME_COUNT", gameCount + 1)
            .putInt("WINNING_STREAK_COUNT", edtWinningStreakCount)
            .putInt("LAST_MY_HAND", myHand)
            .putInt("LAST_COM_HAND", comHand)
            .putInt("BEFORE_LAST_COM_HAND", lastComHand)
            .putInt("GAME_RESULT", gameResult)
            .apply()
    }

    private fun getHand(): Int{
        var hand = (Math.random() * 3).toInt()
        val pref = PreferenceManager.getDefaultSharedPreferences(this)

        val gameCount           = pref.getInt("GAME_COUNT", 0)
        val winningStreakCount  = pref.getInt("WINNING_STREAK_COUNT", 0)
        val lastMyHand          = pref.getInt("LAST_MY_HAND", 0)
        val lastComHand         = pref.getInt("LAST_COM_HAND", 0)
        val beforeLastComHand   = pref.getInt("BEFORE_LAST_COM_HAND", 0)
        val gameResult          = pref.getInt("GAME_RESULT", -1)

        if(gameCount == 1){
            if(gameResult == 2){
                //前回：1回目、コンピュータが勝ち
                //次出す手を変える
                while(lastComHand == hand){
                    hand = (Math.random() * 3).toInt()
                }
            } else if (gameResult == 1) {
                //前回：1回目、コンピュータが負け
                //前回相手が出した手に勝つ手を出す
                hand = (lastMyHand - 1 + 3) % 3
            }
        } else if (winningStreakCount > 0){
            if (beforeLastComHand == lastComHand){
                //同じ手で連勝した場合は手を変える
                while(lastComHand == hand){
                    hand = (Math.random() * 3).toInt()
                }
            }
        }
        return hand
    }
}