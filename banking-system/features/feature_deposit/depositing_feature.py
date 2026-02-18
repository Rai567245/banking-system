from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class DepositingSection:
    def deposit_money (self, account):
        while True:
            print(center_text(banner()))
            print(center_text("|                 Banking System (Depositing Page)                |"))
            print(center_text(banner()))    

            print(left_text(f"Account Balance: {account.balance}", offset=22))
            prompt1 = left_text("Enter the amount to be deposited (or Q to Quit): ", offset=9).rstrip()
            amount_input= input(prompt1).strip().upper()

            if amount_input == 'Q':
                break
                
            try:
                amount = float(amount_input)

                if amount < 100:
                    print(center_text(banner()))
                    print(center_text("!!! Error: Minimum deposit is 100 pesos !!!"))
                    print(center_text(banner()))              
                else:
                    account.balance += amount 
                    print(center_text(banner()))
                    print(left_text(f"Succesfully Deposited: {amount:,.2f}", offset=18))
                    print(left_text(f"The current balance is: {account.balance:,.2f}", offset=18))
                    print(center_text(banner()))

                    print(center_text("...Please Enter to continue..."))
                    break

            except ValueError:
                print("\n" + center_text(banner()))
                print(center_text("!!! Error: Please enter a valid numeric amount !!!"))
                print(center_text(banner()))
            

            
