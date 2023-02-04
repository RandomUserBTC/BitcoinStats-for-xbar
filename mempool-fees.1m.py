#!/Users/RandomUser/.pyenv/versions/3.11.1/bin/python
#coding=utf-8
#<xbar.title>Mempool Recommended Fees</xbar.title>
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

# 🟢 → Coin ticker 
coin_ticker = 'BTCUSDT'

# 🟣 → Retrieve recommended fees data from Mempool API
url_mempool_fees = "https://mempool.space/api/v1/fees/recommended"
payload_mempool_fees = urlopen(url_mempool_fees)
data_mempool_fees = json.loads(payload_mempool_fees.read().decode())

# 🟠 → Retrieve BTC/USDT data from Binance API
url_binanceapi_btc_usdt = "https://api.binance.com/api/v1/ticker/24hr?symbol={}".format(coin_ticker)
payload_binanceapi_btc_usdt = urlopen(url_binanceapi_btc_usdt)
data_binanceapi_btc_usdt = json.load(payload_binanceapi_btc_usdt)
btcusdt_price = int(float(data_binanceapi_btc_usdt['lastPrice']))
pct_change_btc_usdt = float(data_binanceapi_btc_usdt['priceChangePercent'])

# 🟠 → Convert Sat/vB to BTC
low_fee = data_mempool_fees['hourFee']
low_fee_btc = low_fee * 140 / 100000000
low_fee_usd = low_fee_btc * btcusdt_price

medium_fee = data_mempool_fees['halfHourFee']
medium_fee_btc = medium_fee * 140 / 100000000
medium_fee_usd = medium_fee_btc * btcusdt_price

high_fee = data_mempool_fees['fastestFee']
high_fee_btc = high_fee * 140 / 100000000
high_fee_usd = high_fee_btc * btcusdt_price

# 🟣 → Conditions for recommended low priority fee colors
if low_fee_usd <= 0.05:
    low_fee_color = 'lime'
elif low_fee_usd <= 0.2:
    low_fee_color = 'lightgreen'
elif low_fee_usd <= 0.4:
    low_fee_color = 'yellow'
elif low_fee_usd <= 0.6:
    low_fee_color = 'orange'
elif low_fee_usd <= 0.8:
    low_fee_color = 'salmon'
elif low_fee_usd <= 1.00:
    low_fee_color = 'tomato'
else:
    low_fee_color = 'red'

# 🟣 → Conditions for recommended medium priority fee colors
if medium_fee_usd <= 0.05:
    medium_fee_color = 'lime'
elif high_fee_usd <= 0.2:
    medium_fee_color = 'lightgreen'
elif high_fee_usd <= 0.4:
    medium_fee_color = 'yellow'
elif high_fee_usd <= 0.6:
    medium_fee_color = 'orange'
elif high_fee_usd <= 0.8:
    medium_fee_color = 'salmon'
elif high_fee_usd <= 1.00:
    medium_fee_color = 'tomato'
else:
    # 🟢 Any value above 1$
    medium_fee_color = 'red'

# 🟣 → Conditions for recommended high priority fee colors
if high_fee_usd <= 0.05:
    high_fee_color = 'lime'
elif high_fee_usd <= 0.2:
    high_fee_color = 'lightgreen'
elif high_fee_usd <= 0.4:
    high_fee_color = 'yellow'
elif high_fee_usd <= 0.6:
    high_fee_color = 'orange'
elif high_fee_usd <= 0.8:
    high_fee_color = 'salmon'
elif high_fee_usd <= 1.00:
    high_fee_color = 'tomato'
else:
    high_fee_color = 'red'

message_low_priority_fee = 'Low → {}丰 ({:.2f}$) | color={} | font={} | size={}'.format(low_fee, low_fee_usd, low_fee_color, font, size)
message_medium_priority_fee = 'Mid → {}丰 ({:.2f}$) | color={} | font={} | size={}'.format(medium_fee, medium_fee_usd, medium_fee_color, font, size)
message_high_priority_fee = 'High → {}丰 ({:.2f}$) | color={} | font={} | size={}'.format(high_fee, high_fee_usd, high_fee_color, font, size)

print(message_low_priority_fee)
print(message_medium_priority_fee)
print(message_high_priority_fee)