#Employee Menu
import sys


import Employee_end as Ee

def anvv(account):
        if(account.isdigit()):
                if(len(account) == 16):
                    if(Ee.check_account(account)):
                        return (True,)
                    return (False, "Account Doesn't Exists\n")
                return(False, "Account Number is not of 16 digits\n")
        return(False, "Please Enter Numbers Only\n")
while(True):
    a = int(input('''Press the following keys for the repective functions\n
        1 - New User
        2 - User Details
        3 - Transaction
        4 - Transaction History
        5 - Close Account
        6 - Else press any key to exit\n'''))
    if (a == 1):
        b = input('Enter Name \n\n').capitalize()
        c = input('\n\nEnter Phone Number\n\n')
        d = input('\n\nEnter Email\n\n')
        value = Ee.new_user(b,c,d)
        print(value[1])

    elif(a == 2):
        b = input('Enter Account Number\n')
        if(anvv(b)[0]):
            for i in Ee.account_details(b):
                for j in i:
                    print(j, "  ",end = '')
                print()
        else:
            print(anvv(b)[1])

    elif(a == 3):
        while(True):
            b = input('Enter \n1 - For Bank to Bank Transaction \n2 - For Cash withdrawal by Customer \n3 - For Cash credit by Customer\n')
            if(b.isdigit()):
                b = int(b)
                if(b in range(1,4)):
                    if(b == 1):
                        amount = input("Enter the amount in Rupees to Transfer\n")
                        if(amount.isdigit()):
                            amount = int(amount)
                            sender = input("Enter the Sender's account Number\n")
                            if(anvv(sender)[0]):
                                beneficiary = input("Enter the Benificiarie's Account Number\n")
                                if(anvv(beneficiary)[0]):
                                    value = Ee.trans(amount, 1, sender, beneficiary)
                                    print(value)
                                    c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                                    if(c != 'y'):
                                        break
                                else:
                                    print("Benificier's Account Dosen't Exists\n")
                                    c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                                    if(c != 'y'):
                                        break
                            else:
                                print("Sender's Account Number Doesn't Exists\n")
                                c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                                if(c != 'y'):
                                    break
                        else:
                            print("Please Enter Amount In Digits only")
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
            if (b==2):
                    amount = input("Enter the amount in Rupees to Transfer\n")
                    if(amount.isdigit()):
                        amount = int(amount)
                        sender = input("Enter the Sender's account Number\n")
                        if(anvv(sender)[0]):
                            value = Ee.trans(amount, b, sender)
                            print(value)
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                        else:
                            print(anvv(sender)[1],'\n')
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                    else:
                        print('Please Enter Digits Only\n')
                        c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                        if(c != 'y'):
                            break
            else:
                    amount = input("Enter the amount in Rupees to Transfer\n")
                    if(amount.isdigit()):
                        amount = int(amount)
                        Beneficiary = input("Enter the Beneficier's account Number\n")
                        if(anvv(Beneficiary)[0]):
                            value = Ee.trans(amount, b, Beneficiary)
                            print(value, '\n')
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                        else:
                            print(anvv(Beneficiary)[1], '\n')
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                    else:
                        print('Please Enter digits Only\n')
                        c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                        if(c != 'y'):
                            break
    elif(a == 4):
        while(True):
            account = input('Enter Account Number\n')
            if(anvv(account)[0]):
                value = Ee.trans_history(account)
                if(value[0]):
                    if(value[1][0] is not None):
                        print("Transid      Sender      Beneficiary      Date      Sender_amount")
                        for i in value[1][0]:
                            print(i, end = ' ')
                        print()
                    if(value[1][1] is not None):
                        print('Transid      Sender      Beneficiary      Date      Beneficiary_amount')
                        for i in value[1][1]:
                            print(i, end = ' ')
                        print()
                c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                if(c != 'y'):
                    break
            else:
                print(anvv(account)[1])
                c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                if(c != 'y'):
                    break
    elif(a == 5):
        account = input('Enter Account Number\n')
        if(anvv(account)[0]):
            b = input('Enter Y if you are Sure to delete account where account number = '+account + '\n').lower()
            if(b == 'y'):
                 value = Ee.trans(Ee.check_balance(account), 4, account)
                 print(value, '\n')
    else:
        sys.exit()