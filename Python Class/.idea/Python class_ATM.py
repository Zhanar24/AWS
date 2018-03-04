chase_balance = 1000

while True:
    withdraw = int(input("How much would like withdraw? :"))

    if withdraw <= chase_balance:
            chase_balance -= withdraw
            print("Here is your new balance: {}". format(chase_balance))
    else:
        print("You do not have sufficient funds for this transaction:Please make some diposit")
        break