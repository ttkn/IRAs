3.5.2 |Anaconda 4.2.0 (64-bit)| (default, Jul  5 2016, 11:41:13) [MSC v.1900 64 bit (AMD64)]
Python Type "help", "copyright", "credits" or "license" for more information.
[evaluate ira methods.py]
dca(2000,500,30)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
dca(2000,2000,30)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.7815550084695,
 2015: 389.37936212590904,
 2016: 455.23382159728015}
dca(2000,500,40)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
dca(2000,500,41)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
dca(2000,500,80)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
dca(2000,500,2)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
dca(2000,500,8)
{2011: 91.36592468551507,
 2012: 181.33443570665767,
 2013: 260.29219330634186,
 2014: 326.78155500846947,
 2015: 389.379362125909,
 2016: 455.23382159728}
for i, x in df1_year:    # i=year, x=dataframe
       # max1 = budget  # for each year, contribution limit is 5500
        x = x[::interval]
        print(x.head())

Traceback (most recent call last):
  Python Shell, prompt 9, line 3
builtins.NameError: name 'interval' is not defined
for i, x in df1_year:    # i=year, x=dataframe
       # max1 = budget  # for each year, contribution limit is 5500
        x = x[::30]
        print(x.head())

                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2011-12-29 2011-12-29  21.889999  21.889999  21.889999  21.889999       0   

            Adj Close  
Date                   
2011-12-29  20.390305  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2012-01-03 2012-01-03  22.230000  22.230000  22.230000  22.230000       0   
2012-02-15 2012-02-15  23.570000  23.570000  23.570000  23.570000       0   
2012-03-29 2012-03-29  24.250000  24.250000  24.250000  24.250000       0   
2012-05-11 2012-05-11  23.360001  23.360001  23.360001  23.360001       0   
2012-06-25 2012-06-25  22.570000  22.570000  22.570000  22.570000       0   

            Adj Close  
Date                   
2012-01-03  20.707012  
2012-02-15  21.955208  
2012-03-29  22.588621  
2012-05-11  21.759596  
2012-06-25  21.023718  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2013-01-02 2013-01-02  25.330000  25.330000  25.330000  25.330000       0   
2013-02-14 2013-02-14  26.120001  26.120001  26.120001  26.120001       0   
2013-04-01 2013-04-01  26.549999  26.549999  26.549999  26.549999       0   
2013-05-13 2013-05-13  27.709999  27.709999  27.709999  27.709999       0   
2013-06-25 2013-06-25  26.450001  26.450001  26.450001  26.450001       0   

            Adj Close  
Date                   
2013-01-02  24.034400  
2013-02-14  24.783993  
2013-04-01  25.191998  
2013-05-13  26.292665  
2013-06-25  25.097114  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2014-01-02 2014-01-02  30.080000  30.080000  30.080000  30.080000       0   
2014-02-14 2014-02-14  30.309999  30.309999  30.309999  30.309999       0   
2014-03-31 2014-03-31  30.870001  30.870001  30.870001  30.870001       0   
2014-05-13 2014-05-13  31.240000  31.240000  31.240000  31.240000       0   
2014-06-25 2014-06-25  32.189999  32.189999  32.189999  32.189999       0   

            Adj Close  
Date                   
2014-01-02  28.998009  
2014-02-14  29.219735  
2014-03-31  29.759593  
2014-05-13  30.116283  
2014-06-25  31.032110  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2015-01-02 2015-01-02  31.950001  31.950001  31.950001  31.950001       0   
2015-02-17 2015-02-17  32.860001  32.860001  32.860001  32.860001       0   
2015-03-31 2015-03-31  32.740002  32.740002  32.740002  32.740002       0   
2015-05-13 2015-05-13  33.470001  33.470001  33.470001  33.470001       0   
2015-06-25 2015-06-25  33.419998  33.419998  33.419998  33.419998       0   

            Adj Close  
Date                   
2015-01-02  31.334256  
2015-02-17  32.226718  
2015-03-31  32.109032  
2015-05-13  32.824962  
2015-06-25  32.775923  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2016-01-04 2016-01-04  30.370001  30.370001  30.370001  30.370001       0   
2016-02-17 2016-02-17  29.010000  29.010000  29.010000  29.010000       0   
2016-03-31 2016-03-31  31.070000  31.070000  31.070000  31.070000       0   
2016-05-12 2016-05-12  31.170000  31.170000  31.170000  31.170000       0   
2016-06-27 2016-06-27  30.180000  30.180000  30.180000  30.180000       0   

            Adj Close  
Date                   
2016-01-04  30.370001  
2016-02-17  29.010000  
2016-03-31  31.070000  
2016-05-12  31.170000  
2016-06-27  30.180000  
for i, x in df1_year:    # i=year, x=dataframe
       # max1 = budget  # for each year, contribution limit is 5500
        x = x[::3]
        print(x.head())

                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2011-12-29 2011-12-29  21.889999  21.889999  21.889999  21.889999       0   

            Adj Close  
Date                   
2011-12-29  20.390305  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2012-01-03 2012-01-03  22.230000  22.230000  22.230000  22.230000       0   
2012-01-06 2012-01-06  22.110001  22.110001  22.110001  22.110001       0   
2012-01-11 2012-01-11  22.389999  22.389999  22.389999  22.389999       0   
2012-01-17 2012-01-17  22.469999  22.469999  22.469999  22.469999       0   
2012-01-20 2012-01-20  22.889999  22.889999  22.889999  22.889999       0   

            Adj Close  
Date                   
2012-01-03  20.707012  
2012-01-06  20.595234  
2012-01-11  20.856050  
2012-01-17  20.930569  
2012-01-20  21.321795  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2013-01-02 2013-01-02  25.330000  25.330000  25.330000  25.330000       0   
2013-01-07 2013-01-07  25.299999  25.299999  25.299999  25.299999       0   
2013-01-10 2013-01-10  25.490000  25.490000  25.490000  25.490000       0   
2013-01-15 2013-01-15  25.500000  25.500000  25.500000  25.500000       0   
2013-01-18 2013-01-18  25.670000  25.670000  25.670000  25.670000       0   

            Adj Close  
Date                   
2013-01-02  24.034400  
2013-01-07  24.005934  
2013-01-10  24.186216  
2013-01-15  24.195705  
2013-01-18  24.357010  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2014-01-02 2014-01-02  30.080000  30.080000  30.080000  30.080000       0   
2014-01-07 2014-01-07  30.170000  30.170000  30.170000  30.170000       0   
2014-01-10 2014-01-10  30.299999  30.299999  30.299999  30.299999       0   
2014-01-15 2014-01-15  30.400000  30.400000  30.400000  30.400000       0   
2014-01-21 2014-01-21  30.379999  30.379999  30.379999  30.379999       0   

            Adj Close  
Date                   
2014-01-02  28.998009  
2014-01-07  29.084772  
2014-01-10  29.210095  
2014-01-15  29.306498  
2014-01-21  29.287217  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2015-01-02 2015-01-02  31.950001  31.950001  31.950001  31.950001       0   
2015-01-07 2015-01-07  31.469999  31.469999  31.469999  31.469999       0   
2015-01-12 2015-01-12  31.580000  31.580000  31.580000  31.580000       0   
2015-01-15 2015-01-15  31.299999  31.299999  31.299999  31.299999       0   
2015-01-21 2015-01-21  31.820000  31.820000  31.820000  31.820000       0   

            Adj Close  
Date                   
2015-01-02  31.334256  
2015-01-07  30.863505  
2015-01-12  30.971385  
2015-01-15  30.696781  
2015-01-21  31.206760  
                 Date       Open       High        Low      Close  Volume  \
Date                                                                        
2016-01-04 2016-01-04  30.370001  30.370001  30.370001  30.370001       0   
2016-01-07 2016-01-07  29.410000  29.410000  29.410000  29.410000       0   
2016-01-12 2016-01-12  29.219999  29.219999  29.219999  29.219999       0   
2016-01-15 2016-01-15  28.379999  28.379999  28.379999  28.379999       0   
2016-01-21 2016-01-21  28.129999  28.129999  28.129999  28.129999       0   

            Adj Close  
Date                   
2016-01-04  30.370001  
2016-01-07  29.410000  
2016-01-12  29.219999  
2016-01-15  28.379999  
2016-01-21  28.129999  
for i, x in df1_year:    # i=year, x=dataframe
       # max1 = budget  # for each year, contribution limit is 5500
        x = x[::3]
        print(type(x))

<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.frame.DataFrame'>
