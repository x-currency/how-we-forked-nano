# how-we-forked-nano
List available at https://x-currency.org/3000.txt

### LY3000: The Initial Coin Distribution of X Currency

Steps to reproduce:
- Download and follow installation instructions at https://github.com/nanocurrency/nanodb-specification/ to query the Nano ledger database.
- Download data.ldb (109GB) (request + donation required)
- Run accounts query with 33M and 44M count (to double check if all the rows are retrieved) and print to create your nanodump.txt file.


#### 1. Calculate Total Balance of Eligeable Nano Addressess (between 6 and 3000 XNO):
```
python3 printnanobalances.py nanodump.txt
```

#### 1.1 Sum all balances (9 decimals):
```
python3 sumly3000.py nanodump.txt
```

#### 2. Configure Multiplier/Dev Fund:
```
vim multiplier.py
python3 multiplier.py
```

#### 3. Calculate New List
```
vim ly3000.py # edit multiplier
python3 ly3000.py nanodump.txt > 3000.txt
```
