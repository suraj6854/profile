email=input("Enter the email")
k,j,d=0,0,0
if len(email)>=6:
        if email[0].isalpha():
            if (email[-1:-9]=="gmail.com") ^(email[-1:-8]=="gmail.in"):
                pass
            else:
                print("wrong email 6")
            if ("@" in email) and (email.count("@")==1):
                if (email[-4]==".") ^ (email[-3]=="."):
                    for i in email:
                        if i.isspace():
                            k=1
                        elif i.isalpha():
                            if i==i.upper():
                                j=1
                        elif i.isdigit():
                            continue
                        elif i=="-" or i=="." or i=="@":
                            continue
                        else:
                            d=1
                    if k==1 or j==1 or d==1:
                        print("wrong email 5")

                else:
                    print("wrong email 4")
            else:
                print("wrong email 3")
        else:
            print("wrong email 2")
else:
    print("Wrong email 1")