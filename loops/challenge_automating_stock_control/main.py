# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
for item in inventory:
    current_stock, minimum_stock, re_quant, on_sale = inventory[item]
    while current_stock < minimum_stock:
        current_stock += re_quant
    print("this",item, "is below the minimum stock")
    print("item name :", item, "has been added with total ", current_stock)
    inventory[item][0] = current_stock
    if inventory[item][0] > discount_threshold:
            inventory[item][3] = True
            print("THIS ITEM NAME CALLED ",item ,"IS FOR SALE")