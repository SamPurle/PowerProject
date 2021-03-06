"""

Powerlifting - Clustering Model:
    
    A Machine Learning Clustering model to classify competitions into different tiers of difficulty,
    with a view to providing better performance predictions. 
    
"""

# Import libraries

import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')

df = df.join(df.groupby(['Name']).MeetCountry.agg(pd.Series.nunique), on = 'Name', 
             how = 'left', rsuffix = 'Count') 

df = df.join(df.groupby('Name').MeetCountry.agg(pd.Series.mode), on = 'Name', 
             how = 'left', rsuffix = 'Mode')
df['Nationality'] = df['MeetCountryMode'].str[0]
df['Nationality'].replace(to_replace = {'England' : 'UK', 
                                        'Wales' : 'UK',
                                        'Scotland' : 'UK'}, inplace = True)
df.loc[df['Nationality'].str.len() > 1, 'MeetCountryMode'] = df['Nationality']

dfMeet = pd.DataFrame({'CompetitorCount' : df.groupby(['MeetName']).Name.count(),
                       'MedianWilks' : df.groupby(['MeetName']).Wilks.median(),
                       'MaxWilks' : df.groupby(['MeetName']).Wilks.max(),
                       'MeanCountries' : df.groupby(['MeetName']).MeetCountryCount.mean(),
                      'NationalityCount' : df.groupby(['MeetName']).MeetCountryMode.agg(pd.Series.nunique),
                      'MeanTrainingAge' : df.groupby(['MeetName']).ElapsedDays.mean()                      
                        })

xFeatures = ['MedianWilks', 'NationalityCount','MeanTrainingAge']
x = dfMeet[xFeatures]

Model = KMeans(n_clusters = 3, random_state = 42, n_jobs = 3).fit(x)
y = Model.labels_

dfMeet['MeetLevel'] = y
dfMeet['MeetLevel'].replace({0 : 'Beginner',
                             1: 'Intermediate',
                             2: 'Advanced'}, inplace = True)

ClusterPlot = sns.relplot(x = 'MedianWilks', y = 'NationalityCount', 
                          hue = 'MeetLevel', style = 'MeetLevel', data = dfMeet)

plt.show()