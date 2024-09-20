import pandas as pd
from dhanhq import marketfeed
import requests
import datetime


df = pd.read_csv('Dhan_Works/security.csv',low_memory = False)

today = datetime.datetime.today().date()

today_date = datetime.datetime.strftime(today,'%Y-%m-%d')

today_date

underlying = 'SENSEX'
exch = 'BSE'
instrument = 'INDEX'

underlying_s_id = df.loc[(df['SEM_EXM_EXCH_ID'] == exch) & (df['SEM_INSTRUMENT_NAME'] == instrument) & (df['SEM_TRADING_SYMBOL'] == underlying),'SEM_SMST_SECURITY_ID'].item()

underlying_s_id

instrument = 'OPTIDX'

today_date

df_opt = df.loc[(df['SEM_EXM_EXCH_ID'] == exch) & (df['SEM_INSTRUMENT_NAME'] == instrument) & (df['SEM_TRADING_SYMBOL'].str.startswith(underlying)) & (df['SEM_EXPIRY_DATE'].str.startswith(today_date)),:].copy()





df_opt



strike = 190

opt_s_id = df_opt.loc[(df_opt['SEM_STRIKE_PRICE']==190) & (df_opt['SEM_OPTION_TYPE'] == 'CE'),'SEM_SMST_SECURITY_ID'].item()

client_id = "1104088864"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzI5MTExMjIxLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwNDA4ODg2NCJ9.COQOjTvQ0Cmmjs660wwgYd1jnmi34_wla-keJue08L0-Gv4kGarBedXHOJ9i06kRprRqZOM4u1NtLleZcbKSRQ"

feed = marketfeed.DhanFeed(client_id = client_id, access_token = access_token, instruments = instruments)
feed.run_forever()
instruments = [(5,str(opt_s_id),15)]

instruments
response = feed.get_data()

ltp = eval(response['LTP'])
ltp
# buy_price = ltp
buy_price = 4.65

test = pd.DataFrame({'order_id':[],'buyPrice':[],'buyqty':[],'sell_price':[],'ltp':[],'remark' : []})
test.loc[len(test.index)] = ['t1',buy_price,1,None,ltp,None]

p = 0.05
p_l = -0.01
exit = False
while exit == False:
    response = feed.get_data()
    ltp = eval(response['LTP'])
    test.loc[test['order_id'] == 't1','ltp'] = ltp
    present_p = (ltp - buy_price)/ltp
    if present_p >= p:
        p = p + 0.05
        p_l = present_p
    if ltp-buy_price >= p*buy_price :
        test.loc[test['order_id'] == 't1','sell_price'] = ltp
        print('Sold')
        test.loc[test['order_id'] == 't1','remark'] ='Profit_Booked'
        print(test)
        exit = True
        break
    if ltp - buy_price <= p_l*buy_price:
        test.loc[test['order_id'] == 't1','ltp'] = ltp
        print('Sold')
        test.loc[test['order_id']=='t1','remark'] = 'Stop Loss'
        print(test)
        exit = True
        break
    print(test)
    print(f"Present Profit = {(ltp - buy_price)/(buy_price)}")
    print(f"Present Stop Loss = {p_l}")
    print(f"Present Target Profit = {p}")

feed.close_connection()
