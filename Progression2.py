"""

Powerlifting:
    
    Analysis of how competitors' lifts, bodyweight and wilks changee with time competing

"""

# Import libraries

import pandas as pd
import time
st = time.time()

# Load data

print('Loading data...')

df = pd.read_csv('RawData.csv', low_memory = False)

# Filter IPF, SBD, Raw

df = df[df['ParentFederation'] == 'IPF']
df = df.drop(columns = 'ParentFederation')

df = df[df['Event'] == 'SBD']
df = df.drop(columns = 'Event')

df = df[df['Equipment'] == 'Raw']
df = df.drop(columns = 'Equipment')

# Determine First Meet Date

df = df.drop(columns = 'MeetState')
df.drop(columns = 'MeetName')

df.loc[:,'Date'] = pd.to_datetime(df.loc[:,'Date'])

df['FMD'] = 0
df['CompetitorId'] = 0
df['ElapsedTime'] = 0

UniqueNames = df.loc[:,'Name'].unique()

i = 0 

print('Iterating through names...')
for n in UniqueNames:
    i += 1
    dfA = df.loc[df['Name'] == n]
    indices = dfA.index
    FMD = dfA['Date'].min()
        
    for x in indices:
        df.loc[x,'FMD'] = FMD
        df.loc[x,'CompetitorId'] = i
        df.loc[x,'ElapsedTime'] = df.loc[x,'Date'] - FMD
            
    if i % 1000 == 0:
        print('{} entries complete'.format(i))
        print('The elapsed time is {} minutes'.format((time.time() - st) / 60))
    
