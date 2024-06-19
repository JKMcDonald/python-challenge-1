def print_receipt(order_list):
   # print the reciept format
    print(f"{'Item name'} | {'Price'} | {'Quantity'}")
    print('-' * 40)
    
    total_price = 0
    # create order list
    for order in order_list:
        item_name = order['Item name']
        price = order['Price']
        quantity = order['Quantity']
        
       # print list
        print(f"{item_name} | ${price}  | {quantity}")
        
        # Calculate total price
        total_price += price * quantity
    
    print('-' * 40)
    print(f"Total: ${total_price}")

def main():
    
    order_list = []
    
    # Create menu items dictionary
    menu_items = {
        1: {"Item name": "Apple", "Price": 0.49},
        2: {"Item name": "Tea - Thai iced", "Price": 3.99},
        3: {"Item name": "Fried banana", "Price": 4.49}
    }
    
 
    while True:
        print("\nMenu:")
        for key, value in menu_items.items():
            print(f"{key}. {value['Item name']} - ${value['Price']}")
        
         #input selection
        menu_selection = input("Enter your selection from the menu (1, 2, 3): ")
        
        
        if not menu_selection.isdigit():
            print("Error: Invalid input. Please enter a number.")
            continue
        
        menu_selection = int(menu_selection)
        
       
        if menu_selection not in menu_items:
            print("Error: Invalid menu selection.")
            continue
        
        
        item_details = menu_items[menu_selection]
        item_name = item_details['Item name']
        item_price = item_details['Price']
        
       
        quantity_input = input(f"Enter quantity for {item_name} (default is 1): ")
        
    
        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                quantity = 1
        except ValueError:
            quantity = 1
        
        # Add order to order_list
        order_list.append({
            "Item name": item_name,
            "Price": item_price,
            "Quantity": quantity
        })
        
       
        while True:
            decision = input("Would you like to order something else? (y/n): ").lower()
            # conditional for whether order again or not
            if decision == 'y':
                break
            elif decision == 'n':
                print("Thank you for your order!")
                print_receipt(order_list)
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

main()
    
