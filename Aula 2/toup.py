def toup(s): 
    temp = "" 
    for c in s:
        if c.islower():
            c = c.upper()
        temp = temp + chr(ord(c)) 
    return temp 

s = "menteb.in"     
print(toup(s))