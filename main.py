from texttable import Texttable
import sys
import os
import time


def calculate(capital):
    if capital <=1000:
        EQUITY = capital * 0.5 #...50%
        ETF = capital * 0.5 #...50%
        BONDS = 0
    else:
        EQUITY = capital * 0.4 #...40%
        ETF = capital * 0.3 #...30%
        BONDS = capital * 0.3 #...30%

    return EQUITY, ETF, BONDS

if __name__ == '__main__':
    capital = sys.argv[1]
    eq, etf, bonds = calculate(int(capital))
    eq = round(eq, 2)
    etf = round(etf, 2)
    bonds = round(bonds, 2)
    table = Texttable()
    table.add_rows([['Equity', 'ETF', 'Securities & Bonds'], ['₹ ' + str(eq), '₹ ' + str(etf), '₹ ' + str(bonds)]])
    os.system("clear")
    print(table.draw())

    start = time.time()
    timeout = 5

    while True:
        current = time.time()
        if input("\n*** Hit enter for the prompt ***\n") == '':
            break
        