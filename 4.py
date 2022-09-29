year = int(input("년도입력 :"))

if (year%400==0):
    print(year,"년은 윤년입니다.")
elif(year%4==0 and year%100==0):  #and를 사용해 두가지 조건을 만족시키면 윤년이라는 조건을 추가함
    print(year,"년은 평년입니다.")
elif(year%4==0):
    print(year,"년은 윤년입니다.")
else : print(year,"년은 평년입니다.")
