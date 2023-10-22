package com.example.animalbook

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.animalbook.databinding.ActivitySubBinding

class SubActivity : AppCompatActivity() {
    private lateinit var binding: ActivitySubBinding
    private lateinit var title: TitleFragment
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySubBinding.inflate(layoutInflater)
        setContentView(binding.root)

        //ボタン押下時のイベント設定
        binding.btnLion.setOnClickListener {
            supportFragmentManager.beginTransaction().apply {
                replace(R.id.container, LionFragment())
                addToBackStack(null)
                commit()
            }
        }
        binding.btnHippo.setOnClickListener {
            supportFragmentManager.beginTransaction().apply {
                replace(R.id.container, HippoFragment())
                addToBackStack(null)
                commit()
            }
        }
        binding.btnGiraffe.setOnClickListener {
            supportFragmentManager.beginTransaction().apply {
                replace(R.id.container, GiraffeFragment())
                addToBackStack(null)
                commit()
            }
        }
        //タイトル表示
        title = TitleFragment()
        supportFragmentManager.beginTransaction().apply {
            replace(R.id.frmTitle, title)
            commit()
        }
    }

    override fun onResume() {
        super.onResume()
        //サブ画面のタイトル指定
        //title.setTitle("サブ画面")
        title.setTitle(getString(R.string.subtitle_text))
    }
}