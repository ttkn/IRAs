'''
A look at different methods of funding IRAs: lump sum and dollar cost averaging.

The idea of "returns" as it pertains to stocks and retirement seems misguided: defined as an increase in the trading price of the stock since initial purchase, celebrating this is useless because the increase is not "locked in" unless the stock is sold.

The true measure of your IRA's performance is number of shares.
Under current IRS rules, the annual limit for contributions is $5500
Which purchasing method will yield more shares, the lump sum or dca?
'''

import pandas as pd

df = pd.read_csv(r'c:\resolve\projects\IRAs\v2055.csv') #index_col=['y','m','w'],skipinitialspace=True)

# convert date column from string
df.Date = pd.to_datetime(df.Date)
# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)


def dca(amount, interval='week'):
    '''
    amount = annual contribution
    interval = how often
    Returns total number of shares purchased
    
    notes & issues:
    ===================
    - if using multi index, cannot set the index as date and do groupby year/month/etc
    - if using resample, also can't group by y/m/etc
    
    solved issues:
    ===================
    [basic draft OK. still need to add something for interval of purchase]
    - [possible raw input options: week, month]
    - instead of using iterrows, subset and perform operations on subset
    - [can't print a statement plus variables] SOLVED: used str(x)
    - [grouped data frame doesn't work with iterrows] SOLVED: added loop layer
    - [add storage for shares purchased per year]  
    
    failed grouping methods:
    ========================
    #df_week = df.groupby()
    #df_month = df.groupby(['y', pd.Grouper(freq='m')]).first   # 'method' object is not iterable
    #df_month = df.resample('m').resample('a')
    #df_month = df.resample('m').first()'''
  
    if interval == 'week':
        i_week = pd.date_range('2012/1/1',periods=60,freq='7D') #generates date range by week
        reduca = df.index.searchsorted(i_week)  # .serachsorted helps align 2 arrays
        amount = amount/52
    elif interval == 'month':
        i_month = pd.date_range('2012/1/1',periods=60,freq='30D') #generates date range by month
        reduca = df.index.searchsorted(i_month)
        amount = amount/12
    else:
        print('Interval must be week or month')
        
    df['shares'] = amount/df.Close[reduca]  # subsets df and gets # of shares purchased
    ok = df.dropna()
    result = ok.groupby('y').sum()
    return result

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
