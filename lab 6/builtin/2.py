def upper_lower(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
           d["upper"]+=1
        elif c.islower():
           d["lower"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("Upper case : ", d["upper"])
    print ("Lower case : ", d["lower"])

n = input()
upper_lower(n)