# 1. Define the function before calling it
def calculate_total_cost(price, quantity):
    tot_co = price * quantity
    return tot_co

# 2. Call the function and print the result
app_price = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${app_price}")