"""have @ (only 1 time)
no upper case letter
only under_score and @ character are allowed"""

email=input("enter your email address ")
len=len(email)
space=0
upper=0
count=0
if len>=6:     #  t@g.in (length=6 " that is minium length")
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-3]=='.') or (email[-4]=='.') and (email.count('.')==1):
                for i in email:
                    if i==i.isspace():
                        space=1
                    elif i.isalpha():
                        if i==i.upper():
                            upper=1
                    elif i.isdigit():
                        continue
                    elif i=='@' or i=='.' or i=='_':
                        continue
                    else:
                        count=1
                if (space==1) or (upper==1) or (count==1):
                    print("Wrong Email Address you entered (reason : space is there or big alphabet is there or not allowed special character is there) ")
                else:
                    print("You Entered Right Email Address")
            else:
                print("Wrong Email Address you entered (reason : dot position is not in it place )")
        else:
            print("Wrong Email Address you entered (reason: may be you entered more than one @ or not entered any @)")
    else:
        print("Wrong Email Address you entered (reason : first index mus be alphabet)")
else:
    print("Wrong Email Address you entered (reason: length less than 6 is not allowed )")


""" builtin function that used in my code:
    isalpha()
    count()
    isspace()
    upper()
    isdigit()"""