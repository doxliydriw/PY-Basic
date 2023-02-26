nmbr_set =  (-2, -1.2, -6, -9, -45)
nmbr_set = list(nmbr_set)
maxnmbr = nmbr_set[0]
minnmbr = nmbr_set[0]
for i in nmbr_set:
    print(i)
    if i > maxnmbr:
        print('max', i > maxnmbr)
        maxnmbr = i
    elif i < minnmbr:
        print('min', i < maxnmbr)
        minnmbr = i
print(maxnmbr,  minnmbr)
print(maxnmbr - (minnmbr))
