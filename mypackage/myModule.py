import pandas as pd
import numpy as np
ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()
# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

# Function 1:

### START FUNCTION
def dictionary_of_metrics(items):
    """dictionary_of_metrics(items)
    
    Description:
    ------------
    This function calculates the mean, median, variance, standard deviation, minimum and maximum
    of a given list of numeric items. 
        
     Parameters:
     -----------
     items (list): list of numeric items.
        
     Return:
     -------
     (dict): the function return a dict with keys 'mean', 'median', 'std', 'var', 'min', and 'max',
      corresponding to the mean, median, standard deviation, variance, minimum and maximum of the input list, respectively. 
    """
    
    itemsort = sorted(items)
    return {"mean": round(np.mean(items),2),
            "median": round(np.median(items),2),
            "std": round(np.std(items, ddof=1),2),
            "var": round(np.var(items, ddof=1),2),
            "min": itemsort[0],
            "max": itemsort[-1]}
### END FUNCTION

# Function 2:

### START FUNCTION
def five_num_summary(items):
    
    """five_num_summary(items)
            
    Description:
    ------------
    This function calculates the five number summary from a given list of float or integers 
    and returns a dictionary five number summary.
        
    Parameters:
    -----------
    items (list): list of float / integers.
        
    Return:
    -------
    (dict): It returns a dictionary of the five number summary --> Q1, Q3,median, min , and max.  
    """
    sorteditems = sorted(items)
    return {'max': sorteditems[-1],
            'median': round(np.median(items),2) ,
            'min': sorteditems[0],
            'q1': np.percentile(sorteditems, 25),
            'q3': np.percentile(sorteditems, 75)}
### END FUNCTION
# Function 3:

### START FUNCTION
def date_parser(dates):
    
    """date_parser(dates)
            
    Description:
    ------------
    This function takes as input a list of these datetime strings and returns only the date in 'yyyy-mm-dd' format. 
           
    Parameters:
    -----------
    dates (list): list of datetime strings.
        
    Return:
    -------
    dates (list): list of dates strings.  
    """
    
    return [i.split(' ', 1)[0] for i in dates]
### END FUNCTION
# Funtion 4:

### START FUNCTION
def extract_municipality_hashtags(df):
    
    """
    Description:
    ------------
    This function returns a dataframe that adds a hastag and the municipality mentioned in the tweet
    
    Parameters:
    -----------
    (municpality, hashtags): a dataframe of municipality (dict) hashtags
    
    Return:
    ------
    a dataframe of municipality hashtags
    
    """
    contains_email = []
    hashtags = []
    for x in df["Tweets"]:
        contains_email.append([mun_dict[i] for i in x.split(' ') if i in mun_dict.keys()])
        hashtags.append([i.lower() for i in x.split(' ') if '#' in i])
    contains_email_nan = [i if i else np.nan for i in contains_email]
    hashtags_nan = [i if i else np.nan for i in hashtags]
    df["municipality"] = contains_email_nan
    df["hashtags"] = hashtags_nan
    return df
### END FUNCTION
# Funtion 5:

### START FUNCTION
def number_of_tweets_per_day(df):
    
    """
    Description:
    ------------
    This function takes a pandas dataframe as input and returns a modified dataframe with the number of tweets for that day.
    
    Parameters:
    -----------
    (Date, Tweets): a dataframe grouped by day
    
    Return:
    -------
    new dataframe, grouped by day, with the number of tweets for that day.
    """
    
    df["Date"] = [i.split(' ', 1)[0] for i in df["Date"]]
    a = sorted(list(df["Date"].unique()))
    dictp = {}
    for i in a:
        for x in df[df["Date"] == i]["Date"]:
            if x in dictp.keys():
                dictp[x] += 1
            else:
                dictp[x] = 1
    new_df = pd.DataFrame.from_dict(data=dictp, orient="index", columns=["Tweets"])
    new_df.index.name = "Date"
    return new_df
### END FUNCTION

# Funtion 6:

### START FUNCTION
def word_splitter(df):
    
    """
    Description:
    ------------
    This function takes a pandas dataframe as an input and splits Tweets into a list, stored in a new column.
    
    Parameter:
    ----------
    (Tweets, Split Tweets): a dataframe containing a column named 'Tweets'
    
    Return:
    -------
    a modified dataframe with a new column including a list of words.
    
    """
    meh = [list(i.lower().split(" ")) for i in df["Tweets"]]
    df["Split Tweets"] = meh
    df['Date'] = [i.split(' ', 1)[0] for i in df["Date"]]
    df['Tweets'] = [i.lower() for i in df["Tweets"]]
    return df
### END FUNCTION

# Funtion 7:

### START FUNCTION
def stop_words_remover(df):
    
    """
    Description:
    ------------
    This function takes a pandas dataframe as an input and modifies the 
    dataframe by removing all stop words from the predefined dictionary. 
    
    Parameter:
    ----------
    (stop_words_dict, "Without Stop Words"): a dataframe with words from a predefined dictionary removed.
    
    Return:
    -------
    a modified dataframe with stop words removed.
    
    """
    def hash_me(words):
        return [i for i in words.lower().split() if i not in stop_words_dict["stopwords"]]
    df["Without Stop Words"] = df["Tweets"].apply(hash_me)
    return df
### END FUNCTION



