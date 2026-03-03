# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenues = []
    for item in range(len(prices)):
        new_price = prices[item] * quantities_sold[item]
        revenues.append(new_price)
    return revenues
    #print("Step One Complete")
    
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = sorted(zip(products, revenues))

def formatted_output(revenue_per_product):
    for prod, rev in revenue_per_product:
        print(f"{prod} has total revenue of ${rev}")
formatted_output(revenue_per_product)

    
# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")