
from dotenv import load_dotenv
from embedchain import App

load_dotenv()

from embedchain import App 
from embedchain import Pipeline as App
import streamlit as st



bitcoin_bot = App()
bitcoin_bot.add("https://api.blockchair.com/news?q=language(en)", data_type='web_page')
bitcoin_bot.add('https://api.oraclus.com/v1/netflow/ethereum/?api_key=oraclus-5amp13-4p1-k3y-123456', data_type='web_page')
bitcoin_bot.add('https://oraclus.com/api-integration', data_type='docs_site')
bitcoin_bot.add('https://oraclus.com/api/wallet-analytics', data_type='docs_site')
bitcoin_bot.add('https://www.binance.com/en/feed/news/all?ads=true&utm_source=googleadwords_int&utm_medium=cpc&ref=HDYAHEES&gclid=CjwKCAiAvoqsBhB9EiwA9XTWGRVR5AQ_POkA112M50fYnnb-TpEjGH_6dcTMr3Bkqp5q49hmx6RlthoCUksQAvD_BwE', data_type='web_page')
bitcoin_bot.add('https://www.coindesk.com', data_type='web_page')
bitcoin_bot.add('https://coinmarketcap.com', data_type='web_page')



answer = bitcoin_bot.query('What happend with bitcoin in 2023?')

print(answer)