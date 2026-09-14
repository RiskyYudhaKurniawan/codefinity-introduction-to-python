# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
grapes_count = shelf.count("grapes")
orange_count = shelf.count("oranges")
orange_index = shelf.index("oranges")
print("Number of Apples: ", apple_count)

banana_index = shelf.index("bananas") 
print("First Banana Index: ", banana_index)

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    
if grapes_count > 1:
    print ("Grapes are sufficiently stocked.")
else:
    print("Grapes need to be restocked.")

if "oranges" in shelf and orange_index == 1 :
    print ("Oranges are at index: ", orange_index)
else:
    print("Oranges are out of stock.")