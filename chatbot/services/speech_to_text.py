import azure.cognitiveservices.speech as speechsdk
from django.conf import settings

def transcribe_audio(file_path):
    speech_config = speechsdk.SpeechConfig(subscription=settings.AZURE_SPEECH_KEY, region=settings.AZURE_SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    
    result = recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("RECOGNIZED:", result.text)
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("NOMATCH: Speech could not be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print("CANCELED:", cancellation.reason)
        if cancellation.reason == speechsdk.CancellationReason.Error:
            print("ERROR:", cancellation.error_details)

    return ""