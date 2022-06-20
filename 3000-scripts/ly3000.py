import sys
if len(sys.argv) != 2:
    print("usage nanodumptoaccounts.py [dump.txt]")
    exit(1)


import lib.conversion
from decimal import Decimal

MULTIPLIER_FROM_SETUP = '11.172242' # see multiplier.py

total = 0
path=sys.argv[1]

prevAccount = '';
with open(path) as f:
    for line in f:
        if "account " in line:  
            nano_address_pieces = line.split(" ")
            nano_address = nano_address_pieces[len(nano_address_pieces)-1].strip()
            prevAccount = nano_address.replace('nano_','X_')
        if "balance " in line:  
            nano_balance_pieces = line.split(" ")
            nano_balance = nano_balance_pieces[len(nano_balance_pieces)-1].strip()
            inNano = conversion.convert((nano_balance), from_unit='raw', to_unit='XRB')
            if Decimal(6) <= inNano and inNano <= Decimal(3000):
                nanoBalanceRoundedInNineDec = round(inNano,9)
                balanceForXWithMultiplier = nanoBalanceRoundedInNineDec * Decimal(MULTIPLIER_FROM_SETUP)
                print(prevAccount + ":" + str(round(balanceForXWithMultiplier,9))) 
            

