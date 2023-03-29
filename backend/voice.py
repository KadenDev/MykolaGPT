import torch


class TextToVoice:
	def __init__(self):
		self.language = 'ua'
		self.model_id = 'v3_ua'
		self.sample_rate = 48000
		self.speaker = 'mykyta'
		self.put_accent = True
		self.put_yo = True
		self._device = torch.device('cpu')

		self.model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=self.language,
                          speaker=self.model_id)
		
		self.model.to(self._device)

	def convert_text_to_audio(self, text: str):
		audio = self.model.apply_tts(text=text,
                            	speaker=self.speaker,
                            	sample_rate=self.sample_rate,
                            	put_accent=self.put_accent,
                            	put_yo=self.put_yo)

		return audio