from src import textToSpeech

def triggerFunction(event, context):
    ts = textToSpeech()
    return ts.TextToSpeech(event, context)