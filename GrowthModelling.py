"""

Powerlifting - Growth:
    
    How has the sport grown as a whole in past years?
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv', 
                 index_col = 'Unnamed: 0')

# Convert data-type

df['YearFirstMeet'] = pd.to_datetime(df['DateFirstMeet']).dt.year

# Calculate variables

dfYear = pd.DataFrame(df.groupby(['YearFirstMeet']).Name.count())
dfYear['Year'] = dfYear.index
dfYear['Cumulative'] = dfYear['Name'].cumsum()

# Plot and save data

sns.set_style('darkgrid')
sns.relplot(x = 'Year', y = 'Cumulative', data = dfYear, kind = 'line')

MIN_YEAR = 2000 # Specify the starting year for the plot
X_TICK_FREQ = 5 # Specify the tick frequency on the x-axis
plt.xlim(MIN_YEAR,)
plt.xticks(np.arange(MIN_YEAR, dfYear['Year'].max() + X_TICK_FREQ, X_TICK_FREQ))

Y_TICK_FREQ = 50000 # Specify the tick frequeency on the y-axis
MAXCOMP = 250000 # Specify the maximum number of comppetitors for the plot to show
plt.ylim(0, MAXCOMP) 
plt.ylabel('Cumulative Competitors')

plt.title('Plot showing Cumulative Competitors over time')
plt.savefig('docs/assets/SportGrowth.png', bbox_inches = 'tight')

