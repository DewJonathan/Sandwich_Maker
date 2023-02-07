
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        # for key, value in ingredientd()
        # if self[ingredient] < value

        for ingredient, quantity in ingredients.items():
            if self.machine_resources[ingredient] < quantity:
                return False
            else:
                return True

    def make_sandwich(self, sandwich_size, order_ingredients):

        # for each quanitiy or ingredient in order
        # resources[ingredient] -=

        for ingredient, quantity in order_ingredients.items():

            self.machine_resources[ingredient] -= quantity
