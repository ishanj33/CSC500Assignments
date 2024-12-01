class itemToPurchase:
    def __init__(self):
        self.itemName: str = "none"
        self.itemPrice: float = 0
        self.itemQuantity: int = 0
        self.itemDescription: str = "none"

    def print_item_cost(self):
        item_name = self.itemName
        item_price = self.itemPrice
        item_quantity = self.itemQuantity
        print(item_name, item_quantity, "@", "$", item_price, "=", "$", round(item_price*item_quantity, 2))

class ShoppingCart():
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2020"
        self.cart_items: list[itemToPurchase] = []

    def add_item(self, item: itemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        seen = False
        for item in self.cart_items:
            if item_name == item.itemName:
                self.cart_items.remove(item)
                seen = True
                print("Removed item from cart")
                break
        if seen == False:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name):
        seen = False
        for cart_item in self.cart_items:
            if cart_item.itemName == item_name:
                new_quantity = int(input("Please enter new quantity: "))
                cart_item.itemQuantity = new_quantity
                seen = True
                break
        if seen == False:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.itemQuantity
        return num_items
    
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += (item.itemPrice * item.itemQuantity)
        return total_cost
    
    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
            return
        print(self.customer_name, "-", self.current_date)
        print("Number of Items: ", len(self.cart_items))
        total_cost = 0
        for item in self.cart_items:
            print(item.itemName, item.itemQuantity, "@", "$", item.itemPrice, "=", "$", item.itemPrice * item.itemQuantity)
            total_cost += item.itemPrice * item.itemQuantity
        print("Total: $", total_cost)

    def print_descriptions(self):
        print(self.customer_name, "-", self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.itemName, ":", item.itemDescription)





def populateItem(item: itemToPurchase):
    item.itemName = str(input("Enter item name: "))
    item.itemPrice = float(input("Enter item price: "))
    item.itemQuantity = int(input("Enter item quantity: "))
    item.itemDescription = str(input("Enter item description: "))

def print_menu(cart: ShoppingCart):
    print("MENU")
    options_arr = ["a", "r", "c", "i", "o", "q"]
    input_char = input("Please enter a menu option: ")
    while input_char not in options_arr:
        input_char = input("Please enter a valid menu option: ")
    while input_char != "q":
        if input_char == "a":
            print("Add Item to Cart")
            added_item = itemToPurchase()
            added_item.itemName = str(input("Please enter name of item to add: "))
            added_item.itemDescription = str(input("Please enter description of item to add: "))
            added_item.itemPrice = float(input("Please enter price of item to add: "))
            added_item.itemQuantity = int(input("Please enter quanitity of item to add: "))
            cart.add_item(added_item)
            print("Added Item: ", added_item.itemName)
        if input_char == "r":
            print("Remove Item to Cart")
            name = str(input("Please enter name of item to remove: "))
            cart.remove_item(name)
        if input_char == "c":
            print("Modify Item Quantity")
            name_of_item = str(input("Please enter name of item to modify: "))
            cart.modify_item(name_of_item)
            print("Modified Item Quantity: ", name_of_item)
        if input_char == "i":
            cart.print_descriptions()
        if input_char == "o":
            cart.print_total()
        input_char = input("Please enter a menu option: ")
        while input_char not in options_arr:
            input_char = input("Please enter a valid menu option: ")
    return
    
def outputShoppingCart(cart: ShoppingCart):
    print("OUTPUT SHOPPING CART")
    cart.print_total()

def outputDescriptions(cart: ShoppingCart):
    print("OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_descriptions()


def main():
    cart = ShoppingCart()
    cart.customer_name = str(input("Please enter customer name: "))
    cart.current_date = str(input("Please enter today's date: "))
    print("Customer name: ", cart.customer_name)
    print("Today's Date: ", cart.current_date)
    print_menu(cart)
    print("Number of Items in Cart: ", cart.get_num_items_in_cart())
    print("Total Cost of Cart:", cart.get_cost_of_cart())
    outputDescriptions(cart)
    outputShoppingCart(cart)


if __name__== "__main__":
    main()
