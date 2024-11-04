class itemToPurchase:
    def __init__(self):
        self.itemName: str = "none"
        self.itemPrice: float = 0
        self.itemQuantity: int = 0

    def print_item_cost(self):
        item_name = self.itemName
        item_price = self.itemPrice
        item_quantity = self.itemQuantity
        print(item_name, item_quantity, "@", "$", item_price, "=", "$", round(item_price*item_quantity, 2))

def populateItem(item: itemToPurchase):
    item.itemName = str(input("Enter item name: "))
    item.itemPrice = float(input("Enter item price: "))
    item.itemQuantity = int(input("Enter item quantity: "))
    

def main():
    item1 = itemToPurchase()
    item2 = itemToPurchase()
    populateItem(item1)
    populateItem(item2)
    item1.print_item_cost()
    item2.print_item_cost()
    total_price = (item1.itemPrice * item1.itemQuantity) + (item2.itemPrice * item2.itemQuantity)
    print("Total Cost: $", total_price)

if __name__== "__main__":
    main()
