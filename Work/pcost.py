# pcost.py
#
# Exercise 1.27

import sys
from pathlib import Path
import csv

if Path.cwd().name.endswith('python'):
    p = './Work/Data/'
else:
    p = './Data/'

def portfolio_cost(filename):
    'Returns total cost'
    totalcost = 0
    with open(p + filename, newline='') as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            totalcost += int(row[1]) * float(row[2])
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
