import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():

    print("What would you like to do?")
    print("---------------------------")
    print("[0] : off")
    print("[1] : order")
    print("[2] : report")

    choice = int(input("Enter Number:"))
    

    if choice == 1:
        # if option 1 take another input of sandwhich_size
        # get order_ingredients from dict with key = sandwhich_size
        sandwhich_size = input("What would you like? (small/ medium/ large):")
        order_ingredients = recipes[sandwhich_size]["ingredients"]
        # if resources had order_ing
        # get cost with key and value
        if sandwich_maker_instance.check_resources(order_ingredients):
            cost = recipes[sandwhich_size]["cost"]
            print(f"Your sandwich costs:${cost}")
            coins = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins, cost):
                sandwich_maker_instance.make_sandwich(
                    sandwhich_size, order_ingredients)
            print(f"Your {sandwhich_size} is ready.Bon appetit!")
            main()

        else:
            print("Sorry that's not enough money. Money refunded.")
            main()

    elif choice == 2:
        print("Here is a report of the current Respources")
        print("-----------------------------------------")
        for ingredient, quantity in resources.items():
            print(f"{ingredient}:{quantity}")
        main()

    elif choice == 3:
        exit()
    else:
        print(ValueError)

        main()


if __name__ == "__main__":
    main()
