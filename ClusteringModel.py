"""

Powerlifting - Clustering Model:
    
    A machine learning model to cluster meet data into regional, national and 
    international meets to improve predictions of competitive performance.
    
"""

# Import libraries

import pandas as pd 
import time
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

t0 = time.time()

# Load data

df = pd.read_csv('CleanedData.csv', index_col = 'Unnamed: 0')
dfMeet = pd.DataFrame({'MeetName' : df['MeetName'].unique()})
dfMeet['MedianWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.median().values)
dfMeet['MeanWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.mean().values)
dfMeet['CompetitorCount'] = pd.DataFrame(df.groupby(['MeetName']).Name.count().values)
dfMeet['MaxWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.max().values)

x1 = dfMeet['MedianWilks'].values
x2 = dfMeet['MeanWilks'].values


x = dfMeet[['MedianWilks','MaxWilks']]

k_means = KMeans(n_clusters = 3, random_state = 42)
y = k_means.fit_predict(x)



dfMeet['Meet Level'] = pd.DataFrame(y)
dfMeet['Meet Level'].replace(to_replace = [0, 1, 2], value = ['National', 'Regional', 'International'],
                                                              inplace = True)

distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=42
    )
    km.fit(x)
    distortions.append(km.inertia_)
    
# Plot clusters

sns.relplot(x = 'MaxWilks', y = 'MedianWilks', hue = 'Meet Level', data = dfMeet)
plt.title('Clustering of Competitions')
plt.xlabel('Maximum Wilks score')
plt.ylabel('Median Wilks score')
plt.show()

