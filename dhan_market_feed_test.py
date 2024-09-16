from dhanhq import marketfeed
import pandas as pd


client_id = '1104088864'
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI2NTE2MzkwLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwNDA4ODg2NCJ9.1ro6-2OzEiDH2XhaImfzGXBOF6ZR6OkxZ6cOn4xG0A7itc_AvdlXuIKAoJNsSxIgTVr924xUi37Ko9pqip1nzg'

security_url = "https://images.dhan.co/api-data/api-scrip-master.csv"

df = pd.read_csv(security_url,low_memory = False)

df.head()

df['SEM_INSTRUMENT_NAME'].unique()

df['SEM_EXM_EXCH_ID'].unique()

df.loc[(df['SEM_EXM_EXCH_ID'] == 'MCX') & df['SEM_TRADING_SYMBOL'].str.startswith('NATURALGAS'),:].head()



instruments = [(5,'430268',15)]

data = marketfeed.DhanFeed(client_id = client_id, access_token = access_token, instruments = instruments)
data.run_forever()

import time

start = time.time()
for i in range(0,10):
    data.get_data()
print(f"Time Taken = {time.time() - start}")
data.close_connection()


import asyncio
import websockets

asyncio def test():
    async with connect(f"wss://api-feed.dhan.co?version=2&token={access_token}&clientId={client_id}&authType=2") as w:
        await.send('hello')

k = {
    "RequestCode" : 15,
    "InstrumentCount" : 2,
    "InstrumentList" : [
        {
            "ExchangeSegment" : "NSE_EQ",
            "SecurityId" : "1333"
        },
        {
            "ExchangeSegment" : "BSE_EQ",
            "SecurityId" : "532540"
        }
    ]
}



