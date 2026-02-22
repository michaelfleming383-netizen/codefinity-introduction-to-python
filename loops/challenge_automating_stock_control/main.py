# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100


print("Processing started")
#print("------------------")



for item in inventory:
    cu_stock = inventory[item][0]
    print(f"{item} {cu_stock} Current Stock")
    min_stock = inventory[item][1]
    print(f"{item} {min_stock} Current Min Stock")
    re_stock = inventory[item][2]
    print(f"{item} {re_stock} Current Restock value")
    sale = inventory[item][3]
    print(f"{item} {sale} Current Sale")
    print(f"Processing {item}")
    
    
    
  # print(item_dets)
    while cu_stock < min_stock:
            cu_stock += re_stock
            inventory[item][0] = cu_stock
            if cu_stock > discount_threshold and sale == False:
                
                sale = True
                inventory[item][3] = sale
                #print(sale)
print(inventory)               
print("Processing completed")
