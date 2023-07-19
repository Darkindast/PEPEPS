def put2(x, p):
    if x>=30 and x <=61 and p==4:
        return True
    if x<30 and x > 61 and p==4:
        return False
    if x>=30 and x <=61:
        return False

    if p%2==0:
        return put2(x+3, p+1) and put2(x*2, p+1)
    else:
        return put2(x+3, p+1) or put2(x*2, p+1)
maxx = 0
mas =[]
for s in range(1, 30):
    if put2(s, 1):
        mas.append(s)
        print(s)
print()
mas.sort()   
print(mas[len(mas)//2])

        
