# Creating a function to download the data
def get_data(ticker,start,end,interval=None):
    ''' This function downloads data from yahoo finance. Syntax - get_data(ticker,start,end,interval=None)'''
    
    import yfinance as yf
    
    if interval:
        df= yf.download(ticker,start,end,interval= interval)
        
    else:
        df= yf.download(ticker,start,end)
        
    df.drop(columns=['Close'], inplace=True)
    df.rename(columns={'Adj Close':'close'}, inplace=True)
    df.columns= df.columns.str.lower()
    
    return df