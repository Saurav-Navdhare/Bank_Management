#Employee Menu
import sys
import mysql.connector
import Employee_end as Ee

mydb = mysql.connector.connect(host='localhost',
                                user='root',
                                passwd='admin')
mycursor =  mydb.cursor(buffered=True)

while(True):
    a = input('''Press the following keys for the repective functions\n
        1 - New User
        2 - User Details
        3 - Transaction
        4 - Transaction History
        5 - Close Account
        6 - Else press any key to exit\n''')
    if(a.isdigit()):
        a = int(a)
    else:
        sys.exit()
    if (a == 1):
        b = input('Enter Name \n\n').capitalize()
        c = input('\n\nEnter Phone Number\n\n')
        d = input('\n\nEnter Email\n\n')
        value = Ee.new_user(b,c,d)
        print(value[1])

    elif(a == 2):
        b = Ee.select_account(input('Enter Name of Account Holder\n'))
        mycursor.execute("select * from user where account = %s", (b,))

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
                            sender = Ee.select_account(input('Enter Name of Account Holder\n'))
                            if(sender is not None):
                                beneficiary = Ee.select_account(input('Enter Name of Account Holder\n'))
                                if(beneficiary is not None):
                                    value = Ee.trans(amount, 1, sender, beneficiary)
                                    print(value)
                                    c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                                    if(c != 'y'):
                                        break
                                else:
                                    print("Beneficiar's Account Do not Exsists\n")
                                    c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                                    if(c != 'y'):
                                        break
                            else:
                                print("Sender's Account Do not Exsists\n")
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
                        sender = Ee.select_account(input('Enter Name of Account Holder\n'))
                        if(sender is not None):
                            value = Ee.trans(amount, b, sender)
                            print(value)
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                        else:
                            print("Sender's Account Do not Exsists\n")
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
                        Beneficiary = Ee.select_account(input("Enter the Name of account Holder\n"))
                        if(Beneficiary is not None):
                            value = Ee.trans(amount, b, Beneficiary)
                            print(value, '\n')
                            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                            if(c != 'y'):
                                break
                        else:
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
            account = Ee.select_account(input('Enter Name of Account Holder\n'))
            if(account is not None):
                value = Ee.trans_history(account)
                if(value[0]):
                    if(value[1][0] is not None):
                        print("Transid      Sender      Beneficiary      Date      Sender_amount")
                        for i in value[1][0]:
                            print(i, end = '  ')
                        print()
                    if(value[1][1] is not None):
                        print('Transid      Sender      Beneficiary      Date      Beneficiary_amount')
                        for i in value[1][1]:
                            print(i, end = '  ')
                        print()
                c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                if(c != 'y'):
                    break
            else:
                print("Account does not exsists")
                c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
                if(c != 'y'):
                    break
    elif(a == 5):
        account = Ee.select_account(input('Enter Name of Account Holder\n'))
        if(account is not None):
            b = input('Enter Y if you are Sure to delete account where account number = '+account + '\n').lower()
            if(b == 'y'):
                value = Ee.trans(str(Ee.check_balance(account)), 4, account)
                print(value, '\n')
        else:
            print("Account does not exsists")
            c = input('Enter Y to Do again Else Press Any key to Exit\n').lower()
            if(c != 'y'):
                break
    else:
        sys.exit()