from display import display_menu
from user_input import getIntRange
from input_requests import add_product_input, category_input_processing
from update_product_data import add_product_into_category
class menu():


    def menu_main(self):
        
        
        choice = 0; #Basically when it is exiting 
        while choice != 6 :
            
            display_menu().main_menu()

            choice = getIntRange("Select Choice (1-5): ", 1, 6)

            if choice == 1: 
                name, category, color, quantity, price = add_product_input()

                add_product_into_category(name, category_input_processing(category), color, quantity, price)
            
            # elif choice == 2:
                
            elif choice == 4:
                display_menu().display_product_listing("Products")
            



            
            

      
            

            




            
            
    
    

