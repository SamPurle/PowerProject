from os import system
import time

t1 = time.time()

"""

Powerlifting - Data Cleaning:
    
    A script to output the raw .csv file into a usable format
    
"""

system('python Cleaning.py')

#Calculate runtime

t2 = time.time()
print('The runtime for Data Preparation was {:.1f} seconds'.format(t2 - t1))  

""" 

2. Powerlifting - Plotting:
    
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

df['ElapsedTime'] = pd.to_datetime(df['ElapsedTime'])
df['Years'] = df['ElapsedTime'].dt.days / 365
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



# Calculate runtime

t3 = time.time()
print('The runtime for Plotting was {:.1f} seconds'.format(t3 - t2))

"""

3. Powerlifting - Lift Analyis:
    
    Allow the user to input their bodyweight, lifts and sex.
    Return percentiles and representations of where their individual lifts rank
    relative to other competitors in their weight class.

"""

# Input data

UserSex = 'M'
UserBodyweight = int(74)
UserSquat = 200
UserBench = 107.5
UserDeadlift = 212.5

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

# Calculate runtime

t4 = time.time()
print('The runtime for Lift Analysis was {:.1f} seconds'.format(t4 - t3))

"""

4. Powerlifting - Competition Classifier:
    
    A machine learning model to cluster meet data into regional, national and 
    international meets to improve predictions of competitive performance.
    
"""

# Import libraries

from sklearn.cluster import KMeans

# Load data

dfMeet = pd.DataFrame({'MeetName' : df['MeetName'].unique()})
dfMeet['MedianWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.median().values)
dfMeet['MeanWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.mean().values)
dfMeet['CompetitorCount'] = pd.DataFrame(df.groupby(['MeetName']).Name.count().values)
dfMeet['MaxWilks'] = pd.DataFrame(df.groupby(['MeetName']).Wilks.max().values)

x1 = dfMeet['MedianWilks'].values
x2 = dfMeet['MeanWilks'].values


x = dfMeet[['MedianWilks','MaxWilks']]

k_means = KMeans(n_clusters = 3, random_state = 42)
y = k_means.fit_predict(x)

dfMeet['Meet Level'] = pd.DataFrame(y)
dfMeet['Meet Level'].replace(to_replace = [0, 1, 2], value = ['National', 'Regional', 'International'],
                                                              inplace = True)

distortions = []
for i in range(1, 11):
    km = KMeans(
        n_clusters=i, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=42
    )
    km.fit(x)
    distortions.append(km.inertia_)
    
# Plot clusters

sns.relplot(x = 'MaxWilks', y = 'MedianWilks', hue = 'Meet Level', data = dfMeet)
plt.title('Clustering of Competitions')
plt.xlabel('Maximum Wilks score')
plt.ylabel('Median Wilks score')
plt.savefig('docs/assets/ClusterPlot.png', bbox_inches = 'tight')
plt.show()

# Join to existing data

dfMeet = dfMeet.set_index(dfMeet['MeetName'])
df = df.join(dfMeet['Meet Level'], on = (df['MeetName']), how = 'left')

# Calculate runtime

t5 = time.time()
print('The runtime for Meet Classification was {:.1f} seconds'.format(t5 - t4))

"""

5. Powerlifting - Performance Predictor:
    
    A tool to predict a user's placing at an upcoming competition, or retroactively 
    asses the standard of competition and a previous meet.


"""

#Import libraries

import numpy as np

# Input parameters

MeetLevel = 'Regional'
Competitors = 12

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

t6 = time.time()
print('The runtime for Performance Prediction was {:.1f} seconds'.format(t6 - t5))

    

    

    
    
                                       