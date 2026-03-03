# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

 #building revenue list and assigning values. Creates list called revenue and for each product in 
revenue = []
for product in range(len(products)): #uses range(len(list)) because products is STR and needs int
    new_price = prices[product] * quantities_sold[product] #creates new price by multiplying price and quantity of each item
    revenue.append(new_price) #add that price to new revenue list
#print(revenue) to see original values

# Combine the product names list with created revenue list
revenue_per_product = list(zip(products, revenue))
#print(revenue_per_product) to see revenue of each item
revenue_per_product = sorted(revenue_per_product) # Sorts List Alphabetically, Uses sorted() bcuz its a tuple
print(revenue_per_product)

for name , rev in revenue_per_product: #For each item in revenue_per_product prints product has total revenue of rev
# Example of expected output line (do not remove):
    print(f"{name} has total revenue of ${rev}")