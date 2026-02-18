from features.feature_login_auth.login_authentication_feature import LoginAuthenticationSection
from utils.center_text_ui import center_text
from utils.left_text_ui import left_text
from utils.banner_ui import banner

def main():
    login_process = LoginAuthenticationSection()

    while True:
        print("\n")
        print(center_text(banner()))
        print(center_text("|                  Banking System (Landing Page)                  |"))
        print(center_text(banner()))

        print(left_text("S -> Start Transaction", offset=23))
        print(left_text("Q -> Quit", offset=29))
        print(center_text(banner()))

        prompt = left_text("Enter your choice: ", offset=24).rstrip()
        choice = input(prompt).upper().strip()

        if choice == 'S':
            logged_in_account = login_process.login_section()

            if logged_in_account:
                pass
        
        elif choice == 'Q':
            print(center_text(banner()))
            print(center_text("Thankyou for using RGBC. Goodbye!"))
            print(center_text(banner()) + "\n")
            break
        else:
            print()
            print(center_text("Invalid Choice. Please try again."))
            
if __name__ == "__main__":
    main()