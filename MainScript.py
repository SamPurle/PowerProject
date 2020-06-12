""" 

Powerlifting - Main Script:
    
    This script can be run to call all others, which in turn will update all 
    plot files publisheed on the dependent webpage
    
"""

from subprocess import call
from Cleaning import df


print(df['Name'])
