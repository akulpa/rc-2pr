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
            
def test_1():
    print("test 1")
    
def test_2():
    print("test 2")
    
def test_3():
    print("test 3")
    
def test_4():
    print("test 4")
    
def test_5():
    print("test 5")
    
def test_6():
    print("test 6")
    
def test_7():
    print("test 7")