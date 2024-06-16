class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        total = 0
        total += int(input("how many dollars?: ")) * 1.0
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
                print("Sorry, that's not enough money. Money refunded.")
                return False
