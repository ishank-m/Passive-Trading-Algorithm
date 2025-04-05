import yfinance as yf, time


state: str = None       #current state of buy/sell/hold of the stock
range: list = []        #range=[min,max]
target_low: int = None
target_high: int = None


def dynamic_range():
    global range
    while True:
        ticker = yf.Ticker("NVDA")
        data = ticker.history(period = "1d", interval = "1m")
        current_price = float(data["Close"].iloc[-1])
        range = [current_price-1, current_price+1]
        print(range)
        time.sleep(60)

dynamic_range()


