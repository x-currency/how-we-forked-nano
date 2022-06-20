import sys
if len(sys.argv) != 2:
    print("usage sumly3000.py [dump.txt]")
    exit(1)


import lib.conversion
from decimal import Decimal


total = 0
path=sys.argv[1]
with open(path) as f:
    for line in f:
        amount_pieces = line.split(":")
        amount = amount_pieces[len(amount_pieces)-1].strip()
        total += Decimal(amount) # because Python can handle infinitely large int
            
            #print("adding",amount)
print(total)

