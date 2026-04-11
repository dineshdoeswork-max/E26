class Item:
    def __init__(self, itemId, title, price, seller):
        self.itemId = itemId
        self.title = title
        self.price = float(price)
        self.seller = seller
        self.isAvailable = True

    def displayDetails(self):
        status = "Available" if self.isAvailable else "Sold"

        print("\n--- Item Details ---")
        print(f"ID: {self.itemId} | Title: {self.title}")
        print(f"Seller: {self.seller} | Price: ₹{self.price:.2f} | Status: {status}")

class UsedItem(Item):
    def __init__(self, itemId, title, originalPrice, seller, condition, years):

        super().__init__(itemId, title, originalPrice, seller)

        if condition == "Like New":
            factor = 0.9
        elif condition == "Good":
            factor = 0.75
        elif condition == "Fair":
            factor = 0.6
        else:
            factor = 0.45

        self.price = float(originalPrice) * factor
        self.condition = condition
        self.years = years

    def displayDetails(self):
        super().displayDetails()
        print(f"Condition: {self.condition} | Age: {self.years} years")

print("Select Item Type: 1 for New, 2 for Used")
choice = input("Choice: ")

id_in = input("Enter ID: ")
title_in = input("Enter Title: ")
price_in = float(input("Enter Price (or Original Price): "))
seller_in = input("Enter Seller Name: ")


if choice == "1":
    product = Item(id_in, title_in, price_in, seller_in)

else:
    cond_in = input("Enter Condition (Like New, Good, Fair, Poor): ")
    years_in = input("Enter Years of Usage: ")

    product = UsedItem(
        id_in,
        title_in,
        price_in,
        seller_in,
        cond_in,
        years_in)
    

product.displayDetails()