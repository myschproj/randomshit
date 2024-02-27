def f(s, mh, h=0):
    if s >= 29:
        if h % 2 == 1:return 1
        else: return 2
    h = h + 1
    if h > mh: return 0
    rez = []
    rez.append(f(s+1, mh, h))
    rez.append(f(s*2, mh, h))
    if h % 2 == 1:
        if 1 in rez: return 1
        elif 0 in rez: return 0
        else: return 2
    else:
        if 2 in rez: return 2
        elif 0 in rez: return 0
        else: return 1
print(' ', end='\t')
for mh in range(1, 5):
    print(mh, end='\t')
print()
for s in range(1, 28+1):
    print(mh, end='\t')
    for mh in range(1, 5):
        print(f(s, mh), end='\t')
    print()
