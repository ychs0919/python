import random

num = int(input('로또 복권을 몇 장 구입 하실래요?'))
table = [] #여러장의 로또 복권 번호

for i in range(num):
    sList =[]
    j=0
    while j<6 :#로또 번호 6개 입력받음
        temp=random.randint(1,45)
        if not len(sList) : sList.append(temp)
        else :
            for k in range(len(sList)) :
                if sList[k] == temp:
                    j-=1
                    break
            else : sList.append(temp)
        j+=1
    sList.sort()  #오름차순정렬
    table.append(sList) #table에 로또번호 6개 세트 넣음

for i in range(len(sList)):
    print(table[i])
