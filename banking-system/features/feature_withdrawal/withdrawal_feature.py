from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class WithdrawalSection:
    def withdraw_money (self, account):
        while True:
            print(center_text(banner()))
            print(center_text("|                 Banking System (Withdrawal Page)                |"))
            print(center_text(banner()))
 
            print(left_text(f"Current Balanace: {account.balance:,.2f}", offset=21))
            promp1 = left_text("Enter the amount to be withdrawn (or Q to Quit): ", offset=9).rstrip()
            amount_input = input(promp1).strip().upper()

            if amount_input == 'Q':
                break
            
            try:
                amount = float(amount_input)

                if amount < 100:
                    print(center_text(banner()))
                    print(center_text("!!! Error: Minimum withdrawal is 100 pesos !!!"))                
                elif amount % 100 != 0:
                    print(center_text(banner()))
                    print(center_text("!!! Error: Amount must be in 100 denominations (e.g., 100 or 500) !!!"))
                elif amount > account.balance:
                    print(center_text(banner()))
                    print(center_text("!!! Error: Insufficient balance !!!"))
                else:
                    account.balance -= amount
                    print(center_text(banner()))
                    print(left_text(f"Successfully withdrawn: {amount:,.2f}", offset=18))
                    print(left_text(f"New Balance: {account.balance:,.2f}", offset=23))
                    print(center_text(banner()))
                    input(center_text("....Press Enter to continue..."))
                    break

            except ValueError:
                print(center_text(banner()))
                print(center_text("!!! Error: Please enter a valid numeric amount !!!"))