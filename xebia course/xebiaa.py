from datetime import datetime
import webbrowser
import requests

# API keys
OPENWEATHER_API_KEY = "360778482134fd7909b8ae6749967c9b"
NEWS_API_KEY = "695e07af402f4b119f0703e9b19f4683"

# basic commands
greet_msgs = ["hi", "hello", "hey"]
date_msgs = ["date", "today date", "tell me date"]
time_msgs = ["time", "current time"]
news_msgs = ["news", "headlines"]
weather_msgs = ["weather", "current weather"]


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    if len(articles) == 0:
        print("Chatbot: No news available.")
        return

    print("Chatbot: Today's top news:")
    for i in range(5):
        print(f"{i+1}. {articles[i]['title']}")


def get_location():
    try:
        res = requests.get("http://ip-api.com/json/")
        data = res.json()
        return data.get("city"), data.get("lat"), data.get("lon")
    except:
        return None, None, None


def get_weather():
    city, lat, lon = get_location()

    if city is None:
        print("Chatbot: Location not detected.")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Chatbot: Could not fetch weather.")
        return

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    condition = data["weather"][0]["description"]

    print(f"Chatbot: Weather in {city}")
    print("Temperature:", temp, "°C")
    print("Feels like:", feels_like, "°C")
    print("Condition:", condition)


print("Smart Chatbot started...")
running = True

while running:
    user_msg = input("You: ").lower().strip()

    if user_msg in greet_msgs:
        print("Chatbot: Hi! How can I help?")

    elif user_msg in date_msgs:
        print("Chatbot:", datetime.now().date())

    elif user_msg in time_msgs:
        print("Chatbot:", datetime.now().strftime("%I:%M:%S %p"))

    elif "open" in user_msg:
        site = user_msg.split()[-1]
        print("Chatbot: Opening", site)
        webbrowser.open(f"https://www.{site}.com")

    elif any(word in user_msg for word in news_msgs):
        get_news()

    elif any(word in user_msg for word in weather_msgs):
        get_weather()

    elif "calculate" in user_msg:
        try:
            exp = user_msg.replace("calculate", "")
            print("Chatbot: Result =", eval(exp))
        except:
            print("Chatbot: Invalid calculation")

    elif user_msg in ["bye", "exit", "quit"]:
        print("Chatbot: Bye!")
        running = False

    else:
        print("Chatbot: Searching on Google...")
        webbrowser.open("https://www.google.com/search?q=" + user_msg)
