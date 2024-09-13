import nest_asyncio
nest_asyncio.apply()

import marketfeed
import asyncio

client_id = "1104088864"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI3NTE5ODQzLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwNDA4ODg2NCJ9.XIKQpgBpDUa6CLjf67FjM-4c6lIfvURzU0Dob6RJIZUv3dyCmsZhXxiKMhSccdvCNdfPctU_vPSa6j8WclAfiA"

instruments = [(1, "1333"),(0,"13")]
subscription_code = marketfeed.Ticker

# Usage Example
async def on_connect(instance):
    print("Connected to websocket")

async def on_message(instance, message):
    print("Received:", message)

print("Subscription code :", subscription_code)
feed = marketfeed.DhanFeed(client_id, access_token, instruments, subscription_code,on_connect=on_connect, on_message=on_message)

feed.run_forever()

asyncio.create_task(feed.run_forever())
