# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:54:19 2022

@author: Rasool
"""

import base64
import os
import json
import re
from google.cloud.vision import ImageAnnotatorClient, Feature, GcsSource, InputConfig, OutputConfig, GcsDestination, AsyncAnnotateFileRequest
from google.cloud import storage
from google.cloud import pubsub_v1
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

def store_audio_to_gcs(filename,audio_content):
    clnt = storage.Client()
    bucket = clnt.get_bucket('pdftotext-result-files')
    blob = bucket.blob(filename)
    with blob.open(mode='wb') as f:
        f.write(audio_content)
    print('File Uploaded')
    
def speech_synthesis(page):
    
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=page)
    
    voice = texttospeech.VoiceSelectionParams(
        language_code="hi", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)
    
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config)
    
    return response.audio_content
    
def TextToSpeech(event, context):
    
    res = (event['data'])
    json_res = json.loads(res)
    print(json_res)
    filename = json_res['data']['message']['filename']
    pages = json_res['data']['message']['pages']
    for page_number in pages.keys():
        audio = speech_synthesis(pages[page_number])
        f = f'{filename}_{page_number}.mp3'
        store_audio_to_gcs(f,audio)
    print('TEXT_TO_SPEECH COMPLETED')
    