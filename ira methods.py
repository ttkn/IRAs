'''
A look at different methods of funding IRAs: lump sum and dollar cost averaging.
Which purchasing method will yield more shares, the lump sum or dca?
'''

import pandas as pd
import numpy as np
import altair

df = pd.read_csv(r'c:\resolve\projects\IRAs\vwelx.csv') #index_col=['y','m','w'],skipinitialspace=True)

# convert date column from string
df.Date = pd.to_datetime(df.Date)
# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)

def dca(amount, interval):
    '''
    amount = annual contribution
    interval = how often
    Returns total number of shares purchased
    
    notes & issues:
    ===================
        
    solved issues:
    ===================
    - if using multi index, cannot set the index as date and do groupby year/month/etc
    - [if using resample, also can't group by y/m/etc] solved: create mask from resample
    - instead of using iterrows, subset and perform operations on subset

    
    failed grouping methods:
    ========================
    #df_month = df.groupby(['y', pd.Grouper(freq='m')]).first   # 'method' object is not iterable
    #df_month = df.resample('m').resample('a')
    #df_month = df.resample('m').first()'''
  
    if interval == 'week':
        # reduces df to week by week data
        mask = df.resample('W').index
        amount = amount/52

    elif interval == 'month':
        #reduces df to month by month data
        mask = df.resample('BM').index
        amount = amount/12     

    else:
        print('Interval must be week or month')
        return
    
    reduced_df = df.index.searchsorted(mask) # Find indices where elements should be inserted to maintain order
    df['shares'] = amount/df.Close[reduced_df]  # subsets df and gets # of shares purchased
    dfn = df.dropna()
    result = dfn.groupby('y')['shares'].sum()
    check = dfn.groupby(df.y).count()
    #print('{shares} shares purchased using a {interval}ly budget of ${amount}.'.format(shares=result.sum(), interval=interval, amount=amount))
    print(result.sum())
    return result

def lump(amount):
    df2 = df.groupby(df.y).last() # .last() returns the last line of each group
    shares = 0
    shares_table = {}
    for i, row in df2.iterrows():
        shares_bought = amount/row.Close
        shares += shares_bought
        shares_table.update({i:shares_bought})
        #print('{0} - {1} shares bought at ${2}.'.format(i, shares_bought, shares))    
    x = pd.Series(shares_table)
    print(x.sum())
    return x
    
compare = pd.DataFrame([DCA,lump_sum]).T
compare.columns=['DCA','lump_sum']
compare['pct_diff'] = compare.apply(lambda x: (x.DCA - x.lump_sum)/(np.mean([x.DCA, x.lump_sum])), axis=1)