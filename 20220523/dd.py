req = requests.get(f'https://crix-api-endpoint.upbit.com/v1/crix/candles/{time_unit}?code=CRIX.UPBIT.KRW-{coin}&count=100&')
data = req.json()
result = []

for i, candle in enumerate(data):
    result.append({
        'Time'                 : data[i]["candleDateTimeKst"],
        'OpeningPrice'         : data[i]["openingPrice"],
        'HighPrice'            : data[i]["highPrice"],
        'LowPrice'             : data[i]["lowPrice"],
        'TradePrice'           : data[i]["tradePrice"],
        'CandleAccTradeVolume' : data[i]["candleAccTradeVolume"],
        'candleAccTraderPrice' : data[i]["candleAccTradePrice"]
    })
coin_data = pd.DataFrame(result)
coin_data.to_csv(f'{coin}_KRW_{time_unit}.csv')