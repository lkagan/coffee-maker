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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def prompt():
    item = input("What would you like? (espresso/latte/cappuccino): ")
    options = list(MENU.keys()) + ['off', 'report']

    if item not in options:
        print("Sorry, invalid input.")
        return prompt()

    return item


def shutdown():
    print("Shutting down.")
    exit()


def report(resources, money):
    print("The coffee machine has:")
    for key in resources:
        print(f"{key}: {resources[key]}")

    print(f"money: ${money}")



def process_input(input):
    match input:
        case 'off':
            shutdown()
        case 'report':
            report(resources, money)
            process_input(prompt())


process_input(prompt())