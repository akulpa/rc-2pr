import time
from modules.functions import getMenu, login, checkStock, checkCart, checkOut, buyItems, updateCart, myInfo, logout,clearScreen,companyName,loading

# Main functions handles the introduction & main menu
def main(current_user):
    if not current_user:
        return      
    print(f"\nWelcome back, {current_user}\n")
    time.sleep(3)
    clearScreen()
    while True:
        user_choice = getMenu()
        if user_choice == 1:
            checkStock()
        elif user_choice == 2:
            buyItems()
        elif user_choice == 3:
            checkCart()
        elif user_choice == 4:
            updateCart()
        elif user_choice == 5:
            checkOut()
        elif user_choice == 6:
            myInfo(current_user)
        elif user_choice == 7:
            logout(current_user)

# --------------Main routine--------------------    
if __name__ == "__main__":
    # Get the name first, then pass it into main
    while True:
        user_name = login()
        if user_name:
            main(user_name)