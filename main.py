# user difined shopping list organizer
# Ask user to enter items names and prices one by one 

is_running = True
products = {}

while is_running:
    item = input('Enter the item bought or Type("q" to quit): ').lower()
    if item == 'q':
        is_running = False
    else:
        valid_price = True
        if valid_price == True:
            price = input('Enter the price of the item: ')
            if not price.isdigit():
             print('Price should be a digit')

            products[item]= price
            
print(products)


    
    







