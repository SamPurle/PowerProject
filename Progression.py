"""

Powerlifting Progression:
    
    Determine how athletes' lifts, bodyweight and Wilks vary with time competing
    
"""

# Import libraries

import pandas as pd
import time
st = time.time()

# Load data

print('Loading data...')

df = pd.read_csv('RawData.csv')

# Filter IPF, SBD, Raw

df = df[df['ParentFederation'] == 'IPF']
df = df.drop(columns = 'ParentFederation')

df = df[df['Event'] == 'SBD']
df = df.drop(columns = 'Event')

df = df[df['Equipment'] == 'Raw']
df = df.drop(columns = 'Equipment')

# Determine First Meet Date

print('Sorting by date...')
df = df.sort_values(by = ['Date'])

Dates = df['Date'].unique()
lNames = len(df['Name'])
df['FirstMeetDate'] = 0
df['UUID'] = 0
dfSearched = pd.DataFrame(columns = ['Name','FMD', 'UUID'])
i = 0

print('Iterating through names...')

for d in Dates:   
   
    dfDate = df[df['Date'] == d]
    
    for Name in dfDate['Name']:
        
        n = dfDate[dfDate['Name'] == Name].index.values[0]
        
        if Name not in dfSearched['Name']: 
            
            i += 1
            dfA = pd.DataFrame({
                'Name': [Name],
                'FMD' : [d],
                'UUID' : [i]})
            dfSearched = dfSearched.append(dfA)
            df.loc[n, 'FirstMeetDate'] = d
            df.loc[n, 'UUID'] = i
            l = len(dfSearched)
            
            if l % 1000 == 0:
                
                print((l / lNames) * 100, '%')                
                print('The elapsed time is {} minutes'.format((time.time() - st) / 60))
                
        if Name in dfSearched['Name']:
            
            f = dfSearched[dfSearched['Name'] == n]['FMD']
            id = dfSearched[dfSearched['Name' == n]]['UUID']
            df.loc[n, 'FirstMeetDate'] = f
            df.loc[n, 'UUID'] = id
            
df.to_csv('FirstMeetData.csv')

print('The completion time was {} seconds'.format(time.time() - st))