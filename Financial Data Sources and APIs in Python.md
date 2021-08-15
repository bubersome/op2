#### FRED

Before moving on, let's install the libraries used to access financial data sources:

```
pip install yfinance
pip install fredapi
pip install quandl
pip install world_bank_data
```

## Yahoo Finance API

Yahoo Finance allows users to access the stock quotes, up-to-date news, portfolio management resources, international market data, and more. In order to access this resource, we will first import the `yahoo-finance`library:

```
python
import yfinance as yf
```

In the following example, we will extract some stock data. To do that, we need to define `ticker`, which symbolizes the stock and date. Start time and end time define the time period in which we analyze the stock price. The `datetime` library is created to introduce these dates:

Let's extract the daily stock price of `Apple` between 01.01.2010-04.09.2020.

```
import datetime
stocks = 'AAPL'
start = datetime.datetime(2010,1,1)
end = datetime.datetime(2020,4,9)
```

Let's use `ticker`, `start`, and `end`dates and retrieve the daily Apple stock:

```
apple = yf.download(stocks,start=start,end = end, interval='1d')
```

Now we have the Apple stock price within specified period: 

```
apple.head()
```

We have open, high, low, close, and adjusted close prices and volume with date index.

## Federal Reserve Economic Data (FRED)

Using the FRED API, we are allowed to retrieve economic data from the FRED website hosted by the Economic Research Division of the Federal Reserve Bank of St. Louis.

As always, first import the `fredapi` Python library: 

```
from fredapi import Fred
```

In order to access the database, we need to have a unique `api_key`. Mine is 78b14ec6ba46f484b94db43694468bb1:

```
fred = Fred(api_key='78b14ec6ba46f484b94db43694468bb1')
```

Great, we are in! Let's retrieve economic growth data. Of the many versions of this, choose the one that serves your purpose best. How about searching it with `growth` keyword:

```
fred.search('growth')
```

For example, the data in the first row called `CPGDPAI`(percent change of gross domestic product) is the best option for me. Now, we filter this data. To do that, we type `fred.get_series('series id')`. `Series id`locates in the left-most part of the fred search result:

```
growth=fred.get_series('CPGDPAI')
```

All right, now let's see what the data looks like:

```

```

#### Quandl and the World Bank Database

## Quandl

Quandl is a source for financial, economic, and alternative datasets that is used worldwide. To access the data, our procedure is not very different from what we did for FRED. First, [visit their website](https://www.quandl.com/tools/api), and at the bottom of the page, click the Sign Up button. Follow the required steps to get the Quandl API.

Once we import `quandl`, we are ready to play with the data of our choice:

```
import quandl
```

We are ready to move on and retrieve `OIL` data:

```
oil=quandl.get("NSE/OIL", authtoken="sezjeVxkKghvxARoxQAo", start_date="2010-01-01", end_date="2020-01-01")
```

Let's see what the oil data looks like:

```
oil.head()
```

## The World Bank Database

I would like to introduce another database called the World Bank database, which is quite comprehensive and includes many development indicators. It is free and open access global development data and it is rather user friendly. Let's learn how to extract data from the World Bank Database.

As usual, first we import the required Python package, `wbdata`:

```
import world_bank_data as wb
```

Let's see which data sources the World Bank database has:

```
wb.get_sources()
```

It is obvious that this data is compherensive and includes different data sources. Before moving forward, we should define which one we want to work with. For the sake of practice, let's choose number 2, World Development Indicators (2 is the number of the data source).

To make a selection, specify the source number, which is denoted on the left of the databases. Once we denote the source number as 2, we have full list of variables that World Development Indicators includes:

```
wb.search_indicators('', source=2)
```

Suppose that we want to retrieve consumer price index data but do not know how to call it. Search a keyword, such as inflation or price. Then, to call the variable, we use the abbreviation to its left. Once we type `inflation` as a keyword, we have the following:

```
wb.search_indicators('inflation', source=2)
```

`FP.CPI.TOTL.ZG` is the input we feed the code while extracting the consumer prices. Now, it is time to decide which country to examine. Let's continue with the US, but I again do not know how to call it. Just typing a keyword for US will work again:

```
wb.search_countries('united')
```

So, `USA` is the abbreviation that we are to use. The final step before extracting the data is deciding the time interval. Suppose that our analysis period covers between 01-01-2010-onward. Using `wb.get_series`, we form our data for USA inflation: 

```
inf = wb.get_series('FP.CPI.TOTL.ZG', country='USA',date='2010:2020',id_or_value='id', simplify_index=True)
inf
```

Let's now try with multiple countries (in this example, Germany, Turkey, and France) and with different data (say per capita Gross Domestic Product). First, we search for the variable and the name of the countries:

```
wb.search_indicators('gdp', source=2)
```

`NY.GDP.PCAP.CD` is the short name of the `GDP per capita (current US$)`.

```
wb.search_countries('germany')
wb.search_countries('turkey')
wb.search_countries('france')
gdp = wb.get_series('NY.GDP.PCAP.CD',country=['DEU','TUR','FRA'],date='2010:2020',id_or_value='id', simplify_index=True)

gdp
```