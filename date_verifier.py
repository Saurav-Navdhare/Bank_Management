# Date Verification Module


def leap_year(a):
    b = int(a[:4])
    return bool((b%4 == 0 and b%100 != 0) or b% 400 == 0)
        

def month_verify(a):
    b = int(a[5:7])
    if(b > 0 and b < 13):
        if( b in "01 03 05 07 08 10 12".split()):
            return (True,'1')
        elif(b in "04 06 09 11".split()):
            return (True,'2')
        else:
            return (True,'3')
    else:
        return (False,"Month should only lie between 1 to 12")

def date_verify(a):
    b = int(a[8:])
    if(month_verify(a)[0]):
        if(b > 1 and b < 32):
            c = month_verify(a)[1]
            if(c == '1'):
                return (True,)
            elif(c == '2'):
                if(b < 31):
                    return (True,)
                else:
                    return(False, 'Date in this month must be between 0 to 30')
            else:
                if(leap_year(a)):
                    if (b < 30):
                        return (True,)
                    else:
                        return (False, 'Date in February of Leap year must be in 0 to 29')
                else:
                    if(b < 29):
                        return (True,)
                    else:
                        return (False, 'Date in February of a Normal year must be in 0 to 28')
        else:
            return (False, 'Date on any month must be in 0 to 31')

    else:
        return month_verify(a)

def date_input():
    a = input('Enter Year \n')
    a = '0'*(4-len(a))+a
    b = input('Enter Month \n')
    b = '0'*(2 - len(b))+b
    c = input('Enter Date \n')
    c = '0'*(2 - len(c))+c
    d = a+'/'+b+'/'+c
    if(month_verify(d)[0]):
        if(date_verify(d)[0]):
            return(True, d)
        else:
            return(False, date_verify(d)[1])
    else:
        return(False, month_verify(d)[1])


print(date_input())