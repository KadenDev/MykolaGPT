import time
from backend.mykyta import mykyta
from backend.speech_recognition import speech_recognition

class MainProgram:
	def __init__(self):
		print('Асистент запущений успішно...')

	def start(self):
		for phrase in speech_recognition.listen():
			if len(phrase) > 0:
				print(f'[Я]: {phrase.capitalize()}')

				response = mykyta.generate_response(phrase)

				print(f'[МИКИТА]: {response.capitalize()}')

				mykyta.say(response)


if __name__ == '__main__':
	MainProgram().start()