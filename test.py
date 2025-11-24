price1 = int(input("enter price of item 1 :"))
price2 = int(input("enter price of item 2 :"))
price3 = int(input("enter price of item 3 :"))
budget = int(input("enter your budget :"))
total_cost = price1 + price2 + price3
difference = budget - total_cost
if(budget >= total_cost):
    print("you have enough money")
    print("the remaining money = ", difference)
else:
    print("The budget has been exceeded")
    print("you need",abs(difference),"pounds")