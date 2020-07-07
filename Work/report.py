# report.py
#
# Exercise 2.4

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
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

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

def make_report(port, pricedict):
    reportlist = []
    for s in port:
        reportlist.append((s[0], s[1], pricedict.get(s[0]), pricedict.get(s[0])-s[2]))
    return reportlist

filename1 = 'portfolio.csv'
filename2 = 'prices.csv'

portfolio = read_portfolio(p+filename1)
prices = readprices(p+filename2)
report_items = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
dashes = '----------'
print()
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(f'{dashes:>10s} {dashes:>10s} {dashes:>10s} {dashes:>10s}')
for name, shares, price, change in report_items:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

# total = 0.0
# for name, shares, price in portfolio:
#     total += shares*price

# print(f'Total = {total:.2f}')