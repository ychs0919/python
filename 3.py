import math #버림하기위해설정
num = input("임의의 정수 입력 : ")
i=1
sum=0


if int(num)>0:
    temp = int(num)    
    while int(len(num)) >= i:
    
        a = temp%10  #10으로 나눈것의 나머지를 a로 저장
        i+=1
        temp = math.trunc(temp/10) # 입력받은 수를 10으로 나누고 소숫점은 버리고 while을 다시 돌게 만들어줌
    
        sum = sum+a
    print(num,": ",int(len(num)),"자리 정수")
    print("각 자리의 총합 : ",sum)

elif int(num) < 0:  #입력값이 음수일때
    num = str(-int(num))  #음의 부호를 곱해주고 다시 문자열로 반환
    temp = int(num)
    while int(len(num)) >= i:
    
        a = temp%10  #10으로 나눈것의 나머지를 a로 저장
        i+=1
        temp = math.trunc(temp/10) # 입력받은 수를 10으로 나누고 소숫점은 버리고 while을 다시 돌게 만들어줌
    
        sum = sum+a
    print(num,": ",int(len(num)),"자리 정수")
    print("각 자리의 총합 : ",sum)


