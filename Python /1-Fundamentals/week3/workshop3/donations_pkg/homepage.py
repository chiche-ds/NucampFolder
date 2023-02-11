def show_homepage():
    print("         === DonateMe Homepage ===       ")
    print("------------------------------------------")
    print("| 1.   Login     | 2.    Register         |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.  show donations   |")
    print("------------------------------------------")
    print("|            5.    Exit                  |")
    print("------------------------------------------")



def donate(username):
    donate_amt = input("Enter amount to donate:")
    donation_string = username + " donated " + donate_amt
    print("Thank you for your donation")
    return donation_string



def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for n in donations:
            print(n)
            