# user_menu
sender = input('Account Number \n') #Account Number is fetched from the Login Details
import Employee_end as Ee
import sys
while(True):
    a = input('Enter \n1. For Net Transactions.\n2. For Transaction History.\n3. For Account Details.\nElse press any key to exit\n')
    if(a == '1'):
        while(True):
            amount = input("Enter the amount in Rupees to Transfer\n")
            if(amount.isdigit()):
                amount = int(amount)
                beneficiary = input("Enter the Sender's account Number\n")
                if(Ee.check_account(beneficiary)[0]):
                    value = Ee.trans(amount, 1, sender, beneficiary)
                    print(value)
                    c = input('Enter Y to Do again Else Press Any key to Menu\n').lower()
                    if(c != 'y'):
                        break
                else:
                    print("beneficier's Account Dosen't Exists\n")
                    c = input('Enter Y to Do again Else Press Any key to Menu\n').lower()
                    if(c != 'y'):
                        break
    if(a == '2'):
            while(True):
                if(Ee.check_account(sender)[0]):
                    value = Ee.trans_history(sender)
                    if(value[0]):
                        if(value[1][0] is not None):
                            print("Transid      Sender      Beneficiary      Date      Sender_amount")
                            for i in value[1][0]:
                                print(i, end = '  ')
                            print()
                        if(value[1][1] is not None):
                            print('Transid      Sender      Beneficiary      Date      Beneficiary_amount')
                            for i in value[1][1]:
                                print(i, end = ' ')
                            print()
                    c = input('Enter Y to Do again Else Press Any key to Menu\n').lower()
                    if(c != 'y'):
                        break
                else:
                    print(Ee.check_account(sender)[1])
                    c = input('Enter Y to Do again Else Press Any key to Menu\n').lower()
                    if(c != 'y'):
                        break
    if(a == '3'):
        pass # This part of the program is not completed
    else:
        sys.exit()