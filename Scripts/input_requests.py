from user_input import getString, getIntRange, get_non_negative_Int, get_non_negative_float
from display import display_menu

def add_product_input():
# name, category, quantity, price
    name = getString("Input Name of Product: ")
    display_menu().category_menu()
    category = getIntRange("Choose Category 1-4: ",1,5)
    color = getString("Input Name of Color: ")
    quantity = get_non_negative_Int("Please enter the Quantity: ")
    price =  get_non_negative_float("Please Enter the Price of the Item: ")
    
    return name, category, color, quantity, price

def category_input_processing(option):
    Category = ["Electronics","Accessories","Mechanical Parts","Software"]
    option -=1
    return Category[option]