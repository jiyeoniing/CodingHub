w = input()   #Mississipi

word = w.upper()
words = list(word)

#중복제거
word_set = list(set(word))   #['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'i']


cnt = []
for w in word_set:
    cnt.append( words.count(w))

maxn = max(cnt)
if cnt.count(maxn) == 1:
    indx = cnt.index(maxn)
    print(word_set[indx])
else:
    print('?')