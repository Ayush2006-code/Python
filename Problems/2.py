#shopping cart program 
item = input("Enter your item name :")
price = float(input("Enter the price of the item :"))
quantity = int(input("Enter the quantity of the item :"))
total_price = price * quantity  
print(f"The total price of {quantity} {item} is {total_price} Rs.")