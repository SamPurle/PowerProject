"""

Powerlifting - Lift Dependency:
    
    How does the dependence on each lift vary throughout weight classes
    
"""

# Import libraries and modules

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv', index_col = 'Unnamed: 0')

# Calculate percentages

lifts = ['Squat', 'Bench', 'Deadlift']

for l in lifts:
    df['{}Per'.format(l)] = df['Best3{}Kg'.format(l)] / df['TotalKg']
    if 'dfLift' not in locals():
        dfLift = pd.DataFrame(df.groupby(['Sex', 'WeightClassKg'])['{}Per'.format(l)].mean())       
    else:
        dfLift = dfLift.join(pd.DataFrame(df.groupby(['Sex', 'WeightClassKg'])['{}Per'.format(l)].mean()))
        
# Add sex and weight class as columns for plotting purposes

dfLift = dfLift.join(dfLift.index.to_frame())

# Plot and save figures

SexDict = {'M' : 'Men',
           'F' : 'Women'}

for S in df['Sex'].unique():
    SexName = SexDict[S]
    dfPlot = dfLift.loc[S]
    dfPlot[:-1].plot(x = 'WeightClassKg', y = ['SquatPer','BenchPer','DeadliftPer'], kind = 'line')
    
    plt.title('Plot showing how Lift Dependency varies with Weight Class for {}'.format(SexName))
    plt.xlabel('Weight Class (kg)')
    plt.ylabel('Lift as a percentage of Total')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))    
    
    plt.savefig('docs/assets/{}_Dependency.png'.format(S))
    plt.show()
