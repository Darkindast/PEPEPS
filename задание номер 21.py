def vut12(x, p):
    if x>=30 and x <=61 and (p==3 or p==5):
        return True
    if x<30 and x > 61 and p==5:
        return False
    if x>=30 and x <=61:
        return False

    if p%2==1:
        return vut12(x+3, p+1) and vut12(x*2, p+1)
    else:
        return vut12(x+3, p+1) or vut12(x*2, p+1)

maxx = 0
minn = 10**10
for s in range(1, 30):
    if vut12(s, 1):
        print(s)
        if s > maxx:
            maxx = s
        if s < minn:
            minn = s
print()
print(maxx+minn)

        
