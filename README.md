# Pyhoo

_Yet another unofficial Yahoo Finance API library but with concurrent requests._

Pyhoo is **simple**:

```python
import pyhoo

tickers = ['FB', 'AAPL', 'AMZN', 'GOOGL']
start = '2020-02-01'
end = '2020-11-02'

stock_prices = pyhoo.get('chart', tickers, start=start, end=end, granularity="1d")
financial_reports = pyhoo.get('fundamentals', tickers, start=start, end=end)
options = pyhoo.get('options', tickers, start=start, end=end)
```

The result of `pyhoo.get` is a formatted `pandas.DataFrame` (here for stock prices):

|     |  timestamp |   high |    low |   volume |   open |  close | adjclose | currency | symbol | exchangeName | instrumentType | regularMarketPrice | ... |
| --: | ---------: | -----: | -----: | -------: | -----: | -----: | -------: | :------- | :----- | :----------- | :------------- | -----------------: | --: |
|   0 | 1580481000 | 208.69 | 201.06 | 31359900 | 208.43 | 201.91 |   201.91 | USD      | FB     | NMS          | EQUITY         |             286.95 | ... |
|   1 | 1580740200 | 205.14 |  202.5 | 15510500 | 203.44 | 204.19 |   204.19 | USD      | FB     | NMS          | EQUITY         |             286.95 | ... |
|   2 | 1580826600 |  210.6 |  205.2 | 19628900 | 206.62 | 209.83 |   209.83 | USD      | FB     | NMS          | EQUITY         |             286.95 | ... |
|   3 | 1580913000 | 212.73 | 208.71 | 12538200 | 212.51 | 210.11 |   210.11 | USD      | FB     | NMS          | EQUITY         |             286.95 | ... |
|   4 | 1580999400 | 211.19 | 209.34 | 10567500 | 210.47 | 210.85 |   210.85 | USD      | FB     | NMS          | EQUITY         |             286.95 | ... |
|   5 |        ... |    ... |    ... |      ... |    ... |    ... |      ... | ...      | ...    | ...          | ...            |                ... | ... |

Pyhoo is **fast**, it uses concurrency to fire multiple requests at the same time. You can request all the tickers of the S&P500 in one shot.

Pyhoo is **still in development**, feel free to add more endpoints thanks to the `Config` object !

Currently, it supports three endpoints:

1. `chart`, for [OHLC](https://en.wikipedia.org/wiki/Open-high-low-close_chart) data, basically stock prices
1. `fundamentals`, for financial data about the firm, see the [list of available reports](pyhoo/data/fundamentals_type_options.txt)
1. `options`, for detailed information on each call and put at each strike on specific tickers