

def guess_number():
    import random
    random = random.randint(1,100)
    print(random)
    num = input('1-100の数字を入力してください')
    numlist = []
    numlist.append(num)
    i=0
    if int(numlist[i]) < random:
            print('もっと大きいよ')
    else :
            print('もっと小さいよ')
    
    while int(numlist[i]) != random :
        num = input('1-100の数字を入力してください')
        numlist.append(num)
        
        if int(numlist[i]) < random:
            print('もっと大きいよ')
        else :
            print('もっと小さいよ')
        i = i+1


    long = len(numlist)
    print( str(long) +'回で正解しました。')
    for l in numlist :
        print('入力'+str(l))
    return


guess_number()

