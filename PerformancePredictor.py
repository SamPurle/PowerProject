"""

Powerlifting - Performance Predictor:
    
    A tool to estimate a competitor's ranking within a competition based on their weight, total, and comppetition
    
"""

#Import libraries

import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

# Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')


LevelMatches = df[(df['Sex'] == UserSex) & (df['WeightClassKg'] == UserWeightClass)
                  & (df['Meet Level'] == MeetLevel)]

# Calculate statistics

CountLower = LevelMatches[LevelMatches['TotalKg'] < UserTotal].Name.count()
CountTotal = len(LevelMatches)
Per = CountLower / CountTotal

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

dfRank = pd.DataFrame({'Rank' : np.linspace(1, Competitors, Competitors)}).astype(int)

for r in dfRank['Rank']:
    dfRank.loc[r-1,'Choose'] = nCr(Competitors, r - 1)
    dfRank.loc[r-1, 'Probability'] = dfRank.loc[r-1, 'Choose'] * (Per ** (Competitors - r)) * ((1 - Per) ** (r - 1))
    
PlacingPlot = sns.barplot(x = 'Rank', y = 'Probability', data = dfRank)
plt.title('Plot showing the probability distribution of your meet performance')
vals = PlacingPlot.get_yticks()
PlacingPlot.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
PlacingPlot.text(0.75,0.75,'{}\n{}kg Bodyweight\n{}kg Total\n{} Competitors \n{} level'.format(UserSex, UserBodyweight, UserTotal, Competitors, MeetLevel), transform = PlacingPlot.transAxes)
plt.savefig('docs/assets/PlacingPlot.png')
plt.show()

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
ProbPlot.text(0,15,'{}\n{}kg Bodyweight\n{}kg Total\n{} Competitors '.format(
    UserSex, UserBodyweight, UserTotal, Competitors))




    
    
