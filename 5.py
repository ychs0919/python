a = int(input("임의의 정수(1~9) : ")) #입력받은 정수

for i in range(1,a+1):
    k=1
    for j in range(1,a+1):
        if (i>=j) :
            print(int(k),end = ' ') # 줄바꿈 없이 출력을 할 수 있게 도와주는 end = ''
            k=k+1
        else : print("*",end = ' ')
    print("")

