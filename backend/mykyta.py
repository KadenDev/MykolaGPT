import openai
import sounddevice
import time

from backend.voice import TextToVoice
from config import openai_api_key


class Mykyta:
	def __init__(self):
		self.voice = TextToVoice()
		openai.api_key = openai_api_key

	def say(self, text: str):
		audio = self.voice.convert_text_to_audio(text)
		sounddevice.play(audio, self.voice.sample_rate * 1.05)
		
		time.sleep((len(audio) / self.voice.sample_rate) + 0.5)
		
		sounddevice.stop()

	def generate_response(self, message: str):
		response = openai.ChatCompletion.create(
			model='gpt-3.5-turbo',
			messages=[
					{'role': 'user', 'content': message}
				]
		)

		return response.choices[0].message.content


mykyta = mykyta.Mykyta()