# Stock Data Extractor

## Overview

This project is a Python-based data extractor designed to scrape and gather stock information from various sources. It focuses on identifying the top losers of the day in the stock market and retrieving detailed financial data for these stocks. The data is then saved into CSV files for further analysis and strategy development.

## Features

- **Web Scraping**: Extracts stock data from a webpage listing the day's top losers.
- **API Integration**: Utilizes Alpha Vantage and Yahoo Finance APIs to gather detailed stock information.
- **Data Cleaning**: Processes and cleans the extracted data to focus on relevant financial metrics.
- **CSV Export**: Saves the processed data into CSV files for easy access and analysis.

## Code Explanation
### Web Scraping
The scrape_detail_page function scrapes a webpage(https://stockanalysis.com/robots.txt) to retrieve a table of the top losers in the stock market. It uses BeautifulSoup to parse HTML and extract table data into a Pandas DataFrame.
### API Data Retrieval
The script uses Alpha Vantage's API to fetch detailed stock information based on tickers obtained from the scraping process. It then cleans this data by removing unnecessary columns.
Additionally, Yahoo Finance's API (via yfinance) is used to obtain further financial statistics for each stock, which are stored in another CSV file.
### Data Storage
The cleaned and processed data is saved into two separate CSV files:
stock_info.csv: Contains basic information retrieved from Alpha Vantage.
stock_info2.csv: Contains additional financial metrics from Yahoo Finance.
## Usage
This tool is designed for traders or analysts looking to develop trading strategies based on daily market movements. By focusing on stocks that have lost value, users can potentially identify opportunities for investment or further research.
Limitations
The script relies on third-party APIs, which may have rate limits or require valid API keys.
The accuracy of the data depends on the reliability of the source websites and APIs.
The script assumes that the structure of the scraped webpage remains constant; changes in HTML structure may require updates to the scraping logic.
## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `yfinance`

You can install the required libraries using pip:

```bash
pip install -r requirements.txt