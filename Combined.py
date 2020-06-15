"""

POWERLIFTING - MAIN SCRIPT:
    
    THIS SCRIPT CAN BE RUN TO RUN ALL OTHERS. THIS WILL PROCESS THE DATA AND 
    UPDATE ALL PLOTS
    
"""

# Import libraries

from os import system
import time

# Input parameters

global UserSex
UserSex = 'M'

global UserBodyweight
UserBodyweight = int(74)

global UserSquat
UserSquat = 200

global UserBench
UserBench = 107.5

global  UserDeadlift
UserDeadlift = 212.5

global MeetLevel
MeetLevel = 'Regional'

global Competitors
Competitors = 12

"""

Powerlifting - Data Cleaning:
    
    A script to output the raw .csv file into a usable format
    
"""

st = time.time()
FILENAME = 'Cleaning'
system('python {}.py'.format(FILENAME))
print('{} complete. The completion time was {:.1f} seconds'.format(
    FILENAME, time.time() - st))

"""

Powerlifting - Growth:
    
    How has the sport grown as a whole in past years?
    
"""

st = time.time()
FILENAME = 'GrowthModelling'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))

""" 

Powerlifting - Plotting:
    
    A script to plot trajectories of competitors throughout their lifting careers
    
"""

st = time.time()
FILENAME = 'Plotting'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))

"""

Powerlifting - Lift Analysis:
    
    A script to show a competitor's relative strengths and weaknesses

"""

st = time.time()
FILENAME = 'LiftAnalysis'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))

"""

Powerlifting - Clustering Model:
    
    A Machine Learning Clustering model to classify competitions into different tiers of difficulty,
    with a view to providing better performance predictions. 
    
"""

st = time.time()
FILENAME = 'ClusteringModel'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))

"""

Powerlifting - Performance Predictor:
    
    A tool to estimate a competitor's ranking within a competition based on their weight, total, and comppetition
    
"""

st = time.time()
FILENAME = 'PerformancePredictor'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))
    

"""

Powerlifting - Lift Dependency:
    
    How does the dependence on each lift vary throughout weight classes
    
"""

st = time.time()
FILENAME = 'LiftDependency'
system('python {}.py'.format(FILENAME))
print('{} complete. Completion time was {:.1f} seconds.'.format(
    FILENAME, time.time() - st))
    
    
                                       