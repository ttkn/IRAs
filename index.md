title goes here
================

### Intro
As an abstract idea, saving for retirement seems like something that we should be doing automatically. In reality, the many expenses of real-life often get in the way, and at the month's end, after everything is budgeted and accounted for, there isn't much left to spare—maybe $100.

What about $100 though? In discussions about retirement as well as investing, two methods of funding are usually discussed: dollar-cost-averaging (dca) and lumpsum investing. The first can be thought of as "spend $X dollars every so often" while the second, as the name suggests, is simply spending a large amount at once. Can squirreling away $100 a month be as effective as investing it all at once?

### Data with which to answer our question
To answer our question, we'll look at historical prices for Vanguard's 2055 target-date retirement fund, starting from 2012.

'''python

import pandas as pd

df = pd.read_csv(r'c:\resolve\projects\IRAs\v2055.csv')

# convert date column from string
df.Date = pd.to_datetime(df.Date)
# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)

df.head(10)
Out[136]: 
               y  m       Date      Close  w
Date                                        
2012-01-03  2012  1 2012-01-03  22.230000  1
2012-01-04  2012  1 2012-01-04  22.200001  1
2012-01-05  2012  1 2012-01-05  22.180000  1
2012-01-06  2012  1 2012-01-06  22.110001  1
2012-01-09  2012  1 2012-01-09  22.160000  2
2012-01-10  2012  1 2012-01-10  22.389999  2
2012-01-11  2012  1 2012-01-11  22.389999  2
2012-01-12  2012  1 2012-01-12  22.459999  2
2012-01-13  2012  1 2012-01-13  22.340000  2
2012-01-17  2012  1 2012-01-17  22.469999  3
'''

Unlike stocks and other types of securities, target-date retirement funds (and mutual funds in general) only update their prices at the end of the day. This means that we'll just be using the closing price and ignoring the other price-related columns. Additionaly, columns for the week, month, and year were added to the file for grouping purposes.

### Making the tools that will give us the answer
Using this data, we'll create two functions corresponding to dca and lumpsum investing. Given an annual budget, the functions return the total number of shares purchased over time.

The dca function has been made to accomodate monthly as well as weekly savings targets through the '''interval''' argument. Depending on which option is selected, the '''amount''' is divided by 12 or 52 and then used to calculate the number of shares purchased. 

'''python
def dca(amount, interval):
    '''
    amount = annual contribution
    interval = how often
    Returns total number of shares purchased
    '''
  
    if interval == 'week':
        i_week = pd.date_range('2012/1/1',periods=260,freq='7D') #generates date range by week
        reduca = df.index.searchsorted(i_week)  # .serachsorted helps align 2 arrays
        amount = amount/52
    elif interval == 'month':
        i_month = pd.date_range('2012/1/1',periods=61,freq='30D') #generates date range by month
        reduca = df.index.searchsorted(i_month)
        amount = amount/12
    else:
        print('Interval must be week or month')
        return
        
    df['shares'] = amount/df.Close[reduca]  # subsets df and gets # of shares purchased
    dfn = df.dropna()
    result = dfn.groupby('y')['shares'].sum()
    result.index
    print('{shares} shares purchased using a {interval}ly budget of ${amount}.'.format(shares=result.sum(), interval=interval, amount=amount))
    return result
'''

A quick test with a modest budget:

'''python

In [155]: dca(1000,'month')
175.93789361041246 shares purchased using a monthly budget of $83.33.
Out[155]: 
year	shares
2012    45.335818
2013    35.975445
2014    31.877293
2015    30.921921
2016    31.827417
'''
