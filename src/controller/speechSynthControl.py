from ..utilities import SpeechSynthesizer,AudioWriter
import json

class textToSpeech:
    def __init__(self):
        self._SpeechSy = SpeechSynthesizer()
        self._writer = AudioWriter()

    def TextToSpeech(self,event, context):
        
        res = (event['data'])
        json_res = json.loads(res)
        print(json_res)
        filename = json_res['data']['message']['filename']
        pages = json_res['data']['message']['pages']
        for page_number in pages.keys():
            audio = self._SpeechSy.speech_synthesis(pages[page_number])
            f = f'{filename}_{page_number}.mp3'
            self._writer.writeAudio(f,audio)
        print('TEXT_TO_SPEECH COMPLETED')
        return 'Done'
        