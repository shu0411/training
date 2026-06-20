import numpy as np
from scipy.io.wavfile import write

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
write('school_chime.wav', sample_rate, audio_data)

