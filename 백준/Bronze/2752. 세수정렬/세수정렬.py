lst = list( map(int, input().split()) )



for i in range(len(lst)):
    minx = lst[i]
    for k in range(i+1, len(lst)):
        
        if lst[k] <= minx:
            minx = lst[k]
            
            lst[i], lst[k] = lst[k], lst[i]
        
for x in lst:
    print(x, end=' ')