vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print ("Updated Vegetable Inventory: ", vegetables)
if vegetables == "carrots":
    print ("Carrot are already in the list.")
elif vegetables == "cucumbers":
    print ("Cucumbers are already in the list.")