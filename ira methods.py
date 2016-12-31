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

df = pd.read_csv(r'c:\resolve\projects\IRAs\v2055.csv')

# convert date column from string
df.Date = pd.to_datetime(df.Date)

# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)

def dca(budget, amount, interval):
    '''
    Purchases shares, spending $X at a time, up to a maximum.
    Tracks total number of shares purchased
    
    notes & issues:
    ===================
    - buying extra shares by making max go negative
    - [basic draft OK. still need to add something for interval of purchase]
    - [possible raw input options: week, month]
    - instead of using iterrows, subset and perform operations on subset
    
    
    - [add storage for shares purchased per year]  
    
    solved issues:
    ===================
    - [can't print a statement plus variables] SOLVED: used str(x)
    - [grouped data frame doesn't work with iterrows] SOLVED: added loop layer
    
    '''
    shares = 0
    shares_table = {}
    prices = []
    df1 = df[::interval].groupby(pd.TimeGrouper("A")) # subset/skip over X days and group by year
    
    
    for i, x in df1:    # i=year, x=dataframe
        max1 = budget  # for each year, contribution limit is 5500
        for e, row in x.iterrows():
            shares_bought = amount/row.Close    #basic transactional details
            max1 -= amount
            if max1 <= 0:
                break
            else:
                shares += shares_bought
                prices.append(row.Close)
                #shares_table[i.year] = {'shares':shares, 'price':row.Close,'date':row.Date}
                shares_table[i.year] = {'shares':shares}
    return shares_table
