from user_input import getString, getIntRange, get_non_negative_Int, get_non_negative_float, getInt, getYesOrNo
from display import display_menu


def add_product_input():
# name, category, quantity, price
    name = getString("Input Name of Product: ")
    display_menu().category_menu()
    category = getIntRange("Choose Category 1-4: ",1,5)
    if category == 3:
        color = getString("Input Name of Color: ")
        quantity = get_non_negative_Int("Please enter the Quantity: ")
    else:
        color = "NULL"
        quantity = "NULL"
    price =  get_non_negative_float("Please Enter the Price of the Item: ")
    
    return name, category, color, quantity, price

def category_input_processing(option):
    Category = ["Electronics","Accessories","Mechanical Parts","Software"]
    option -=1
    return Category[option]

def remove_product_input():
    id = getInt("Choose the Product ID of the item you wish to remove: ")
    return id 

def update_product_quantity_input():
    prod_id = get_non_negative_Int("Select the ProductID of the item quantity you would like to modify: ")
    quantity = get_non_negative_Int("Enter the new quantity: ")

    return prod_id, quantity

    