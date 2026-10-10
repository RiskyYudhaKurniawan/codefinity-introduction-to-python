prices = [29.99, 45.50, 12.75, 38.20]
discount = [0.10, 0.20, 0.15, 0.05]
for cost in range(len(prices)):
    discount_rate = discount[cost]
    prices[cost] -= prices[cost] * discount_rate
    print(f"Updated price for item {cost + 1}: ${prices[cost]:.2f}")
    