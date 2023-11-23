from scipy.io.wavfile import write as write_wav
import numpy as np
import winsound
from multiprocessing import Pool

class Wave():
    #freq: 周波数,  dt: 時間増分(1/sampling rate)
    def __init__(self, freq, dt):
        self.freq = freq
        self.phase = 0.0
        self.dt = dt

    def value(self):
        v = np.sin(2*np.pi * self.phase)
        self.phase += self.freq * self.dt
        if self.phase > 1.0:
            self.phase -= 1.0
        return v

# winsound.SND_LOOP: 繰り返し再生
def mysound(v):
    winsound.PlaySound(v, winsound.SND_ASYNC |
                       winsound.SND_FILENAME | winsound.SND_LOOP)

if __name__ == '__main__':
    #     サンプリング周波数
    s_rate = 44100
    #     音データの長さ（２秒）
    ts = np.linspace(0, 2, s_rate * 2 + 1)
    #     時間増分
    d_t = 1.0 / s_rate
    
    Do = Wave(523.251, d_t) # ド（523.251ヘルツ）
    Mi = Wave(659.255, d_t) # ミ（659.255ヘルツ）
    Sol = Wave(783.991, d_t) # ソ（783.991ヘルツ）

    # 音データの作成
    w_values = np.zeros(len(ts))    # 音データの配列を初期化
    #最初の0.5秒はド、次の0.5秒はミ、次の0.5秒はソ、最後の0.5秒は（ド＋ミ＋ソ）の平均
    for t in range(len(ts)):
        if t < len(ts) / 4:
            w_values[t] = Do.value()
        elif t < 2 * len(ts) / 4:
            w_values[t] = Mi.value()
        elif t < 3 * len(ts) / 4:
            w_values[t] = Sol.value()
        else:
            w_values[t] = (Do.value() + Mi.value() + Sol.value()) / 3

    #音データの強さの調整
    amplitude = np.iinfo(np.int16).max * 0.5    # 16bitの最大値の半分
    max_wave = np.abs(w_values).max()           # 音データの絶対値の最大値
    w_values = w_values * amplitude / max_wave  # 音データの強さを調整

    # numpy.ndarrayのデータをint16型でwavファイルに書き出す
    write_wav("example.wav", s_rate, w_values.astype(np.int16))

    # Enterキーが押されるまで、繰り返し再生になるように
    # 再生を別プロセスとして実行する。
    with Pool() as pool:
        print('Playing.')
        pool.map(mysound, ["example.wav"])
        print()
        a = input('Press Enter-key, to exit.')
        pool.terminate()