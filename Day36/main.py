

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

from datetime import datetime

today = datetime.now()
# print(today.strftime("%Y-%m-%d"))
yesterday = (int(today.strftime("%d")))- 1
yesterday_formatted = today.strftime(f"%Y-%m-{yesterday}")
# print(yesterday_formatted)

day_before_yesterday = (int(today.strftime("%d")))- 2
day_before_yesterday_formatted = today.strftime(f"%Y-%m-{day_before_yesterday}")
# print(day_before_yesterday_formatted)


import requests

API = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API
}

url = 'https://www.alphavantage.co/query'

stock_data = requests.get(url, params=stock_params)
stock_data.raise_for_status()
data = stock_data.json()['Time Series (Daily)']
print(data)

stock_yesterday = data[yesterday_formatted]["4. close"]
stock_day_before_yesterday = data[day_before_yesterday_formatted]["4. close"]
print(stock_yesterday)
print(stock_day_before_yesterday)

price_difference = float(stock_yesterday) - float(stock_day_before_yesterday)
print(f"Price difference: {price_difference}")
percent_diff = abs(price_difference / float(stock_yesterday) * 100)
print("Percent:" + str(percent_diff))



# def stock_changed():
if percent_diff == 5:
    print("Get news")
else:
    print("No significant change")


# STEP 2 GET NEWS: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = 'https://newsapi.org/v2/everything'
NEWS_API = ""  #insert api

# def get_news():
news_params = {
    "q": COMPANY_NAME,
    "from": yesterday_formatted,
    "to": day_before_yesterday_formatted,
    "language": "en",
    "sortBy": "relevancy",
    "pageSize": 3,
    "apiKey": NEWS_API,
}
request = requests.get(news_url, params=news_params)
request.raise_for_status()
news_data = request.json()
print(news_data)