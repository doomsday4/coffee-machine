MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 200,
}

def check_resources(c):
    if MENU[c]['ingredients']['water'] > resources['water']:
        return "milk"
    if MENU[c]['ingredients']['coffee'] > resources['coffee']:
        return "coffee"
    if c != "espresso":
        if MENU[c]['ingredients']['milk'] > resources['milk']:
            return "water"

    return True

money = 0
choice = input("What would you like? (espresso/latte/cappuccino): ")

while choice != "off" :
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    else:
        possible = check_resources(choice)
        if  possible!= True:
            print(f"Sorry there is not enough {possible}.")
        else:
            print("Please insert the coins.")
            q = int(input("Quarters? "))
            d = int(input("Dimes? "))
            n = int(input("Nickels? "))
            p = int(input("Pennies? "))

            total_money = q*0.25 + d*0.10 + n*0.05 + p*0.01
            if total_money < MENU[choice]['cost'] :
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += round(total_money, 2)
                resources["water"] -= MENU[choice]['ingredients']['water']
                resources["coffee"] -= MENU[choice]['ingredients']['coffee']
                if choice != "espresso":
                    resources["milk"] -= MENU[choice]['ingredients']['milk']
                print(f"Here is your {choice}. Enjoy!")
                change = round(total_money - MENU[choice]['cost'], 2)
                if change>0:
                    print(f"And here's your change- ${change}. Thank You.")

    choice = input("What would you like? (espresso/latte/cappuccino): ")
