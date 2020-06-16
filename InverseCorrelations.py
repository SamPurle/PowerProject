"""

Powerlifting - Inverse Correlations:
    
    A script to show inverse correlations between different lifts
    

"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')

# Isolate lifts

lifts = ['Squat', 'Bench', 'Deadlift']

for l in lifts:
    df['{}Per'.format(l)] = df['Best3{}Kg'.format(l)] / df['TotalKg']
    

for l in lifts:
    dfPlot = pd.DataFrame()
    LiftPlot = lifts.copy()
    LiftPlot.remove(l)
    for a in LiftPlot:
        dfPlot['{}'.format(a)] = df.groupby(['Best3{}Kg'.format(l)])['{}Per'.format(a)].mean().values
        
    CorPlot = sns.regplot(x = dfPlot.columns[0], y = dfPlot.columns[1], data = dfPlot)
    
    vals = CorPlot.get_yticks()
    CorPlot.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
    vals = CorPlot.get_xticks()
    CorPlot.set_xticklabels(['{:,.0%}'.format(x) for x in vals])
    
    plt.title('Plot showing how {} varies with {}'.format(dfPlot.columns[1], dfPlot.columns[0]))
    plt.xlabel('{} (% of Total)'.format(dfPlot.columns[0]))
    plt.ylabel('{} (% of Total)'.format(dfPlot.columns[1]))
    plt.savefig('docs/assets/{}-{}.png'.format(dfPlot.columns[0], dfPlot.columns[1]))
    plt.show()
    del dfPlot