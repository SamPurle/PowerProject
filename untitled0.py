"""

Powerlifting 3:
    
    Classification of lifters on based on their experience in a competitive environment
    
"""

# Impport libraries

import pandas as pd
import seaborn as sns

# Load data

df = pd.read_csv('TimeData.csv')
df = df[df.loc[:,'Sex'] == 'M']

df['Days'] = df.ElapsedTime.str.partition(' ').iloc[:,0]

df.loc[:,'Days'] = df.loc[:,'Days'].astype(int)

bins = pd.qcut(df.loc[:,'Days'], q = 250, duplicates = 'drop', labels = False)
df['bin'] = bins
cuts = bins.unique()

dfPlot = pd.DataFrame(columns = ['BinNumber','Years','AvgWilks','AvgTotal','Bodyweight'])

for c in cuts:
    dfBin = df[df['bin'] == c]
    dfPlot.loc[c,'BinNumber'] = c
    dfPlot.loc[c,'Years'] = (dfBin['Days'].mean()) / 365
    dfPlot.loc[c,'AvgWilks'] = dfBin['Wilks'].mean()
    dfPlot.loc[c,'AvgTotal'] = dfBin['TotalKg'].mean()
    dfPlot.loc[c,'Bodyweight'] = dfBin['BodyweightKg'].mean()

fig1 = sns.relplot(x = 'Years', y = 'AvgWilks', ci = 'sd', data = dfPlot)
fig1.set_axis_labels('Years Competing', 'Average Wilks')
