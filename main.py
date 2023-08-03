from texttable import Texttable


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
    eq, etf, bonds = calculate(2351)
    eq = round(eq, 2)
    etf = round(etf, 2)
    bonds = round(bonds, 2)
    table = Texttable()
    table.add_rows([['Equity', 'ETF', 'Securities & Bonds'], ['₹ ' + str(eq), '₹ ' + str(etf), '₹ ' + str(bonds)]])
    print(table.draw())