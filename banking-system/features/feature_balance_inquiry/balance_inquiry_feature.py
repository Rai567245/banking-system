from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class BalanceInquirySection:
    def show_balance(self, account):
        while True:
            print(center_text(banner()))
            print(center_text(f"|               Banking System (Balance Inquiry Page)             |"))
            print(center_text(banner()))

            print(left_text(f"Account Name: {account.name}", offset=23))
            print(left_text(f"Account Balance: {account.balance}", offset=22))
            print(left_text(f"Account Status: {account.status}", offset=23))

            print(center_text(banner()))
            prompt1 = left_text("Press (Q) to Quit: ", offset=24).rstrip()
            choice = input(prompt1).upper().strip()

            if choice == 'Q':
                print(center_text(banner()))
                print(center_text("...Now Returning To Main Menu..."))
                break