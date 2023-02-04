#!/Users/RandomUser/.pyenv/versions/3.11.1/bin/python
#coding=utf-8
#<xbar.title>Last Bitcoin Block + Mempool Unconfirmed Tx</xbar.title>
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

# 🟣 → Retrieve last block height from Mempool API
url_mempool_last_block = "https://mempool.space/api/blocks/tip/height"
payload_mempool_last_block = urlopen(url_mempool_last_block)
mempool_last_block = json.loads(payload_mempool_last_block.read().decode())

# 🟣 → Retrieve unconfirmed transactions from Mempool API
url_unconfirmed_transactions = "https://mempool.space/api/mempool" 
payload_unconfirmed_transactions = urlopen(url_unconfirmed_transactions)
data_unconfirmed_transactions = json.loads(payload_unconfirmed_transactions.read().decode())
unconfirmed_transactions = data_unconfirmed_transactions['count']

# 🟣 → Conditions for unconfirmed transactions colors
if unconfirmed_transactions < 1000:
    unconfirmed_transactions_color = 'lime'
elif unconfirmed_transactions <= 2500:
    unconfirmed_transactions_color = 'lightgreen'
elif unconfirmed_transactions <= 5000:
    unconfirmed_transactions_color = 'yellow'
elif unconfirmed_transactions <= 8000:
    unconfirmed_transactions_color = 'orange'
elif unconfirmed_transactions <= 10000:
    unconfirmed_transactions_color = 'salmon'
elif unconfirmed_transactions <= 15000:
    unconfirmed_transactions_color = 'tomato'
else:
    unconfirmed_transactions_color = 'red'

# 🟣 → Retrieve last block data from Mempool API
url_last_block_info = f"https://mempool.space/api/v1/blocks/" + str(mempool_last_block)
payload_last_block_info = urlopen(url_last_block_info)
data_last_block_info = json.loads(payload_last_block_info.read().decode())
last_block_timestamp = data_last_block_info[0]['timestamp']
convert_timestamp = datetime.fromtimestamp(last_block_timestamp)
current_datetime = datetime.now()
time_since_last_block = current_datetime - convert_timestamp

# 🟣 → Conditions for last block color
if time_since_last_block.total_seconds() < 60: 
    last_block_color = 'lime'
    block_time = 'Now'
elif time_since_last_block.total_seconds() < 660: 
    last_block_color = 'lightgreen'
    m = int(time_since_last_block.total_seconds() / 60)
    block_time = f'{m} min'
elif time_since_last_block.total_seconds() <= 1260: 
    last_block_color = 'yellow'
    m = int(time_since_last_block.total_seconds() / 60)
    block_time = f'{m} min'
elif time_since_last_block.total_seconds() <= 1860: 
    last_block_color = 'orange'
    m = int(time_since_last_block.total_seconds() / 60)
    block_time = f'{m} min'
elif time_since_last_block.total_seconds() <= 2760: 
    last_block_color = 'salmon'
    m = int(time_since_last_block.total_seconds() / 60)
    block_time = f'{m} min'
elif time_since_last_block.total_seconds() < 3660:
    last_block_color = 'tomato'
    m = int(time_since_last_block.total_seconds() / 60)
    block_time = f'{m} min'
else:
    last_block_color = 'red'
    h = int(time_since_last_block.total_seconds() / 3600)
    block_time = f'{h} hour'
    if h > 1:
        block_time = f'{h} hours'

message_last_block = 'Block → {:,} ({}) | color={} | font={} | size={}'.format(mempool_last_block, block_time, last_block_color, font, size).replace(",", ".")
message_unconfirmed_transactions = 'Unconfirmed Tx → {:,} | color={} | font={} | size={}'.format(unconfirmed_transactions, unconfirmed_transactions_color, font, size).replace(",", ".")

print(message_last_block)
print(message_unconfirmed_transactions)