import requests
import logging

logging.basicConfig(format='%(asctime)s %(message)s', filename='fetch_stocks.log',level=logging.DEBUG)

logging.debug('Setting the API Key')
apikey="6PIRCZQQY12S49FR"

logging.info('------------------------- start calling service ')

dlh_stock_call = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=LHA.DE&apikey='+apikey)

logging.info('calling service finished')


dlh_stocks_json = dlh_stock_call.json()


dlh_stocks_lastrefreshed = dlh_stocks_json['Meta Data']['3. Last Refreshed']
logging.debug('the fetched data is from: ' + dlh_stocks_lastrefreshed)

dlh_stocks_data = dlh_stocks_json['Time Series (Daily)'][dlh_stocks_lastrefreshed]
print dlh_stocks_data['1. open'] +' -> '+ dlh_stocks_data['4. close']
