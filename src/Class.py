import requests
from requests.api import head


class CryptoCurrency:

   URL = 'https://min-api.cryptocompare.com/data/{}'
   SINGLE_SYMBOL_URL = 'price?fsym={}&tsyms={}'
   MULTIPLE_SYMBOL_URL = 'pricemulti?fsyms={}&tsyms={},{},{}'
   
   def __init__(self, key=None):
      self.key = key

   def get_url(self, endpoint):
      return self.URL.format(endpoint)

   def get_request(self, url):
      headers = {'Apikey':self.key}
      return requests.get(url, headers=headers)


   def get_single_exchange_rate(self, currency_from, currency_to):
      endpoint = self.SINGLE_SYMBOL_URL.format(currency_from, currency_to)
      url = self.get_url(endpoint)
      response = self.get_request(url)
      if response.status_code == '200':
         return response.json()
      return response.text

   def get_multiple_exchange_rate(self, currency_from,first_currency_to, second_currency_to, tird_currency_to):
      endpoint = self.MULTIPLE_SYMBOL_URL.format(currency_from, first_currency_to,second_currency_to,tird_currency_to)
      url = self.get_url(endpoint)
      response = self.get_request(url)
      if response.status_code == '200':
         return response.json()
      return response.text

   
      

   

   
   