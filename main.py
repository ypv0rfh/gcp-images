import requests
import json
import pandas as pd

def fx_rates(data, context):
    api_key = 'J24I47N1ENVUXCS9'
    url = 'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&outputsize=full&&apikey=' + api_key
    api_call = requests.get(url)
    data = api_call.json()
    meta_data = pd.json_normalize(data['Meta Data'])
    fx_data = pd.DataFrame(data['Time Series FX (Daily)']).filter(items=['4. close'],axis=0).melt()
    fx_data['from_currency'] = meta_data['2. From Symbol'].to_string().replace('0','')
    fx_data['to_currency'] = meta_data['3. To Symbol'].to_string().replace('0','')
    fx_data.columns = ['date','fx_rate','from_currency','to_currency']
    fx_data.to_csv('gs://test_bucket_jesse/test.csv')
    print(fx_data.head(1))
