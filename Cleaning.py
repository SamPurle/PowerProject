"""

Powerlifting - Data Cleaning:
    
    A script to output the raw .csv file into a usable format
    
"""

# Import libraries

import pandas as pd
import math

# Load data

df = pd.read_csv('D:\Datasets\Powerlifting\RawData.csv', low_memory = False)

# Filter for Raw, IPF, SBD

df = df.loc[(df['Equipment'] == 'Raw') & (df['Event'] == 'SBD') & (df['ParentFederation'] == 'IPF')]

# Convert Place to integer

df = df[(df.Place != 'DQ') & (df.Place != 'G') & (df.Place != 'DD') & (df.Place != 'NS')]
df.loc[:,'Place'] = df.Place.astype(int)

# Convert Date to datetime format

df.loc[:,'Date'] = pd.to_datetime(df.Date)

# Convert Weight Class to integer

df = df[df.loc[:,'BodyweightKg'].notnull()]

MaleWeightClasses = [20,53, 59, 66, 74, 83, 93, 105, 120, 
                     math.ceil(df.loc[df['Sex'] == 'M', ['BodyweightKg']].max())]
FemaleWeightClasses = [20, 43, 47, 52, 57, 63, 72, 84, 
                       math.ceil(df.loc[df['Sex'] == 'F', ['BodyweightKg']].max())]

global WCDict
WCDict = {'M' : MaleWeightClasses, 'F' : FemaleWeightClasses}

for s in df.Sex.unique():
    df.loc[df['Sex'] == s, ['WeightClassKg']] = pd.cut(df[df.loc[:,'Sex'] == s]['BodyweightKg'], 
                                    bins = WCDict[s], labels = WCDict[s][1:])

df.loc[:, 'WeightClassKg'] = df.loc[:, 'WeightClassKg'].astype(int)

# Calculate elapsed time since first meet

df = df.join(df.groupby(['Name'])['Date'].min(), how = 'left', on = (df['Name']), rsuffix = 'FirstMeet')
df['ElapsedDays'] = (df['Date'] - df['DateFirstMeet']).dt.days

df.to_csv('D:/Datasets/Powerlifting/CleanedData.csv')