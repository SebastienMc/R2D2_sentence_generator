import json
from struct import pack
from math import sin, pi
from random import randint

def r2d2(sentence):
	def freq(sentence):
	    return [d[ord(x) - 65 + 45]['frequency'] for x in sentence]

	def au_file(name='test.au', freqs=[], dur=200, vol=0.5):
	    """
	    creates an AU format sine wave audio file
	    of frequency freq (Hz)
	    of duration dur (milliseconds)
	    and volume vol (max is 1.0)
	    """
	    file_length = 0
	    val = b""
	    
	    for freq in freqs:
	        factor = 2 * pi * freq / 8000
	        # write data
	        note_dur = randint(dur-100, dur+100)
	        file_length += note_dur
	        for seg in range(8 * note_dur):
	            # sine wave calculations
	            sin_seg = sin(seg * factor)
	            val += pack('b', int(vol * 127 * sin_seg))
	    
	    fout = open(name, 'wb')
	    # header needs size, encoding=2, sampling_rate=8000, channel=1
	    fout.write(pack('>4s5L', '.snd'.encode("utf8"), 24, 8 * file_length, 2, 8000, 1))

	    fout.write(val)
	        
	    fout.close()
	    print("File %s written" % name)


	with open('notes.json') as json_data:
	    d = json.load(json_data)
	    d = d['440']

	sentence = sentence.upper()

	freqs = freq(sentence)

	au_file(name='r2d2.au', freqs=freqs, dur=100, vol=0.8)
