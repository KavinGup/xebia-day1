from datetime import datetime
import webbrowser
import requests

# Corpus
greet_msgs = ["hi", "hello", "hey", "hi there", "hello there"]
date_msgs = ["date", "tell me date", "today's date"]
time_msgs = ["time", "tell me time", "current time"]
news_msgs = ["tell me news", "news", "headlines"]

# Function to get news
def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    for i in range(len(articles)):
        print(articles[i]['title'])

# Start chat
chat = True
print("Smart Chatbot: Hello! Ask me anything...")

while chat:
    user_msg = input("You: ").lower().strip()

    # Greetings
    if user_msg in greet_msgs:
        print("Chatbot: Hello User! How may I help you?")
    
    # Date
    elif user_msg in date_msgs:
        print(f"Chatbot: Today's date is: {datetime.now().date()}")
    
    # Time
    elif user_msg in time_msgs:
        current_time = datetime.now().time()
        print("Chatbot: Current time is:", current_time.strftime("%I:%M:%S %p"))
    
    # Open website
    elif "open" in user_msg:
        website_name = user_msg.split()[-1]
        url = f"https://www.{website_name}.com"
        print(f"Chatbot: Opening {website_name}...")
        webbrowser.open(url)
    
    # News
    elif any(word in user_msg for word in news_msgs):
        get_news()
    
    # Calculator
    elif "calculate" in user_msg:
        expression = user_msg.replace("calculate", "").strip()
        try:
            result = eval(expression)
            print(f"Chatbot: Result is: {result}")
        except Exception:
            print("Chatbot: Invalid expression. Example: 'calculate 5 + 3 * 2'")
    
    # Exit
    elif user_msg in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        chat = False
    
    # Default fallback
    else:
        print(f"Chatbot: I cannot understand '{user_msg}'. Searching Google...")
        webbrowser.open(f"https://www.google.com/search?q={user_msg}")
#ipapi
#openweather
#sqb-codes