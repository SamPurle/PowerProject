"""

Weight Class predictor:
    
    Use the OpenPowerlifting dataset to predict competitors' weight classes based on their performance
    
"""

# Import libraries

import time
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st = time.time()

# Load data

df = pd.read_csv('RawData.csv')

xFeatures = ['Sex', 'Event', 'Equipment', 'Age', 'AgeClass',
       'BirthYearClass', 'BodyweightKg', 'WeightClassKg', 'Best3SquatKg', 'Best3BenchKg',
       'Best3DeadliftKg', 'TotalKg', 'Place', 'Dots', 'Wilks', 'Glossbrenner',
       'Goodlift', 'ParentFederation']

x = df[xFeatures]
x = x[x['ParentFederation'] == 'IPF'].drop(columns = 'ParentFederation')
x = x[x['Event'] == 'SBD'].drop(columns = 'Event')
x = x[x['Equipment'] == 'Raw'].drop(columns = 'Equipment')

print('The completion time waasa {} seconds'.format(time.time() - st))
print('\007')