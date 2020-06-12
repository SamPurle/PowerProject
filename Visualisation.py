"""

Powerlifting: 
    
    Experimenting with data visualisation
    
"""

# Import libraries

import pandas as pd
import numpy as np
import seaborn as sns

# Load data

df = pd.read_csv('RawData.csv')

Features = ['Sex', 'AgeClass', 'Division', 'Event', 'Equipment', 'ParentFederation',
       'BodyweightKg', 'WeightClassKg','Best3SquatKg',
       'Best3BenchKg', 'Best3DeadliftKg', 'TotalKg', 'Place', 'Dots', 'Wilks',
       'Glossbrenner', 'Tested', 'Date']

df = df[Features]

# Filter SBD, Raw, IPF

df = df[df['Event'] == 'SBD']
df = df.drop(columns = 'Event')

df = df[df['Equipment'] == 'Raw']
df = df.drop(columns = 'Equipment')

df = df[df['ParentFederation'] == 'IPF']
df = df.drop(columns = 'ParentFederation')

# Visualise

sns.pairplot(df)
