""" 

Powerlifting - Plotting:
    
    A script to plot trajectories of competitors throughout their lifting careers
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')

# Bin data for plotting

df['Years'] = df['ElapsedDays'] / 365
df['YearBin'] = pd.qcut(df['Years'], 250, labels = False, duplicates= 'drop')

dfBin = pd.DataFrame(df.groupby(['Sex','YearBin']).Years.mean()).reset_index()

    
dfBin['Wilks'] = df.groupby(['Sex','YearBin']).Wilks.mean().values
WilksPlot = sns.relplot(x = 'Years', y = 'Wilks', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot showing Wilks against Years Competing')
plt.savefig('docs/assets/WilksPlot.png', bbox_inches = 'tight')
plt.show()


dfBin['Total'] = df.groupby(['Sex','YearBin']).TotalKg.mean().values
TotalPlot = sns.relplot(x = 'Years', y = 'Total', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot Showing Total against Years Competing')
plt.savefig('docs/assets/TotalPlot.png', bbox_inches = 'tight')
plt.show()

dfBin['Bodyweight'] = df.groupby(['Sex','YearBin']).BodyweightKg.mean().values
BodyweightPlot = sns.relplot(x = 'Years', y = 'Bodyweight', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot showing Bodyweight against Years Competing')
plt.savefig('docs/assets/BodyweightPlot.png', bbox_inches = 'tight')
plt.show()