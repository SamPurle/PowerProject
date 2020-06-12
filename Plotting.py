"""

Powerlifting - Plotting:
    
    Data visualisation using the Seaborn and matpplotlib libraries to make general visualisations of the overall dataset
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

sns.set_style('darkgrid')

# Load data

df = pd.read_csv('D:\DataSets\Powerlifting\CleanedData.csv', low_memory = False)
df['ElapsedTime'] = datetime.datetime(df['ElapsedTime'])
# Bin data for plotting

df['Years'] = df['ElapsedTime'].dt.days / 365
df['YearBin'] = pd.qcut(df['Years'], 250, labels = False, duplicates= 'drop')

dfBin = pd.DataFrame(df.groupby(['Sex','YearBin']).Years.mean()).reset_index()

    
dfBin['Wilks'] = df.groupby(['Sex','YearBin']).Wilks.mean().values
WilksPlot = sns.relplot(x = 'Years', y = 'Wilks', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot showing Wilks against Years Competing')
plt.show()

dfBin['Total'] = df.groupby(['Sex','YearBin']).TotalKg.mean().values
TotalPlot = sns.relplot(x = 'Years', y = 'Total', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot Showing Total against Years Competing')
plt.show()

dfBin['Bodyweight'] = df.groupby(['Sex','YearBin']).BodyweightKg.mean().values
WilksPlot = sns.relplot(x = 'Years', y = 'Bodyweight', hue = 'Sex', style= 'Sex', data = dfBin)
plt.title('Plot showing Bodyweight against Years Competing')
plt.show()
plt.savefig('\Page\assets\BodyweightPlot.png')