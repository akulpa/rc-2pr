from data.admin import member_list
#from data.inventory import cinema_stock, menu
from utils.options import options_list

def login():
    while True:
        name = input("Name: ").title()
        if name in member_list:
            return name
        else:
            print("Admin not found.")
   
def getMenu():
    user_choice = 0
    while True:
        try:
            for index, value in enumerate(options_list, start=1):
                print(f"{index} :  {value}")
            user_choice = int(input("Select an option (1-7): "))
            if 1 <= user_choice <=7:        
                return user_choice            
            else:              
                print("\nPlease select 1 - 7\n")    
        except ValueError:
            print("Invalid. Please select 1-7")