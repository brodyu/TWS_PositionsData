from ib_insync import *
import pandas as pd
import time
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)

accounts = ib.managedAccounts()

final_df = pd.DataFrame()

for account in accounts:
    stocks = []
    quantity = []

    positions = ib.positions(account)

    for i in range(len(positions)):
        stocks.append(positions[i].contract.localSymbol)
        quantity.append(positions[i].position)

    df = pd.DataFrame(stocks, columns=[account])
    df['Quantity'] = quantity
    final_df = pd.concat([final_df, df], axis=1)

print(final_df.head())
tm = time.strftime('%d %b %y')
final_df.to_csv('positionsData {}.csv'.format(tm))