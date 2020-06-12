"""

Powerlifting - Growth Plot:
    
    It is widely known that Powerlifting has experienced rapid growth in 
    recent years. This script can be used to quantify this growth.
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Load data

from Cleaning import df

df['Year'] = pd.DatetimeIndex(df['DateFirstMeet']).year

dfPlot['Year'] = pd.DataFrame(df['Year'].unique())
dfPlot['CompetitorCount'] = pd.groupby(df['Year']).count()[0]
