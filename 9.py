class Cal:
    def __init__(self,first,second):
        self.first =first
        self.second = second
        self.getFirst = self.first
        self.getSecond = self.second
    def add(self) : return self.first + self.second
    def sub(self) : return self.first - self.second
    def mul(self) : return self.first * self.second
    def div(self) : return self.first / self.second

print("두개의 정수를 입력하시오...")
first = int(input("first: "))
second = int(input("second: "))

class subCal(Cal):
    
    def pow(self):
        return self.getFirst()**self.getSecond()
    def div(self):  #Cal 에서 지원하는 div기능을 덮어쓴다.
        if self.getSecond() == 0 :
            return 0
        else : return self.getFirst()/self.getSecond()
#새로운 객체 newCal생성
newCal = subCal(first,second)
print(newCal.first,"/",newCal.second,"=",newCal.div())
