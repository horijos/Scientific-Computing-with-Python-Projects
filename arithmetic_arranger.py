class ToomanyproblemsExc (Exception):
    "Raised when the input value is less than 18"
    pass


def arithmetic_arranger(*nums):

    n = {}
    signos = []

    if len(nums[0])>5:
        raise TypeError("Error: Too many problems.")

    for e in nums[0]:
        ele = e.split()
        if len(ele) !=3:
            raise TypeError("Error: Too many problems.")
        
        else:
            if ele[1]!='+' and ele[1]!='-':
                raise TypeError("Error: Operator must be '+' or '-'.")

            if ele[0].isnumeric()==False and ele[2].isnumeric()==False:
                raise TypeError("Error: Numbers must only contain digits.")

            if len(ele[0])>4 or len(ele[1])>4:
                raise TypeError("Error: Numbers cannot be more than four digits.")
     
            n[ele[0]]=ele[2]
            signos.append(ele[1])

    for e in n.keys():
        r = max(len(e),len(n[e]))
        print (f'{int(e):{r+2}d}',end="    ")
    print()

    cont=0
    for e in n.keys():
        r = max(len(e),len(n[e]))
        x = signos[cont]
        print(f'{x} ',end="")
        print (f'{int(n[e]):{r}d}',end="    ")
        cont=cont+1
    print()

    for e in n.keys():
        r = max(len(e),len(n[e]))
        for i in range(r+2):
            print("-",end="")
        print("    ",end="")
    print()

    if len(nums)==2:
        if nums[1]==True:
            cont = 0;
            for e in n.keys():
                r = max(len(e),len(n[e]))
                res = 0;
                if signos[cont]=='-' :
                    res=int(e)-int(n[e])
                else:
                    res=int(e)+int(n[e])
                print (f'{res:{r+2}d}',end="    ")
                cont=cont+1
        print()

    print()

a=["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49","1 + 1"]

arithmetic_arranger(a,True)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
