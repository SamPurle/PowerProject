"""

Powerlifting - Performance Predictor:
    
    A tool to estimate a competitor's ranking within a competition based on their weight, total, and comppetition
    
"""

# Import libraries

import pandas as pd
import seaborn as sns
import math
import numpy as np
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv('TimeData.csv')

# Recieve inputs

sex = 'M'
bw = [74]
tot = 520
Competitors = 20

# Clean weight classes

MaleWc = [20,53, 59, 66, 74, 83, 93, 105, 120, 260]
FemaleWc = [20, 43, 47, 52, 57, 63, 72, 84, 260]

if sex == 'M':
    WC = MaleWc
    
if sex == 'F':
    WC = FemaleWc

lab = [53, 59, 66, 74, 83, 93, 105, 120, 'SHW']

df['WC'] = pd.cut(df['BodyweightKg'], MaleWc, labels = lab)
df = df[df.loc[:,'Sex'] == sex]

# Filter by weightclass

wc = pd.cut(bw, MaleWc, labels = lab)    
df = df[df.loc[:,'WC'] == wc[0]]

CountTotal = len(df)
CountLower = df[df['TotalKg'] < tot]['CompetitorId'].count()
CountHigher = df[df['TotalKg'] > tot]['CompetitorId'].count()

# Calculate statistics

Per = CountLower / CountTotal

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

dfRank = pd.DataFrame(np.linspace(1, Competitors, Competitors))
dfRank.columns = ['Rank']
dfRank['Rank'] = dfRank['Rank'].astype(int)
dfRank['NumHigher'] = dfRank['Rank'] - 1
dfRank['NumLower'] = Competitors - dfRank['Rank']

for l in range(0,Competitors):
    dfRank.loc[l,'Choose'] = nCr(Competitors - 1, dfRank.loc[l,'NumLower'])
dfRank['Prob'] = dfRank['Choose'] * (Per ** dfRank['NumLower']) * ((1 - Per) ** dfRank['NumHigher'])
dfRank['Per'] = dfRank['Prob'] * 100

MaxProb = dfRank.loc[:,'Prob'].max()
MaxRow = dfRank[dfRank.loc[:,'Prob'] == MaxProb]
print('Based on historical data you are on the {:.0f}th percentile for lifters in your weight class, and it is most probable that you will take rank {}'.format(Per * 100, MaxRow.iloc[0,0]))

Top3 = dfRank.loc[0:2,'Prob'].sum()
Top1 = dfRank.loc[0,'Prob']
print('You have a {:.2%} chance of placing in the top 3, with a {:.2%} chance of winning your weight class'.format(Top3, Top1))

sns.set_style('darkgrid')
ProbPlot = sns.barplot(x = 'Rank', y = 'Per', data = dfRank)
plt.title('Probability distribution of placing at competition')
plt.ylabel('Percentage likelihood')
ProbPlot.text(0,15,'{}\n{}kg Bodyweight\n{}kg Total\n{} Competitors '.format(sex, bw[0], tot, Competitors))




    
    
