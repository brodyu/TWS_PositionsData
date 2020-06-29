from ib_insync import *
import pandas as pd
import time
# util.startLoop()  # uncomment this line when in a notebook

class TWSAPI:

    # Function to pull position data from managed accounts
    def positionsData(self):
        
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

        tm = time.strftime('%d %b %y')
        final_df.to_csv('positionsData {}.csv'.format(tm))

# Main
if __name__ == "__main__":
    # Try to connect to TWS API, throws error if 
    while True:
        try:
            ib = IB()
            ib.connect('127.0.0.1', 7496, clientId=1)
            break
        except ValueError:
            print("Could not connect to TWS: Check if TWS is runnning & correct port gate...")

    print("Connection established...")
    print("Pulling positions data for managed accounts...")
    
    apicall = TWSAPI()
    apicall.positionsData()

