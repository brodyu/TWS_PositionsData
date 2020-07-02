# TWS_PositionsData

This Python script collects user stock data and position data for each account under management for the Interactive Brokers platform. Script outputs a CSV file with all the positions data for easy portfolio management. 

## Instructions

1. You must have IBKR's Trader Workstation open while running the script. 
2. Within Trader Workstation, enable ActiveX and Socket Clients, and make sure you match the correct socket port to the Python code (7496 by default).

Special thanks to the ib_insync team for making a easy to use library to connect to the TWS API. 

