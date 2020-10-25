#This File contains all the sql functions requireed in the project including a) Create Account b) Transaction option with Bank -> Bank, Bank-> Customer, Customer -> Bank, c) Transaction History, d) Delete Account
import mysql.connector
from datetime import date, datetime
from date_verifier import date_input

Date = date.today().strftime('%Y/%m/%d')





mydb = mysql.connector.connect(host='localhost',
                                user='root',
                                passwd='admin')
mycursor =  mydb.cursor(buffered=True)
mycursor.execute('Create database if not exists bank_Management')
mycursor.execute('Use Bank_Management')
mycursor.execute('create table if not exists user(account char(17) Primary Key, name Varchar(20) Not Null, Phone char(11) Unique Not Null,email varchar(35) Unique Not Null, Balance int(10) check(Balance >-1) Not Null, transid varchar(25) not null, TOA varchar(10) Not Null, DOC date Not Null)')
mycursor.execute('create table if not exists trans(Sender char(17) references user(account), Beneficiary char(17) references user(account), transid varchar(25) not null, date date not null, amount int(10), bank int(10) check(bank>-1))')           
# Will be called When approved by an employee ; Employee Menu Side

def check_details(phone, email):
    k = 0
    mycursor.execute('Select phone from user')
    for i in mycursor:
        if(phone in i):
            k=1
            break
    else:
        mycursor.execute('select email from user')
        for j in mycursor:
            if(email in j):
                k=2
                break
        return (True,)
    if(k == 1):
        return (False,'Phone Number Already Exists in Database')
    return (False,'Email Already Exsists in database')

def new_user( name, phone, email):

    if not(check_details(phone ,email)[0]):
        return check_details(phone,email)

    account = datetime.today().strftime('%Y%m%d%H%M%S%f')[:16]

    mycursor.execute("Insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)", (account, name, phone, email, 1000, account+'1', "savings", Date))
    mycursor.execute("Insert into trans values('Self', %s, %s, %s, %s, %s)",(account, account+'1', Date, 1000, 1000))
    mydb.commit()
    return (True,"Successfully new Account Created with account number - "+account+" and First Transaction id as " + account+'1')

def check_account( account):
    mycursor.execute("select account from user")
    for i in mycursor:
        if i == (account,):
            return True
    return False

def account_details( reciever):
    mycursor.execute("Select account, name, email, Balance from user where account = %s", (reciever,))
    return mycursor

def check_balance( account):
    if(check_account(account)):
        mycursor.execute("select balance from user where account = %s", (account,))
        for i in mycursor:
            for j in i:
                return j
    return "Account does not Exsist"

def transid(account):
    mycursor.execute("select transid from user where account = %s", (account,))
    for i in mycursor:
        return (account + str(int(i[0][16:])+1))

# mode must be entered from frontend side 1 = Transfer, 2 = Cash Withdrwal, 3 = Cash Deposit
def trans(amount, mode, account, reciever='Self'):
    # Mode 1 is only vaialable on Customer side, all are avaialable on Employee side

    if(mode == 1):
        if(int(check_balance(account)) >= 1000+int(amount)):
            mycursor.execute("Select account, name, email from user where account = %s", (reciever,))
            for i in mycursor:
                print(i, end='')
            print()
            a = input('Press Y if the above details about the reciever are correct\n').lower()
            if(a == 'y'):
                tid = transid(account)
                mycursor.execute("insert into trans values(%s,%s,%s,%s,%s,%s)", (account, reciever, tid, date.today().strftime('%Y/%m/%d'), amount, check_balance(account) - amount))
                mycursor.execute("Update user set balance = balance - %s where account = %s", (amount, account))
                mycursor.execute("Update user set balance = balance + %s and transid = %s where account = %s", (amount, tid, reciever))
                mydb.commit()
                return f"{amount} Rs has been transferred from {account} to {reciever}"
            return "Transaction is Aborted"
        return "Insufficient Balance"

    if(mode == 2):
        tid = transid(account)
        if(check_balance(account) >= amount+1000):
            mycursor.execute("insert into trans values(%s,'self',%s,%s,%s,%s)", (account, tid, date.today().strftime('%Y/%m/%d'), amount, check_balance(account)-amount))
            mycursor.execute("update user set balance = balance -%s where account = %s", (amount, account))
            mycursor.execute("update user set balance = balance +%s and transid = %s where account = %s", (amount, tid, reciever))
            mydb.commit()
            return str(amount)+ " Rs has been withdrawn from " + account
        return "Insufficient Balance"

    if(mode == 3):
        tid = transid(account)
        mycursor.execute("insert into trans values('self', %s, %s, %s,%s,%s)", (account, tid, date.today().strftime('%Y/%m/%d'), amount, check_balance(account)+amount))
        mycursor.execute("update user set balance = balance + %s where account = %s", (amount, account))
        mycursor.execute("update user set transid = %s where account = %s", (tid, account))
        mydb.commit()
        return f'{amount} rs has been credited to {account}'

    if(mode == 4):
        tid = transid(account)
        mycursor.execute("insert into trans values(%s,'self',%s,%s,%s,%s)", (account, tid, date.today().strftime('%Y/%m/%d'), check_balance(account), 0))
        mycursor.execute("delete from user where account = %s", (account,))
        mycursor.execute("update user set balance = balance +%s and transid = %s where account = %s", (amount, tid, reciever))
        mydb.commit()
        return str(amount)+ " Rs has been withdrawn from " + account + "And Account Has been Closed"

def istransid( account, transid):
    mycursor.execute(
        "Select transid from trans where sender = %s or beneficiary = %s", (account, account))
    for i in mycursor.fetchall():
        if i[0] == transid:
            return True
        
    return False

def trans_history(account):
    while(True):
        a = input("Enter 1. For only Transid Searched Transaction \n2. For Transaction between Specific Date Range \n3. For Transaction Made on a day\n")
        if(a.isdigit()):
            a = int(a)
            if(a in range(1, 4)):
                if(a == 1):
                    transid = input("enter transid\n")
                    if(istransid(account, transid)):
                        mycursor.execute("select * from trans where transid = %s and(sender = %s or beneficiary = %s)", (transid,account, account)) #Comment  for i in value :  print(i, '  ' ,end = '')
                        return(True, mycursor.fetchone())
                    return("False transid Provided")
                if(a == 2):  ## Needed to be recoded
                    b = date_input()
                    if(b[0]):
                        print('Enter Second Date')
                        c = date_input()
                        if(c[0]):
                            mycursor.execute("select * from trans where date between %s and %s and (sender = %s or beneficiary = %s)", (b[1], c[1], account, account))
                            return (True,mycursor.fetchall())   #Here Loop on this value and Print Details
                        return c[1]
                    return b[1]

                b = date_input()
                if(b[0]):
                    mycursor.execute("Select * from trans where date = %s and (sender = %s or beneficiary = %s)", (b[1], account, account))
                    return [True, mycursor.fetchall()]
                return b[1]
                            
def close_account( account):
    if(check_account(account)):
        if(check_balance(account) == '0'):
            mycursor.execute("delete from user where account = %s", (account,))
            mydb.commit()
            return "Account deleted Successfully"
        k = check_balance(account)
        trans(k, 3, account)
        mycursor.execute("delete from user where account = %s", (account,))
        return "Account deleted succesfully and Rs " + k + " will be returned to you as cash"
    return "account doesn't exsist"