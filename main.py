import requests
from bs4 import BeautifulSoup
import pandas as pd
import yfinance as yf
import creds

# this function scrapes the webpage and returns the data in dataframe format
def scrape_detail_page(url):
    try :
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Failed to fetch page: {response.status_code}')
            return None
        # scraping the table imbedded in the webpage to retrieve the top losers stock of the day
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table', class_ = 'symbol-table svelte-eurwtr')
        headers = table.find_all('th')
        titles = []
        # using the first row of the table to get the column names
        for i in headers:
            title = i.text
            titles.append(title)

        # creating a dataframe to store the data
        df = pd.DataFrame(columns = titles)
        rows = table.find_all('tr')
        # using the rest of the rows to get the data one by one
        for i in rows[1:]:
            data = i.find_all('td')
            row = [tr.text for tr in data]
            length = len(df)
            df.loc[length] = row

        df = df.iloc[:, :-2]
        return df   
        
    except Exception as e:
        print(f'Failed to fetch page: {e}')
        return None
         
url1 = 'https://stockanalysis.com/markets/losers/'   
data = scrape_detail_page(url1)
data.drop(data.columns[0], axis = 1, inplace = True)
# creating a new dataframe to store a new data set which update daily for the top losers stock of the day
# we are creating a new dataset which is updated daily and unique for the certain trading strategies
info = pd.DataFrame()
# iterating over the stock tickers to get the stock information form the API
for value in data.iloc[:, 0]:
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={value}&apikey={creds.API_KEY}'
    raw = requests.get(url).json()
    info = info._append(pd.DataFrame(raw, index = [0]))

# cleaning the data
info.drop(['Description'], axis = 1, inplace = True)
info.drop(['Address'], axis = 1, inplace = True)
info.drop(['AssetType'], axis = 1, inplace = True)
info.drop(['CIK'], axis = 1, inplace = True)
info.drop(['Industry'], axis = 1, inplace = True)
info.drop(['OfficialSite'], axis = 1, inplace = True)
info.drop(['Sector'], axis = 1, inplace = True)
info.drop(['RevenueTTM'], axis = 1, inplace = True)
info.drop(['Beta'], axis = 1, inplace = True)
info.drop(['PERatio'], axis = 1, inplace = True)

# saving the data to a csv file
info.to_csv('stock_info.csv', index = False)

# creating a new dataset using yfinance api to get additional stock information which is going to be used for the analysis.
stats_to_retrieve = [
    'totalRevenue', 'marketCap', 'enterpriseValue', 'asets'
    'profitMargins', 'operatingMargins', 'returnOnAssets', 'returnOnEquity',
    'revenuePerShare', 'quarterlyRevenueGrowth', 'grossMargins',
    'ebitdaMargins', 'operatingCashflow', 'freeCashflow',
    'earningsGrowth', 'currentRatio', 'quickRatio',
    'debtToEquity', 'beta'
]
# creating a list to store the data
data_list = []
# iterating over the stock tickers to get the stock information form the API
for value in data.iloc[:, 0]:
    # Fetch data for each ticker
    stock = yf.Ticker(value)
    info = stock.info
    
    # Extract the relevant statistics
    data = {stat: info.get(stat, None) for stat in stats_to_retrieve}
    
    # Add the ticker symbol to the data
    data['Symbol'] = value
    
    # Append the data dictionary to the list
    data_list.append(data)
# creating a new dataframe to store the data
df2 = pd.DataFrame(data_list)
df2.to_csv('stock_info2.csv', index = False)


         