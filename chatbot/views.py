import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.speech_to_text import transcribe_audio
from .services.text_to_speech import synthesize_speech
from .services.openai_service import get_recommendation_from_gpt
from .services.convert_to_azure_pcm import convert_to_azure_pcm

@csrf_exempt
def chat(request):
    raw_audio_path = "media/input.wav"
    converted_audio_path = "media/audio_input.wav"
    response_audio_path = "media/audio_output.wav"

    if request.method == 'POST':
        if request.FILES.get("audio"):
            with open(raw_audio_path, 'wb+') as f:
                for chunk in request.FILES['audio'].chunks():
                    f.write(chunk)

            convert_to_azure_pcm(raw_audio_path, converted_audio_path)
            user_text = transcribe_audio(converted_audio_path)

        elif request.content_type == "application/json":
            body = json.loads(request.body.decode('utf-8'))
            user_text = body.get("text_input", "").strip()

        else:
            return JsonResponse({"error": "Invalid request"}, status=400)

        bot_reply = get_recommendation_from_gpt(user_text)
        synthesize_speech(bot_reply, response_audio_path)

        return JsonResponse({
            'user_text': user_text,
            'text': bot_reply,
            'audio_url': f"/media/audio_output.wav"
        })

    return render(request, "index.html")
