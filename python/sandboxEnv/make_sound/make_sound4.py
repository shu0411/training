#pysynthを持ってきたもの。うまくはいっているが、未解析

#!/usr/bin/env python

#from demosongs import *
#from mkfreq import getfreq

#pitchhz, keynum = getfreq(pr = True)

harm_max = 4.

import wave, math, struct

keys_s = ('a', 'a#', 'b',  'c',  'c#', 'd', 'd#', 'e',  'f',  'f#', 'g', 'g#')
keys_f = ('a', 'bb', 'b',  'c',  'db', 'd', 'eb', 'e',  'f',  'gb', 'g', 'ab')
keys_e = ('a', 'bb', 'cb', 'b#', 'db', 'd', 'eb', 'fb', 'e#', 'gb', 'g', 'ab')

def getfreq(pr = False):
	pitchhz, keynum = {}, {}
	if pr:
		print("Piano key frequencies (for equal temperament):")
		print("Key number\tScientific name\tFrequency (Hz)")
	for k in range(88):
		freq = 27.5 * 2.**(k/12.)
		oct = (k + 9) // 12
		note = '%s%u' % (keys_s[k%12], oct)
		if pr:
			print("%10u\t%15s\t%14.2f" % (k+1, note.upper(), freq))
		pitchhz[note] = freq
		keynum[note] = k
		note = '%s%u' % (keys_f[k%12], oct)
		pitchhz[note] = freq
		keynum[note] = k
		note = '%s%u' % (keys_e[k%12], oct)
		pitchhz[note] = freq
		keynum[note] = k
	return pitchhz, keynum

pitchhz, keynum = getfreq(pr = True)

file_name="pysynth_scale.wav"

def make_wav(song):
	bpm = 120
	bpmfac = 120./bpm
	
	pause = .05
	boost = 1.1
	repeat = 0
	transpose = 0 #?
	f=wave.open(file_name,'w')

	f.setnchannels(1)
	f.setsampwidth(2)
	f.setframerate(44100)
	f.setcomptype('NONE','Not Compressed')

	def length(l):
		return 88200./l*bpmfac

	def sixteenbit(x):
		return struct.pack('h', round(32000*x))

	def asin(x):
		return math.sin(2.*math.pi*x)

	def render2(a,b,vol):
		tmp1 = 44100. / a
		b2 = (1.-pause) * b
		tmp2 =float(b2)/44100.*a
		
		q = int(tmp2 * tmp1)
		ow = b''

		# harmonics are frequency-dependent:
		lf = math.log(a)
		lf_fac = (lf-3.) / harm_max
		if lf_fac > 1:
			harm = 0
		else:
			harm = 2. * (1 - lf_fac)
		decay = 2. / lf
		t = (lf-3.) / (8.5-3.)
		volfac = 1. + .8 * t * math.cos(math.pi / 5.3 * (lf - 3.))

		for x in range(q):
			fac=1.
			if x<100:
				fac=x/80.
			if 100<=x<300:
				fac=1.25-(x-100)/800.
			if x>q-400:
				fac=1.-((x-q+400)/400.)
			s = float(x)/float(q)
			dfac =  1. - s + s * decay
			
			ow = ow + sixteenbit(
				        (asin( float(x) / tmp1 )
                        + harm * asin( float(x) / (tmp1/2.) )
                        + .5 * harm * asin( float(x) / (tmp1/4.)))/4. * fac * vol * dfac * volfac)
		fill = max(int(ex_pos - curpos - q), 0)
		f.writeframesraw((ow)+(sixteenbit(0)*fill))
		return q + fill

	##########################################################################
	# Write to output file (in WAV format)
	##########################################################################

	print("Writing to file", file_name)
	curpos = 0
	ex_pos = 0.
	for rp in range(repeat+1):
		for nn, note_list in enumerate(song):
			note_name = note_list[0]
			note_length = note_list[1]

			if not nn % 4:
				print("[%u/%u]\t" % (nn+1,len(song)))
			if note_name!='r':
				if note_name[-1] == '*':
					vol = boost
					note = note_name[:-1]
				else:
					vol = 1.
					note = note_name
				try:
					a=pitchhz[note]
				except:
					a=pitchhz[note + '4']	# default to fourth octave
				a = a * 2**transpose
				if note_length < 0:
					b=length(-2.*note_length/3.)
				else:
					b=length(note_length)
				ex_pos = ex_pos + b
				curpos = curpos + render2(a,b,vol)

			if note[0]=='r':
				b=length(note_length)
				ex_pos = ex_pos + b
				f.writeframesraw(sixteenbit(0)*int(b))
				curpos = curpos + int(b)

	f.writeframes(b'')
	f.close()
	print()

##########################################################################
# Synthesize demo songs
##########################################################################

if __name__ == '__main__':
	song1 = [
        ['c',4],['d',4],['e',4],['f',4],['g',4],['a',4],['b',4],['c5',2],['r',1],
        ['c3',4],['d3',4],['e3',4],['f3',4],['g3',4],['a3',4],['b3',4],['c4',2],['r',1],
        ['c1*', 1], ['c2*', 1], ['c3*', 1], ['c4*', 1], ['c5*', 1], ['c6*', 1], ['c7*', 1], ['c8*', 1],
    ]
	print()
	print("Creating Demo Songs... (this might take about a minute)")
	print()

	# SONG 1
	make_wav(song1)



