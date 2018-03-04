ATM_code = 1187
money = 0
while True:
    answer1 = int(input("Enter your ATM code:"))

    if answer1 == ATM_code:

        answer2 = str(input("Would you like make diposit?:"))
        if answer2 == 'yes':
            deposit = int(input("How much?:"))

            if deposit >= money:
                money += deposit
                print("Here is your balance:{}". format(money))
                withdraw = str(input("Would like withdraw?:"))
                if withdraw == 'yes':
                    deposit2 = int(input("How much?:"))
                    if deposit2 <= money:
                        money -= deposit2
                    print("Here is your new balance: {}". format(money))
            if answer2 == 'no':
                        print ("Good bye")
            elif withdraw == 'no':
                        print ("See you next time")
            break




