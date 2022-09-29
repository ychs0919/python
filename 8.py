def telInput():
    print('[입력모드]')
    while True :
        name =input("이름: ")
        if not name : break
        tel = input("연락처: ")
        sDict[name] =tel
    
def telSearch():
    print('[검색모드]')
    while True:
        name = input('이름: ')
        if not name : break
        if name in sDict :
            print(name,"의 전화번호는 ",sDict[name],"입니다.")
sDict = {}
while True:
    print("##### 전화번호부 #####")
    print("1 : 입력")
    print("2 : 검색")
    print("3 : 종료")
    num = int(input("메뉴선택 : "))

    if num ==1: telInput()   #1입력하면 입력모드
    elif num ==2: telSearch()  #2입력하면 검색모드
    elif num ==3: break        #3입력하면 종료
    else: print("잘못된선택!")
