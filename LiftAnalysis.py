"""

Powerlifting - Lift Analysis:
    
    A script to show a competitor's relative strengths and weaknesses
    
"""

# Import libraries

import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

#Load data

df = pd.read_csv('D:/Datasets/Powerlifting/CleanedData.csv')

# Input data

UserSex = 'M'
UserBodyweight = int(74)
UserSquat = 200
UserBench = 107.5
UserDeadlift = 212.5

MaleWeightClasses = [20,53, 59, 66, 74, 83, 93, 105, 120, 
                     math.ceil(df.loc[df['Sex'] == 'M', ['BodyweightKg']].max())]
FemaleWeightClasses = [20, 43, 47, 52, 57, 63, 72, 84, 
                       math.ceil(df.loc[df['Sex'] == 'F', ['BodyweightKg']].max())]

WCDict = {'M' : MaleWeightClasses, 'F' : FemaleWeightClasses}

# Basic calculations

UserWeightClass = pd.cut([UserBodyweight], bins = WCDict[UserSex], labels = WCDict[UserSex][1:])[0]
UserTotal = UserSquat + UserBench + UserDeadlift

# Dictionary creation

UserDict = {
    'Sex' : UserSex,
    'Bodyweight' : UserBodyweight,
    'Squat': UserSquat,
    'Bench' : UserBench,
    'Deadlift' : UserDeadlift,
    'Total' : UserTotal,
    'WeightClass' : UserWeightClass
    }

# Filter matches

Matches = df[(df['Sex'] == UserSex) & (df['WeightClassKg'] == UserWeightClass)]

ComparisonDf = pd.DataFrame(columns = ['Lift', 'Percentile', 'Difference'])
Lifts = ['Squat', 'Bench', 'Deadlift', 'Total']
DataFrameDict = {'Squat' : 'Best3SquatKg',
                 'Bench' : 'Best3BenchKg',
                 'Deadlift' : 'Best3DeadliftKg',
                 'Total' : 'TotalKg'}

for l in Lifts:
    
    x = int(UserDict[l])    
    
    Dif = x / Matches[DataFrameDict[l]].mean() - 1
    
    NumLower = Matches[Matches[DataFrameDict[l]] < x].Name.count()
    Per = NumLower / len(Matches)
        
    ComparisonDf = ComparisonDf.append(
        {
            'Lift': l, 
            'Percentile' : Per, 
            'Difference' : Dif
            }, ignore_index = True)
    
    DistPlot = sns.distplot(Matches[DataFrameDict[l]])
    vals = DistPlot.get_yticks()
    DistPlot.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
    DistPlot.axvline(x = x, color = 'red')
    plt.text(0.05, 0.85, 'Percentile : \n{:.0f}'.format(Per * 100), transform = DistPlot.transAxes)
    plt.xlabel('{} (kg)'.format(l))
    plt.ylabel('Frequency')
    plt.title('Plot showing your {} relative to other lifters in your class'.format(l))
    plt.savefig('docs/assets/{}Dist.png'.format(l))
    plt.show()
    
# Plot relative strengths

LiftPlot = sns.barplot(x = 'Lift', y = 'Difference', data = ComparisonDf)
vals = LiftPlot.get_yticks()
LiftPlot.set_yticklabels(['{:,.0%}'.format(x) for x in vals])
plt.title('Relative Strengths of your lifts')
plt.savefig('docs/assets/LiftPlot.png')
plt.show()