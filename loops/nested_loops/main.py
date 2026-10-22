produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]

for section in groceries:
    print("Name of section : ", section)
    for item in section:
        print("Item name : ", item)
    