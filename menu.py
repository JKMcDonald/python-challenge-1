def print_receipt(order_list):
    # Print header
    print(f"{'Item name':<25} | {'Price':<6} | {'Quantity':<8}")
    print('-' * 40)
    
    total_price = 0
    
    for order in order_list:
        item_name = order['Item name']
        price = order['Price']
        quantity = order['Quantity']
        
        # Print each item in receipt format
        print(f"{item_name:<25} | ${price:>5.2f}  | {quantity:>8}")
        
        # Calculate total price
        total_price += price * quantity
    
    print('-' * 40)
    print(f"Total: ${total_price:.2f}")

def main():
    # Initialize an empty list to store orders
    order_list = []
    
    # Menu items dictionary (sample data)
    menu_items = {
        1: {"Item name": "Apple", "Price": 0.49},
        2: {"Item name": "Tea - Thai iced", "Price": 3.99},
        3: {"Item name": "Fried banana", "Price": 4.49}
    }
    
    # order loop
    while True:
        print("\nMenu:")
        for key, value in menu_items.items():
            print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")
        
        # Prompt for menu selection
        menu_selection = input("Enter your selection from the menu (1, 2, 3): ")
        
        # Validate if input is a digit
        if not menu_selection.isdigit():
            print("Error: Invalid input. Please enter a number.")
            continue
        
        menu_selection = int(menu_selection)
        
        # Check if the selection is valid
        if menu_selection not in menu_items:
            print("Error: Invalid menu selection.")
            continue
        
        # Get item details
        item_details = menu_items[menu_selection]
        item_name = item_details['Item name']
        item_price = item_details['Price']
        
        # Ask for quantity
        quantity_input = input(f"Enter quantity for {item_name} (default is 1): ")
        
        # Validate quantity input
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
        
        # Prompt if the customer wants to keep ordering
        while True:
            decision = input("Would you like to order something else? (y/n): ").lower()
            
            if decision == 'y':
                break
            elif decision == 'n':
                print("Thank you for your order!")
                print_receipt(order_list)
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

main()
    