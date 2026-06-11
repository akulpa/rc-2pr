import time
from modules.functions import getMenu, login, test_1, test_2, test_3, test_4, test_5, test_6, test_7
# Main functions handles the introduction & main menu
def main(current_user):
    if not current_user:
        return      
    print(f"\nWelcome back, {current_user}\n")
    time.sleep(3)
    while True:
        user_choice = getMenu()
        if user_choice == 1:
            test_1()
        elif user_choice == 2:
            test_2()
        elif user_choice == 3:
            test_3()
        elif user_choice == 4:
            test_4()
        elif user_choice == 5:
            test_5()
        elif user_choice == 6:
            test_6()
        elif user_choice == 7:
            test_7()

# --------------Main routine--------------------    
if __name__ == "__main__":
    # Get the name first, then pass it into main
    while True:
        user_name = login()
        if user_name:
            main(user_name)