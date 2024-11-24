from display import display_menu
from user_input import getIntRange
from input_requests import add_product_input, category_input_processing, remove_product_input, update_product_quantity_input
from update_product_data import add_product_into_category, remove_product_by_id, update_quantity
class menu():


    def menu_main(self,conn):
        
        
        choice = 0; #Basically when it is exiting 
        while choice != 6 :
            
            display_menu().main_menu()

            choice = getIntRange("Select Choice (1-5): ", 1, 6)
          
            if choice == 1: 
                name, category, color, quantity, price = add_product_input()
                
                
                add_product_into_category(conn,  name, category_input_processing(category), color, quantity, price)
            
            elif choice == 2:
                 display_menu().display_product_listing(conn, "Products")
                 print("---Choose the ProductID of the item you wish to remove---")
                 prod_id = remove_product_input()
                 remove_product_by_id(conn, prod_id)

            elif choice == 3:
                display_menu().display_product_listing(conn, "Products")
                prod_id, quantity = update_product_quantity_input()
                update_quantity(conn, prod_id, quantity )
                

            elif choice == 4:
                display_menu().display_product_listing(conn, "Products")
              

            elif choice == 5:
                break;
            



            
            

      
            

            




            
            
    
    

