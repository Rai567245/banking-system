from features.feature_balance_inquiry.balance_inquiry_feature import BalanceInquirySection
from features.feature_withdrawal.withdrawal_feature import WithdrawalSection
from features.feature_deposit.depositing_feature import DepositingSection
from features.feature_transfer_funds.transfering_fund_feature import TransferFundSection
from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

class TransactionMenuSection:
    checking_balance_process = BalanceInquirySection()
    withdraw_amount_process = WithdrawalSection()
    deposit_amount_process = DepositingSection()
    transfer_amount_process = TransferFundSection()

    def transaction_process(self, account): 
        while True:
            print(center_text(banner()))
            print(center_text("|                    Banking System (Menu Page)                   |"))
            print(center_text(banner()))

            print(left_text("B -> Balance Inquiry", offset=24))
            print(left_text("W -> Withdrawal", offset=26))
            print(left_text("D -> Deposit", offset=28))
            print(left_text("T -> Transfer Fund", offset=25))
            print(left_text("C -> Cancel", offset=28))
            
            print(center_text(banner()))
            prompt1 = left_text("Enter transaction type: ", offset=22).rstrip()
            choice = input(prompt1).upper().strip()
            print(center_text(banner()))

            match choice:
                case 'B':
                    print(center_text("...Loading Balance Inquiry..."))
                    self.checking_balance_process.show_balance(account)
                case 'W':
                    print(center_text("...Loading Withdrawal..."))
                    self.withdraw_amount_process.withdraw_money(account)
                case 'D':
                    print(center_text("...Loading Deposit..."))
                    self.deposit_amount_process.deposit_money(account)
                case 'T':
                    print(center_text("...Loading Transfer Funds..."))
                    self.transfer_amount_process.transfer_fund(account)
                case 'C':
                    print(center_text("...Transaction Cancelled. Returning to Menu..."))
                    break
                
                
                

                