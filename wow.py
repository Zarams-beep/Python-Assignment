def reverse_str(strii):
    nor_typ=type(strii)
    ar=[]
    wow=[n for n in strii]
    for num in range(len(wow)):
        ar.append(wow.pop())
    g="".join(ar)
    n=nor_typ(g)
    print(type(n))
    print(n)
