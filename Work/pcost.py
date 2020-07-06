# pcost.py
#
# Exercise 1.27
# Used pandas instead of more tradational methods.
# Then read that course wants you to stick to traditional python. Okay.

import sys
import pathlib
import pandas as pd

def portfolio_cost(filename):
    'Returns total cost'
    datapath = pathlib.Path.cwd() / 'Work' / 'Data' / filename
    if datapath.is_file():
        df = pd.read_csv(datapath).assign(cost=lambda x: x['shares'] * x['price'])
        return df.cost.sum()
    else:
        return 'File not found'

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
