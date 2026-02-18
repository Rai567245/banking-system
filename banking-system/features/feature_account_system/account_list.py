from features.feature_account_system.account_system import Account

accounts = [
    Account("0123-4567-8901", "Roel Richard", 5000.00, "1111", "Active"),
    Account("2345-6789-0123", "Dorie Marie", 0.00, "2222", "Blocked"),
    Account("3456-7890-1234", "Railee Darrel", 10000.00, "3333", "Active"),
    Account("4567-8901-2345", "Railynne Dessirei", 2500.00, "4444", "Active"),
    Account("5678-9012-3456", "Raine Dessirei", 10000.00, "5555", "Active"),
    Account("0000-1111-2222", "RaiTech", 5000.00, "0119", "Active")  
]

def find_account(acc_num):
    for acc in accounts:
        if acc.acc_num == acc_num:
            return acc
    return None