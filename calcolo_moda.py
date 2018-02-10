_DEBUG = False

def moda(lista):
    moda = 0
    for i in a:
        if _DEBUG:
            print(i, moda, a.count(i), end=' ')
        if a.count(i) > a.count(moda):
            moda = i
            if _DEBUG:
                print('-> ', i, end=' ')
        print()
    return moda

a = [1,2,3,4,1,2,67,8,1,2,7,1,7,9,11,5,1,11,1,1,5,6,3]
moda(a)
