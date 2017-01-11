## Intro
As an abstract idea, saving for retirement seems like something that we should be doing automatically. In reality, the many expenses of real-life often get in the way, and at the month's end, after everything is budgeted and accounted for, there isn't much left to spare—maybe $100.

What about $100 though? In discussions about retirement as well as investing, two methods of funding are usually discussed: dollar-cost-averaging (DCA) and lumpsum investing. The first can be thought of as "spend $X dollars every so often" while the second, as the name suggests, is simply spending a large amount at once. Can saving $100 a month be as effective as investing $1000 all at once?

## Data with which to answer our question
To answer our question, we'll look at historical prices for Vanguard's 2055 target-date retirement fund, starting from 2012.

```python
import pandas as pd
import numpy as np

df = pd.read_csv(r'c:\resolve\projects\IRAs\v2055.csv')

# convert date column from string
df.Date = pd.to_datetime(df.Date)
# set the date column as the index
df.index = df.Date
df = df.sort_index(ascending=True)

In [122]: df.head(5)
Out[122]: 
                 Date      Close     y  m
Date                                     
2012-01-03 2012-01-03  22.230000  2012  1
2012-01-04 2012-01-04  22.200001  2012  1
2012-01-05 2012-01-05  22.180000  2012  1
2012-01-06 2012-01-06  22.110001  2012  1
2012-01-09 2012-01-09  22.160000  2012  1
```

Unlike stocks and other types of securities, target-date retirement funds (and mutual funds in general) only update their prices at the end of the day. This means that we'll just be using the closing price and ignoring the other price-related columns. Additionaly, columns for the week, month, and year were added to the file for grouping purposes.

## Making the tools that will give us the answer
Using this data, we'll create two functions corresponding to DCA and lumpsum investing. Given an annual budget, the functions return the total number of shares purchased over time.

The DCA function has been made to accomodate monthly as well as weekly savings targets through the ```interval``` argument. Depending on which option is selected, the dataframe is reduced to 12 or 52 rows of price info per year, which is then used to calculate the number of shares purchased. 

```python
def dca(amount, interval):
    '''
    amount = annual contribution
    interval = how often
    Returns total number of shares purchased
    '''
  
    if interval == 'week':
        i_week = pd.date_range('2012/1/1',periods=260,freq='7D') #generates date range by week
        i_week_filter = i_week[i_week < df.index[-1]]
        reduca = df.index.searchsorted(i_week_filter)  # .serachsorted helps align 2 arrays
        amount = amount/52
    elif interval == 'month':
        i_month = pd.date_range('2012/1/1',periods=60,freq='30D') #generates date range by month
        i_month_filter = i_month[i_month < df.index[-1]]
        reduca = df.index.searchsorted(i_month_filter)
        amount = amount/12
    else:
        print('Interval must be week or month')
        return
        
    df['shares'] = amount/df.Close[reduca]  # subsets df and gets # of shares purchased
    dfn = df.dropna()
    result = dfn.groupby('y')['shares'].sum()
    check = dfn.groupby(df.y).count()    
    #print('{shares} shares purchased using a {interval}ly budget of ${amount}.'.format(shares=result.sum(), interval=interval, amount=amount))
    print(result)
    return result.sum()
```

The lump sum function is much shorter as it only considers how much to put away each year. It uses prices from the end of each year but any other day would also work fine. 

```python
def lump(amount):
    df2 = df.groupby(df.y).last() # .last() reduces the groupby results to 1 row per group
    shares = 0
    shares_table = {}
    for i, row in df2.iterrows():
        shares_bought = amount/row.Close
        shares += shares_bought
        shares_table.update({i:shares_bought})
        #print('{0} - {1} shares bought at ${2}.'.format(i, shares_bought, shares))    
    x = pd.Series(shares_table)
    print(x)
    return x.sum()
```

## Results
Let's test both functions using a modest budget of $1000/year and a monthly interval for dollar cost averaging:

```python
In [123]: dca(1000, 'month')
175.93789361041246
Out[123]: 
y
2012    45.335818
2013    35.975445
2014    31.877293
2015    30.921921
2016    31.827417
Name: shares, dtype: float64

In [124]: lump(1000)
167.36289485793716
Out[124]: 
2012    40.322582
2013    32.948929
2014    31.269543
2015    32.435939
2016    30.385901
dtype: float64
```

In considering the results, we're going to be concerned with the total number of shares owned rather than dollar value. The dollar value of the fund still matters, of course, but since this discussion is about retirement accounts, we must recognize two things. First, holdings can't be sold until we are near retirement-age, which is a long way off. (Unless we take the penalty for withdrawing early, but that negates the benefit of using retirement accounts in the first place.) Second, if the holdings can't be sold until some time in the future, that free us to ignore the fluctuations of share prices. 

With that said, both methods seem similar in performance: a total of 175.94 shares for DCA and 167.36 for lump sum. A savings goal of $1000/year is a good place to start, but at a difference of only 8 shares, it seems that it doesn't matter which method is used. Let's use a larger amount and see how it affects things:

```python
In [118]: dca(5000, 'month')
879.6894680520625
Out[118]: 
y
2012    226.679090
2013    179.877223
2014    159.386465
2015    154.609603
2016    159.137087
Name: shares, dtype: float64

In [119]: lump(5000)
836.8144742896858
Out[119]: 
2012    201.612911
2013    164.744646
2014    156.347717
2015    162.179695
2016    151.929505
dtype: float64
```

This time the difference between them is more pronounced, about 43 shares in favor of DCA. Let's put the two side by side for an easier comparison:

```python
In [97]: compare = pd.DataFrame([DCA,lump_sum]).T

In [98]: compare.columns=['DCA','lump_sum']

In [99]: compare['pct_diff'] = compare.apply(lambda x: (x.DCA - x.lump_sum)/(np.mean([x.DCA, x.lump_sum])), axis=1)

In [100]: compare
Out[100]: 
             DCA    lump_sum  pct_diff
y                                     
2012  226.679090  201.612911  0.117052
2013  179.877223  164.744646  0.087821
2014  159.386465  156.347717  0.019249
2015  154.609603  162.179695 -0.047793
2016  159.137087  151.929505  0.046341
```

It seems that a large part of the difference in performanace happened in 2012 and 2013: DCA got 11.7% and then 8.8% more shares than lump sum. After that, the difference shrank to 1% and swung in favor of lump sum the last two years. The overall difference of 43 shares is only 5%, which seems rather small and possibly insignificant. The small size of our current dataset, which only goes back 5 years, is probably to blame. However, it's also a good idea to review the code for anything that might be affecting the results. To start, let's check the DCA function and the frequency that it purchases shares at. If it's working properly, there should be exactly 12 transactions per year since we selected the monthly interval.

```python
check = dfn.groupby(df.y).count()

In [128]: check
Out[128]: 
      Date  Close   y   m  shares
y                                
2012    13     13  13  13      13
2013    12     12  12  12      12
2014    12     12  12  12      12
2015    12     12  12  12      12
2016    12     12  12  12      12
```

Well that explains the 11.7% lead that DCA had in 2012: it bought an extra month's worth of shares. To correct this, we'll need to reevaluate how the data was reduced to monthly intervals. While we're making this change, we'd also benefit from switching to a different fund with a longer history.

## Revision

Instead of the target-date fund we started with, we will now use a old S&P 500 index fund and go back as far as 2000, which gives us three times the data:

```python
df = pd.read_csv(r'c:\resolve\projects\IRAs\vwelx.csv')

In [380]: df.head(5)
Out[380]: 
               y       Date      Close
Date                                  
2000-01-05  2000 2000-01-05  27.450001
2000-01-06  2000 2000-01-06  27.850000
2000-01-07  2000 2000-01-07  28.270000
2000-01-10  2000 2000-01-10  28.170000
2000-01-11  2000 2000-01-11  27.910000

In [2]: len(df)
Out[2]: 4275
```

After closer examination of the DCA function, it seemed that the method used for reducing the date range was off by 1 month.When applied to this larger dataset, it consistently put either 11 or 13 months into any given year. Re-writing the DCA function using a different method has fixed the problem:

```python
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

In [381]: check = dfn.groupby(df.y).count()

In [382]: check
Out[382]: 
       y  Date  Close  shares
y                            
2000  12    12     12      12
2001  12    12     12      12
2002  12    12     12      12
2003  12    12     12      12
2004  12    12     12      12
2005  12    12     12      12
2006  12    12     12      12
2007  12    12     12      12
2008  12    12     12      12
2009  12    12     12      12
2010  12    12     12      12
2011  12    12     12      12
2012  12    12     12      12
2013  12    12     12      12
2014  12    12     12      12
2015  12    12     12      12
2016  12    12     12      12
```
With that done, we can now compare saving for retirement via DCA and lump sum over a long period of time. Prior to correcting the DCA function, our comparison showed an overall difference of about 5%; with the spending between the two methods now even, there could be even less of a difference. However, the increased timespan may tilt the odds in favor of one or the other. Let's have a look, using an annual budget of $5000 and monthly interval:

```python
In [2]: compare
Out[2]: 
             DCA    lump_sum  pct_diff
y                                     
2000  180.727669  177.242119  0.019474
2001  176.916853  183.418929 -0.036089
2002  193.054997  203.583070 -0.053087
2003  192.949733  173.550856  0.105860
2004  170.275040  165.617749  0.027731
2005  164.246849  164.744646 -0.003026
2006  156.981207  154.178230  0.018016
2007  148.603369  153.280201 -0.030984
2008  174.073575  204.666394 -0.161551
2009  195.968517  173.310225  0.122716
2010  171.358680  160.771704  0.063752
2011  158.050740  159.540523 -0.009382
2012  149.564927  147.754137  0.012181
2013  135.316893  131.787036  0.026431
2014  126.924064  127.713914 -0.006204
2015  129.141811  135.906493 -0.051045
2016  131.586481  128.008189  0.027568
         2755.74     2745.07
```

## Conclusion
Our original question was whether saving $100 a month could be as effective as using $1200 all at once, and not only is it competitive, it turns out that it's sometimes even more effective. In the example above, 17 years of investing showed 9 years where dollar cost averaging yielded more shares than lump sum; at the end, it totaled ten shares ahead. At today's share price of $39.40, that would be a $394.00 difference. That said, the 10 share difference is less than 1%, which means that both investing methods are equally viable. Regardless of which one is used, for whatever reason or circumstance, the end result is practically the same for both.

## Areas for future study
An important factor to consider in evaluating the relatively close performance between DCA and lump sum is that 
transaction costs are not reflected in the functions. These vary depending on the platform used to fund the investments and no default value was substituted to account for them. If the DCA were to be refined further, this would be the first area to investigate. Paying whatever amount as a purchasing fee 12 or 52 times over the course of a year would certainly have a measurable effect on the results.

Besides transaction costs, another area for future study would be the dates used in the lump sum function. The main benefit to using the lump sum method is capturing a large number of shares at a good price. If the dates were set to correspond with annual lows from a given fund, thereby creating a best-case scenario, it would make for an interesting comparision to DCA. Alternatively, the dates could also be randomized to more closely reflect human behavior.