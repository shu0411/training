import numpy as np
from scipy.io.wavfile import write

#クラス設定
class Wave:
    #freq: 周波数,  dt: 時間増分(1/sampling rate)
    def __init__(self, freq, dt):
        self.freq = freq
        self.phase = 0.0
        #self.harmonics = [(1, 0.5), (2, 0.3), (3, 0.2)]  # (倍数, 強度)
        self.dt = dt

    def value(self):
        v = np.sin(2 * np.pi * self.phase)
        #v = sum(amplitude * np.sin(2 * np.pi * self.phase * harmonic)
        #        for harmonic, amplitude in self.harmonics)
        self.phase += self.freq * self.dt
        if self.phase > 1.0:
            self.phase -= 1.0
        return v

# パラメータ設定
sample_rate = 44100  # サンプリングレート
dt = 1.0 / sample_rate  # 時間増分
duration = 1  # 4分音符トーンの持続時間（秒）
write_file_name = 'school_chime2.wav'

# メロディーに対応する周波数（Cメジャースケール基準）
notes = {
    'C': 261.63,  # ド
    'D': 293.66,  # レ
    'E': 329.63,  # ミ
    'F': 349.23,  # ファ
    'G': 392.00,  # ソ
    'A': 440.00,  # ラ
    'B': 493.88,  # シ
    'X': 000.00,  # シ
}

# メロディー (ファ、ラ、ソ、ドー、ファ、ソ、ラ、ファー)
melody = [
    ('F',1),
    ('A',1),
    ('G',1),
    ('C',2),
    ('F',1),
    ('G',1),
    ('A',1),
    ('F',2),
]

# 空のオーディオデータを作成
audio_data = []

# 各トーンを生成
for note in melody:
    freq = notes[note[0]]
    wave = Wave(freq, dt)
    for _ in range(int(sample_rate * duration * note[1])):
        audio_data.append(wave.value())

# NumPy 配列に変換
audio_data = np.array(audio_data, dtype=np.float32)

# オーディオデータを [-1, 1] の範囲に正規化
audio_data /= np.max(np.abs(audio_data))

# WAVファイルとして書き出し
write(write_file_name, sample_rate, audio_data)