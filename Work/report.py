# report.py
#
# Exercise 2.4

import sys
import csv

def read_portfolio(filename):
    '''Reads file and creates tuple records for each holding in the portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

portfolio = read_portfolio('./Work/Data/'+filename)
print(portfolio)

total = 0.0
for name, shares, price in portfolio:
    total += shares*price

print(f'Total = {total}')