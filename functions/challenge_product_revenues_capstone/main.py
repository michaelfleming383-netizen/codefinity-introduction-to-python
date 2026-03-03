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
# This function should multiply each price by its corresponding quantity sold, 
# store the results in a list, and return this list of revenues.
    
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = sorted(zip(products, revenues)) #pairs each product with associated revenue and sorts alphabetically

def formatted_output(revenue_per_product):
    for prod, rev in revenue_per_product:
        print(f"{prod} has total revenue of ${rev}")
formatted_output(revenue_per_product)
# This function should take a list of `(product_name, revenue)` tuples, 
# sort them alphabetically by product name,
# and print each in the specified format.