import numpy as np
import wave

# パラメータ
sample_rate = 44100  # サンプリングレート
duration = 0.5  # トーンの持続時間（秒）

# チャイムのメロディーを作成するための周波数（Hz）
frequencies = [440, 440, 880, 440]  # A4, A4, A5, A4

# 空のオーディオデータを作成
audio_data = np.array([], dtype=np.float32)

# 各トーンを生成し、オーディオデータに追加
for freq in frequencies:
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * 2 * np.pi * t)
    audio_data = np.concatenate((audio_data, tone))

# オーディオデータを [-1, 1] の範囲に正規化
audio_data /= np.max(np.abs(audio_data))

# WAVファイルとして書き出し
#write('school_chime.wav', sample_rate, audio_data)

sampwidth=3
writefilename = "./write-audio.wav"

# write wavefiles
wav_file = wave.open(writefilename, "wb")
#convert numpy arrays to binary format
#write_binary_data = audio_data.tobytes()
#wav_file.writeframes(write_binary_data)

# setting parameters
wav_file.setnchannels(1)
wav_file.setsampwidth(sampwidth)
wav_file.setframerate(sample_rate)
wav_file.writeframes(audio_data)
wav_file.close() # close file