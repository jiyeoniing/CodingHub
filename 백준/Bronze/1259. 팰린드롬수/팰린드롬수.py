while True:
    x = input()
    if x == '0':
        break
    
    else:
        if x == x[::-1]:
            print('yes')
    
        else:
            print('no')
    