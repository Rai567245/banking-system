from features.feature_account_system.account_list import find_account
from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class TransferFundSection:
    def transfer_fund(self, account):
        while True:
            print(center_text(banner()))
            print(center_text("|              Banking System (Transfer Fund Section)             |"))
            print(center_text(banner()))

            print(left_text(f"Your Current Balance: {account.balance:,.2f}", offset=19))
            
            prompt1 = left_text("Enter Recipient Account Number (or Q to Quit): ", offset=10).rstrip()
            target_acc = input(prompt1).upper().strip()

            if target_acc == 'Q':
                break

            recipient = find_account(target_acc)
            if not recipient:
                print(center_text("!!! Error: Recipient account not found !!!"))
                continue

            prompt2 = left_text("Enter amount to transfer: ", offset=21).rstrip()
            amount_input = input(prompt2).strip()
            
            try:
                amount = float(amount_input)
                
                if amount < 1000:
                    print(center_text("!!! Error: Minimum transfer is 1000 pesos !!!"))
                    continue

                fee = (amount // 1000) * 15
                total_deduction = amount + fee

                if total_deduction > account.balance:
                    print(center_text(f"!!! Error: Insufficient funds (Needed: {total_deduction:,.2f}) !!!"))
                else:
                    account.balance -= total_deduction 
                    recipient.balance += amount         
                    
                    print(center_text(banner()))
                    print(center_text(f"Transfer Successful to {recipient.name}!"))
                    print(center_text(f"Amount: {amount:,.2f} | Fee: {fee:,.2f}"))
                    print(center_text(f"New Balance: {account.balance:,.2f}"))
                    print(center_text(banner()))
                    print(center_text("...Press Enter to continue..."))
                    break

            except ValueError:
                print(center_text("!!! Error: Invalid numeric amount !!!"))