balance = 100000
month = 1
while balance > 0:
    print("Here is your balance: {} at month {}".format(balance, month))
    month += 1
    balance = balance + (balance * 0.01) - 1500
print("It took you ~{} years to pay off the balance ".format(month // 12))

