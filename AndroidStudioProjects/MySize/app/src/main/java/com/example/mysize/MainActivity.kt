package com.example.mysize

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.edit
import androidx.preference.PreferenceManager
import com.example.mysize.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val pref = PreferenceManager.getDefaultSharedPreferences(this)
        val editNeck    = pref.getString("NECK","")
        val editSleeve  = pref.getString("SLEEVE","")
        val editWaist   = pref.getString("WAIST","")
        val editInseam  = pref.getString("INSEAM","")

        binding.txtNeck.setText(editNeck)
        binding.txtSleeve.setText(editSleeve)
        binding.txtWaist.setText(editWaist)
        binding.txtInseam.setText(editInseam)

        binding.btnSave.setOnClickListener { onSaveTapped() }
    }
    private fun onSaveTapped(){
        val pref = PreferenceManager.getDefaultSharedPreferences(this)
        pref.edit {
            putString("NECK",    binding.txtNeck.text.toString())
            putString("SLEEVE",  binding.txtSleeve.text.toString())
            putString("WAIST",   binding.txtWaist.text.toString())
            putString("INSEAM",  binding.txtInseam.text.toString())
        }
    }
}