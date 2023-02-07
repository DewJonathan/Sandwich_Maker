class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        # """Returns the total calculated from coins inserted.
        #    Hint: include input() function here, e.g. input("how many quarters?: ")"""
        ###
        total_large_dollars = int(input("How many large dollars?:"))
        total_half_dollars = int(input("How many half dollars?:"))
        total_quarters = int(input("How many quarters?:"))
        total_nickels = int(input("How many nickels?:"))

        customer_total = total_large_dollars * 1 + total_half_dollars * \
            0.5 + total_quarters * 0.25 + total_nickels * 0.05
        print("-------------------------------")
        print(f"Your total:$ {customer_total}")
        return customer_total

    def transaction_result(self, coins, cost):
        # """Return True when the payment is accepted, or False if money is insufficient.
        #    Hint: use the output of process_coins() function for cost input"""
        change = coins - cost
        print(f"Here is ${change} in change")
        if change < 0:
            return False
        else:
            return True
