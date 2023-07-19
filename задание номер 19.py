def vut1(x, p):
    if x>=30 and x <=61 and p==3:
        return True
    if x<30 and x > 61 and p==3:
        return False
    if x>=30 and x <=61:
        return False

    if p%2==1:
        return vut1(x+3, p+1) and vut1(x*2, p+1)
    else:
        return vut1(x+3, p+1) or vut1(x*2, p+1)
maxx = 0

for s in range(1, 30):
    if vut1(s, 1):
        print(s)
        if s > maxx:
            maxx = s
print()
print(maxx)
