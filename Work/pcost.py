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
    total_cost = 0
    with open(p + filename, newline='') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost from date file:', cost)
