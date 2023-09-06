from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from deep_translator import GoogleTranslator
import openai
import os
from dotenv import load_dotenv

# Set your OpenAI API key
load_dotenv()
openai.api_key = os.environ.get("OPENAI_TOKEN")


def openai_generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"],
    )

    return response.choices[0].text


def index(request):
    r = sr.Recognizer()
    spoken_text = "Default text"
    ai_response = "Default response"

    def SpeakText(command):
        # Translate the command to Urdu
        ar = GoogleTranslator(source="auto", target="ur").translate(command)
        tts = gTTS(ar, lang="ur")
        tts.save("output7.mp3")
        audio = AudioSegment.from_file("output7.mp3")
        play(audio)
        # play("output7.mp3")

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = r.listen(source)
            with open("audio_file", "wb") as f:
                f.write(audio.get_raw_data())
            print("Recording complete.")
            spoken_text = r.recognize_google(audio, language="en-US")
            print("You said:", spoken_text)

            # Create a conversation prompt
            conversation_prompt = f"Human: {spoken_text}\nAI:"

            # Generate a response using OpenAI
            ai_response = openai_generate_response(conversation_prompt)

            # Translate the AI response to Urdu and speak it
            SpeakText(ai_response)

            print("AI:", ai_response)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occurred")

    context = {
        "spoken_text": spoken_text,
        "ai_response": ai_response,
    }

    return JsonResponse(context)
    # return render(request, "chat.html", context)
    # return HttpResponse(ai_response)


def chat(request):
    return render(request, "chat.html")
