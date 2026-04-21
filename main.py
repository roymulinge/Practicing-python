# user difined shopping list organizer
# Ask user to enter items names and prices one by one 

is_running = True
products = {}

while is_running:
    item = input('Enter the item bought: ').lower()
    price = float(input('Enter the price of the item: '))
    products[item] = price
    quit = input('Press "q" to quit').lower()
    if quit == 'q':
        is_running = False
        print(products)



    
    







