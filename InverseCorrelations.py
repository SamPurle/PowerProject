"""

Powerlifting - Inverse Correlations:
    
    A script to show inverse correlations between different lifts
    

"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import rankdata as rank
import numpy as np

sns.set_style('darkgrid')

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')

# Isolate lifts

lifts = ['Squat', 'Bench', 'Deadlift']

for l in lifts:
    df['{}Per'.format(l)] = df['Best3{}Kg'.format(l)] / df['TotalKg']
    df['{}Percentile'.format(l)] = rank(df['Best3{}Kg'.format(l)]) / len(df)
    df['{}Percentile'.format(l)] = df['{}Percentile'.format(l)].round(2) * 100
    
    

# for l in lifts:
#     dfPlot = pd.DataFrame()
#     LiftPlot = lifts.copy()
#     LiftPlot.remove(l)
#     for a in LiftPlot:
#         dfPlot['{}'.format(a)] = df.groupby(['Best3{}Kg'.format(l)])['{}Per'.format(a)].mean().values
        
#     CorPlot = sns.regplot(x = dfPlot.columns[0], y = dfPlot.columns[1], data = dfPlot)
    
#     vals = CorPlot.get_yticks()
#     CorPlot.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
#     vals = CorPlot.get_xticks()
#     CorPlot.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
    
#     plt.title('Plot showing how {} varies with {}'.format(dfPlot.columns[1], dfPlot.columns[0]))
#     plt.xlabel('{} (% of Total)'.format(dfPlot.columns[0]))
#     plt.ylabel('{} (% of Total)'.format(dfPlot.columns[1]))
#     plt.savefig('docs/assets/{}-{}.png'.format(dfPlot.columns[0], dfPlot.columns[1]))
#     plt.show()
#     del dfPlot

for l in lifts:
    dfPlot = pd.DataFrame()
    LiftPlot = lifts.copy()
    LiftPlot.remove(l)
    xLift = LiftPlot[0]
    yLift = LiftPlot[1]
    
    # Generate DataFrame for plotting
    
    dfPlot = pd.DataFrame(df.groupby('{}Percentile'.format(xLift))['{}Percentile'.format(yLift)].mean())
    dfPlot = dfPlot.join(dfPlot.index.to_frame())
    
    # Create plot
    
    Plot = sns.regplot(x = '{}Percentile'.format(xLift), y = '{}Percentile'.format(yLift), data = dfPlot)
    plt.title('Plot showing the relationship between {} and {}'.format(xLift, yLift))       
    
    # Format correctly
    
    plt.xlabel(xLift + ' Percentile')
    plt.xlim(0,100)
    
    plt.ylabel(yLift +' Percentile')
    plt.ylim(0,100)
    
    # Add equality line
    
    plt.plot(np.arange(0,100),np.arange(0,100))   
    plt.savefig('docs/assets/{}-{}.png'.format(xLift, yLift))
    plt.show()
    
  
    
    
        

            