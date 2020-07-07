# report2.py - Using dict

import sys
import csv
from pathlib import Path

if Path.cwd().name.endswith('python'):
    p = './Work/Data/'
else:
    p = './Data/'

def read_portfolio(filename):
    '''Reads file and creates tuple records for each holding in the portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {headers[0]: row[0], headers[1]:int(row[1]), headers[2]: float(row[2])}
            portfolio.append(holding)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

portfolio = read_portfolio(p+filename)
print(portfolio)

total = 0.0
for s in portfolio:
    total += s['shares'] * s['price']

print(f'Total = {total:.2f}')

# readprices function
def readprices(fn):
    prices = {}
    with open(fn, newline='') as f2:
        rows = csv.reader(f2)
        for row in rows:
            if not row:
                continue
            prices[row[0]] = float(row[1])
    return prices

pricedict = readprices(p+'prices.csv')

print(pricedict)