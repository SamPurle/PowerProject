"""

Powerlifting - Growth Plot:
    
    It is widely known that Powerlifting has experienced rapid growth in 
    recent years. This script can be used to quantify this growth.
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data

from Cleaning import df

DateData = df.groupby(['DateFirstMeet']).count()

dfPlot = pd.DataFrame({'Date' : DateData.index,
                        'Count' :DateData['Name']})

GrowthPlot = sns.distplot(df['DateFirstMeet'])
plt.show()