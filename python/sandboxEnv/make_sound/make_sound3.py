#汎用性高めようとしたが、音割れ。
#ChatGPTが作成したものをベースに、pysynth.pyを参考にして作成。
import numpy as np
import wave
import struct

#クラス設定
class Make_wave:
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

# パラメータ設定
channel_count = 1 # チャンネル数  1:モノラル 2:ステレオ
sampwidth_byte = 2 # サンプルサイズ 1:8bit 2:16bit 3:24bit
sample_rate = 44100  # サンプリングレート
dt = 1.0 / sample_rate  # 時間増分

duration = 1  # 4分音符トーンの持続時間（秒）
write_file_name = 'school_chime3.wav'

if __name__ == '__main__':
    f=wave.open(write_file_name,'w')

    f.setnchannels(channel_count)   #チャンネル数を設定します。1:モノラル 2:ステレオ
    f.setsampwidth(sampwidth_byte)   #サンプルサイズを設定します。1:8bit 2:16bit 3:24bit
    f.setframerate(sample_rate)   #サンプリング周波数を設定します。
    f.setcomptype('NONE','Not Compressed')  #圧縮形式とその記述を設定します。

    # 空のオーディオデータを作成
    audio_data = []

    # 各トーンを生成
    for note in melody:
        freq = notes[note[0]]
        wave = Make_wave(freq, dt)
        for _ in range(int(sample_rate * duration * note[1])):
            audio_data.append(wave.value())

    # NumPy 配列に変換
    audio_data = np.array(audio_data, dtype=np.float16)

    # オーディオデータを [-1, 1] の範囲に正規化
    audio_data /= np.max(np.abs(audio_data))

    write_binary_data = audio_data.tobytes()

    f.writeframesraw(write_binary_data)
    f.close()
