from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

class SpeechSynthesizer:
    def speech_synthesis(self,page):
        
        client = texttospeech.TextToSpeechClient()

        synthesis_input = texttospeech.SynthesisInput(text=page)
        
        voice = texttospeech.VoiceSelectionParams(
            language_code="hi", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3)
        
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config)
        
        return response.audio_content