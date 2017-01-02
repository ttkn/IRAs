'''
A look at different methods of funding IRAs: lump sum and dollar cost averaging.

The idea of "returns" as it pertains to stocks and retirement seems misguided: defined as an increase in the trading price of the stock since initial purchase, celebrating this is useless because the increase is not "locked in" unless the stock is sold.

The true measure of your IRA's performance is number of shares.
Under current IRS rules, the annual limit for contributions is $5500
Which purchasing method will yield more shares, the lump sum or dca?
'''

import pandas as pd
import numpy as np
from datetime import datetime, date, time

df = pd.read_csv(r'c:\resolve\projects\IRAs\v2055.csv') #index_col=['y','m','w'],skipinitialspace=True)

# convert date column from string
df.Date = pd.to_datetime(df.Date)
# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)

def dca(amount, interval='week'):
    '''
    amount = how much to spend at a time
    interval = how often
    Returns total number of shares purchased
    
    notes & issues:
    ===================
    - if using multi index, cannot set the index as date and do groupby year/month/etc
    - if using resample, also can't group by y/m/etc
    
    '''
    '''solved issues:
    ===================
    [basic draft OK. still need to add something for interval of purchase]
    - [possible raw input options: week, month]
    - instead of using iterrows, subset and perform operations on subset
    - [can't print a statement plus variables] SOLVED: used str(x)
    - [grouped data frame doesn't work with iterrows] SOLVED: added loop layer
    - [add storage for shares purchased per year]  
    '''
    shares = 0
    shares_table = {}
    prices = []
    #df_week = df.groupby()
    #df_month = df.groupby(['y', pd.Grouper(freq='m')]).first   # 'method' object is not iterable
    #df_month = df.resample('m').resample('a')
    df_month = df.resample('m').first()
    if interval == 'week':
        df1 = df_week
    elif interval == 'month':
        df1 = pd.DataFrame(df_month).groupby('y')
    else:
        print('Interval must be week or month')
    
    def buy(x):
        shares_bought = amount/x
        return shares_bought
    def track(x):
        limit += amount
        return limit
    df['shares'] = df.Close.apply(buy)
    
    for eh, x in df1:    # i=year, x=dataframe
        limit = 0       # limit resets every year
    
        for e, row in x.iterrows(): # for each row in 2012+
            if limit < 5500:
                shares_bought = amount/row.Close    #basic transactional details
                limit += amount
                shares += shares_bought
                print('{0} - {1} shares. ${2} spent'.format(row.Date, shares, limit))
                
                #else: # for each year, contribution limit is 5500
                    #amount_adj = limit - 5500
                    #shares += (amount + amount_adj)/row.Close
                    #print('{0} - {1} shares. ${2} spent'.format(e.year, shares, limit))
                    
                
        return shares

def lump(amount):
    df2 = df.groupby(df.y).last() # .last() returns the last line of each group
    shares = 0
    for i, row in df2.iterrows():
        shares_bought = amount/row.Close
        shares += shares_bought
        print('{0} - {1} shares bought. {2} shares total.'.format(i, shares_bought, shares))    
def buy(x):
    limit = 0
    while limit < 5500:
        shares_bought = 2000/x
        limit += 2000
        return shares_bought
    
dca(800, 'month')