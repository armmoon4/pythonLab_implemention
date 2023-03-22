import openai
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "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"
engine.say("Hello Moon! I am your virtual assistant you can ask me any question if you want.")
engine.runAndWait()
while True:

    with sr.Microphone() as source:
        print('Speak Now:')
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
    model = "text-davinci-003"
    if "exit" in data:
        break

    completion = openai.Completion.create(model = "text-davinci-003",
        prompt =  data,
        max_tokens = 1024,
        temperature = 0.5,
        n = 1 ,
        stop = None)

    response = completion.choices[0].text
    print(response)
    engine.say(response)
    engine.runAndWait()