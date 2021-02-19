# stock.py

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name   = name
        self.shares = shares
        self.price  = price
    
    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, nshares):
        '''
        Sell a number of shares
        '''
        self.shares -= nshares


def main(args):
    # if len(args) != 3:
    #     raise SystemExit('Usage: %s portfile pricefile' % args[0])
    # portfolio_report(args[1], args[2])
    pass

if __name__ == '__main__':
    import sys
    main(sys.argv)