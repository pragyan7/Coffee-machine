from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 3.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
profit = 0
# Check the resources
def check_resources(order_ingredients):
    '''Checks the resources available to make the drink order.'''
    # If no, inform that there ain't enough resources to make the coffee order
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"\nSorry, there is not enough {item} to make your order 😥")
            return False
    return True

# Ask for the money
# Process the coins by asking all four types of coin questions
def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print("\nPlease insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
    
# Check money received
def is_enough_money(money_received, drink_cost):
    '''Return True if the payment is sufficient, and False if not.'''
    # If the money is not enough, inform that the money is not enough. Then, refund the money
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is 💲{change} in change!")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded 💰")
        return False
        
# Ask for the type of coffee
def coffee_machine(coffee, order_ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee.title()} ☕. Enjoy!")

is_on = True
while is_on:
    print(logo)
    choice = (input("What would you like? (Espresso/Latte/Cappuccino): ")).lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("---------------")
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"\nMoney: 💲{profit}")
        print("---------------")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_enough_money(payment, drink["cost"]):
                coffee_machine(choice, drink["ingredients"])
