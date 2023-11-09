import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random
import requests
from bs4 import BeautifulSoup

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("I'm sorry, but I couldn't request results. Check your internet connection.")
        return ""

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time

def get_name():
    speak("What's your name?")
    name = listen()
    if name:
        return name
    else:
        return "User"

def get_weather(city):
    api_key = "cc5a2a83e6f6b102260dd275470bedca" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        temperature_celsius = temperature - 273.15
        return f"The weather in {city} is {weather_description} with a temperature of {temperature_celsius:.2f}°C."
    else:
        return "I couldn't retrieve the weather information for that location."


def get_answer(question):
    try:
        response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&utf8=&srsearch={question}")
        data = response.json()
        search_results = data["query"]["search"]
        if search_results:
            page_title = search_results[0]["title"]
            page_url = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
            response = requests.get(page_url)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            answer = paragraphs[0].text  # Get the first paragraph
            return answer
        else:
            return "I couldn't find any information related to your question."
    except Exception as e:
        return "An error occurred while searching for the answer."

def main():
    name = get_name()
    print(f"Hello, {name}! How can I assist you today?")
    speak(f"Hello, {name}! How can I assist you today?")
    while True:
        command = listen()
        if "hello" in command:
            print(f"Hello, {name}! How can I help you?")
            speak(f"Hello, {name}! How can I help you?")
        elif "goodbye" in command:
            print(f"Goodbye, {name}!")
            speak(f"Goodbye, {name}!")
            break
        elif "time" in command:
            current_time = get_time()
            print(f"The current time is {current_time}.")
            speak(f"The current time is {current_time}.")
        elif "search" in command:
            print("What do you want to search for?")
            speak("What do you want to search for?")
            search_query = listen()
            if search_query:
                search_url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(search_url)
                break
        elif "joke" in command:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "How does a penguin build its house? Igloos it together!",
                "What do you call a fish with no eyes? Fsh!",
            ]
            joke = random.choice(jokes)
            print(joke)
            speak(joke)
        elif "weather" in command:
            print("Sure, which city would you like to check the weather for?")
            speak("Sure, which city would you like to check the weather for?")
            city = listen()
            weather_info = get_weather(city)
            print(weather_info)
            speak(weather_info)
        elif "reminder" in command:
            print("What's the reminder?")
            speak("What's the reminder?")
            reminder = listen()
            if reminder:
                print(f"Reminder set: {reminder}")
                speak(f"Reminder set: {reminder}")
            else:
                print("I couldn't catch that. Please try again.")
                speak("I couldn't catch that. Please try again.")
        elif "question" in command:
            print("What's your question?")
            speak("What's your question?")
            question = listen()
            if question:
                answer = get_answer(question)
                print(answer)
                speak(answer)
            else:
                print("I couldn't catch your question. Please ask again.")
                speak("I couldn't catch your question. Please ask again.")
        else:
            print(f"I'm not sure how to help with that, {name}. Please say 'hello,' 'goodbye,' 'time,' 'search,' 'tell me a joke,' 'weather,' 'reminder,' or 'question'.")
            speak(f"I'm not sure how to help with that, {name}. Please say 'hello,' 'goodbye,' 'time,' 'search,' 'tell me a joke,' 'weather,' 'reminder,' or 'question'.")

if __name__ == "__main__":
    main()
