# stock.py

class Stock:

    def __init__(self, name, shares, price):
        # Any value stored on `self` is instance data
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amtsold):
        self.shares -= amtsold


def main(args):
    # if len(args) != 3:
    #     raise SystemExit('Usage: %s portfile pricefile' % args[0])
    # portfolio_report(args[1], args[2])
    pass

if __name__ == '__main__':
    import sys
    main(sys.argv)