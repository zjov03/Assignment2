import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
machine = SandwichMaker(resources)
cashier = Cashier()




def main():
    while True:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            print("Turning off machine")
            break
        elif choice == "report":
            machine.resource_report()
        elif choice in recipes:
            sandwich = recipes[choice]
            if machine.check_resources(sandwich["ingredients"]):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, sandwich["cost"]):
                    machine.make_sandwich(choice, sandwich["ingredients"])
        else:
            print("invalid selection. choose again please.")

if __name__=="__main__":
    main()
