from features.feature_account_system.account_list import find_account
from features.feature_transaction_menu.transaction_menu_feature import TransactionMenuSection
from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class LoginAuthenticationSection:
    transaction = TransactionMenuSection()

    def login_section(self):
        print(center_text(banner()))
        print(center_text("|                   Banking System (Login Page)                   |"))
        print(center_text(banner()))

        propmt_1 = left_text("Enter your account number: ", offset=20).rstrip()
        acc_num = input(propmt_1).strip()
        account = find_account(acc_num)

        if not account:
            print(left_text("Invalid account number: ", offset=27))
            return None
        
        if account.status == "Blocked":
            print("\n\n" + center_text(banner()))
            print(center_text("!!! ACCOUNT BLOCKED !!!"))
            print(center_text("PLEASE CALL 143-44 FOR ASSISTANCE"))
            print(center_text(banner()))
            return None
        
        attempts = 0
        while attempts < 3:
            propmt_2 = left_text("Enter your pin number: ", offset=22).rstrip()
            pin = input(propmt_2).strip()

            if pin == account.pin:
                print(center_text(banner()))
                print(center_text("Login Successful!"))
                
                menu = TransactionMenuSection()
                menu.transaction_process(account)
            
                return account
            
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(center_text(f"Incorrect PIN! Attempts left: {remaining}"))
            else:
                account.status = "Blocked"
                print(center_text("CAPTURE CARD.... PLEASE CALL 143-44"))
                return None
            
        return None

