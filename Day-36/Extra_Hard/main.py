import requests
import yaml
from twilio.rest import Client

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

# Reda env file
with open('.env') as f:
    Env = f.read()
    ENVS = yaml.safe_load(Env)
    STOCK_PRICE_API_KEY = ENVS['STOCK_PRICE_API_KEY']
    NEWS_API_KEY = ENVS['NEWS_API_KEY']
    TWILIO_PHONE_NUMBER = ENVS['TWILIO_PHONE_NUMBER']
    MY_PHONE_NUMBER = ENVS['MY_PHONE_NUMBER']


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&&interval=5min&apikey={STOCK_PRICE_API_KEY}'
r = requests.get(url)
data = r.json()

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
yesterday_data = data['Time Series (5min)']
yesterday_data_list = [value for (key, value) in yesterday_data.items()]
yesterday_closing_price = yesterday_data_list[0]['4. close']

# Get the day before yesterday's closing stock price
day_before_yesterday_data = yesterday_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

# Work out the percentage difference in price between closing price yesterday and closing price the day before
# yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    print('Get News')

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    news_api_key = ENVS['NEWS_API_KEY']
    news_url = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&sortBy=popularity&apiKey={NEWS_API_KEY}'
    news_r = requests.get(news_url)
    news_data = news_r.json()['articles']
    three_articles = news_data[:3]
    print(three_articles)

    # Use Python slice operator to create a list that contains the first 3 articles. Hint:
    # https://stackoverflow.com/questions/509211/understanding-slice-notation Create a new list of the first 3
    # articles headline and description using list comprehension.
    formatted_articles = [(f'{STOCK}: {up_down}{diff_percent}% Headline: {article["title"]}. '
                           f'Brief: {article["description"]}') for article in three_articles]
    print(formatted_articles)

    # Send each article as a separate message via Twilio.
    account_sid = ENVS['TWILIO_ACCOUNT_SID']
    auth_token = ENVS['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(message.status)


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
NVDA: 🔺2% Headline: ast year, NVIDIA unveiled DLSS 3 with frame interpolation, which used its AI-driven rendering 
accelerator to add extra frames to games. Now at Gamescom it's introducing DLSS 3.5, which adds Ray 
Reconstruction, a new feature that will use the company's neural…

or 

"NVDA: 🔻5% Headline: Valve may not have touched the Half-Life franchise in over a decade apart from releasing its 
VR-only game Alyx, but that isn't stopping enthusiasts from giving the game a visual overhaul. 
NVIDIA has unveiled a community-led Half-Life 2 RTX: An RTX Remix Proje….
"""
