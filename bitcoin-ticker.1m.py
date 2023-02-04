#!/Users/RandomUser/.pyenv/versions/3.11.1/bin/python
#coding=utf-8
#<xbar.title>BTC/USD + SAT/USD Price Ticker</xbar.title>
#<xbar.author>RandomUserBTC</xbar.author>
#<xbar.author.github>RandomUserBTC</xbar.author.github>
#<xbar.version>v1.0</xbar.version>
#<xbar.dependencies>python</xbar.dependencies>

import json
import time
from datetime import datetime
from urllib.request import urlopen

# 🟢 → Font and size
font = 'FiraCode'
size = 12

# 🟢 → Coin ticker and fiat ticker
coin_ticker = 'BTCUSDT'
fiat_ticker = 'USD-BRL'

# 🟠 → Retrieve BTC/USDT data from Binance API
url_binanceapi_btc_usdt = "https://api.binance.com/api/v1/ticker/24hr?symbol={}".format(coin_ticker)
payload_binanceapi_btc_usdt = urlopen(url_binanceapi_btc_usdt)
data_binanceapi_btc_usdt = json.load(payload_binanceapi_btc_usdt)
btcusdt_price = int(float(data_binanceapi_btc_usdt['lastPrice']))
pct_change_btc_usdt = pct_change_btc_usdt = float(data_binanceapi_btc_usdt['priceChangePercent'])

# 🟠 → Conditions for BTC/USD
if pct_change_btc_usdt > 0:
    last_price_color = 'lightgreen'
    message_btc_usdt = 'BTC/USD → {:,}$ (+{:.2f}%↑) | color={} | font={} | size={}'.format(btcusdt_price, pct_change_btc_usdt, last_price_color, font, size).replace(",", ".")
else:
    last_price_color = 'salmon'
    message_btc_usdt = 'BTC/USD → {:,}$ ({:.2f}%↓) | color={} | font={} | size={}'.format(btcusdt_price, pct_change_btc_usdt, last_price_color, font, size).replace(",", ".")
if pct_change_btc_usdt >= 5:
    last_price_color = 'lime'
    message_btc_usdt = 'BTC/USD → {:,}$ (+{:.2f}%↑) | color={} | font={} | size={}'.format(btcusdt_price, pct_change_btc_usdt, last_price_color, font, size).replace(",", ".")
elif pct_change_btc_usdt == 0: 
    last_price_color = 'orange'
    message_btc_usdt = 'BTC/USD → {:,}$ ({:.2f}%) | color={} | font={} | size={}'.format(btcusdt_price, pct_change_btc_usdt, last_price_color, font, size).replace(",", ".")
elif pct_change_btc_usdt <= -5: 
    last_price_color = 'red'
    message_btc_usdt = 'BTC/USD → {:,}$ ({:.2f}%↓) | color={} | font={} | size={}'.format(btcusdt_price, pct_change_btc_usdt, last_price_color, font, size).replace(",", ".")

# 🔵 → Convert USD to SATs
usd_price_in_sats = 100000000 / btcusdt_price
usd_price_in_sats = int(usd_price_in_sats)

# 🔵 → Conditions for SAT/USD Ticker
if pct_change_btc_usdt < 0:
    last_price_color = 'lightgreen'
    message_usd_in_sats = 'SAT/USD → {:,}丰 (+{:.2f}%↑) | color={} | font={} | size={}'.format(usd_price_in_sats, abs(pct_change_btc_usdt), last_price_color, font, size).replace(",", ".")
else:
    last_price_color = 'salmon'
    message_usd_in_sats = 'SAT/USD → {:,}丰 (+{:.2f}%↓) | color={} | font={} | size={}'.format(usd_price_in_sats, abs(pct_change_btc_usdt), last_price_color, font, size).replace(",", ".")
if pct_change_btc_usdt >= 5:
    last_price_color = 'red'
    message_usd_in_sats = 'SAT/USD → {:,}丰 (-{:.2f}%↓) | color={} | font={} | size={}'.format(usd_price_in_sats, abs(pct_change_btc_usdt), last_price_color, font, size).replace(",", ".")
elif pct_change_btc_usdt == 0:
    last_price_color = 'orange'
    message_usd_in_sats = 'SAT/USD → {:,}丰 (+{:.2f}%) | color={} | font={} | size={}'.format(usd_price_in_sats, abs(pct_change_btc_usdt), last_price_color, font, size).replace(",", ".")
elif pct_change_btc_usdt <= -5: 
    last_price_color = 'lime'
    message_usd_in_sats = 'SAT/USD → {:,}丰 (+{:.2f}%↑) | color={} | font={} | size={}'.format(usd_price_in_sats, abs(pct_change_btc_usdt), last_price_color, font, size).replace(",", ".")

print(message_btc_usdt)
print(message_usd_in_sats)
