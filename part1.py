rangelist=[0,20,40,60,80,100,120]
total=0
while True:
    try:
        pass_credit=int(input("enter the credit at pass:"))
        if pass_credit not in rangelist:
            print("invalid range 1")
            continue
        defer_credit=int(input("enter the credit at defer:"))
        if defer_credit not in rangelist:
            print("invalid range 2")
            continue
        fail_credit=int(input("enter the credit at fail:"))
        if  fail_credit not in rangelist:
            print("invalid range 3")
            continue
        break
        if pass_credit==120:
            print("progress")
        elif pass_credit==100:
            print("progress - module trailer")
        elif fail_credit>=80:
            print("Exclude")
        else:
            print("do not progress - module retriever")
    except ValueError:
        print("please enter a integer value")
        continue
total=pass_credit+defer_credit+fail_credit
if total!=120:
    print("total incorrect")

    
    

