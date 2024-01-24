x = int(input())

i = 0
old = x
new=-1
while old != new:
    if x < 10:
        s = x
        new = 10*x + x
    else:
        first = x//10   #2
        second = x%10    # 6
        s = first + second
        new = (x%10)*10 + (s%10)
    x = new
    i += 1
        
print(i)