from decimal import Decimal

# X Currency Setup
totalSupply = Decimal('210000000.000000000') # 210M
totalDevFund = Decimal('2100000.000000000') # 1% of 210M is 2.1M

# Data from June 5th Snapshot
print()
print("=== NANO SNAPSHOT 5th of June DATA")
totalAccounts = 95178
print('total_users (who had betwen 6 and 3000 XNO):',str(totalAccounts))
totalWithoutFund = Decimal('18608618.963808177')
print('total_nano:',str(totalWithoutFund))

# Increasing Snapshot Funds by factor ?
totalInitialDistribution = totalSupply - totalDevFund

factor = totalInitialDistribution / totalWithoutFund

print()
print("=== COMPUTATIONS")
print('factor:',factor)
print('exact factor used (to not exceed supply):',round(factor,6))
# exact = 11.17224230365207735011868624
# using 11.172242 and rest to dev fund, since already owe X to a few devs

# using new total without fund is 207899994.349453805
newTotal = Decimal('207899994.349453805')
exactDevFund = totalSupply - newTotal
print()
print("=== X STARTING POINT")
print("total_user:", str(newTotal))
print("dev:", str(exactDevFund))
print("double check (total user + dev):", newTotal+exactDevFund)
print()
