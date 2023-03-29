import json
import vosk
import sys
import sounddevice
import queue

vosk.SetLogLevel(-1)


class SpeechRecognition:
	def __init__(self):
		self.model = vosk.Model('backend/vosk-model-ua')
		self.sample_rate = 16000
		self._device = 1
		self._q = queue.Queue()

	def _callback(self, indata, frames, time, status):
		if status:
			print(status, file=sys.stderr)

		self._q.put(bytes(indata))	

	def listen(self):
		with sounddevice.RawInputStream(samplerate=self.sample_rate, blocksize=8000, device=self._device, dtype='int16',
										channels=1, callback=self._callback):
			recognizer = vosk.KaldiRecognizer(self.model, self.sample_rate)

			while True:
				data = self._q.get()
				if recognizer.AcceptWaveform(data):
					yield json.loads(recognizer.Result())['text']


speech_recognition = SpeechRecognition()