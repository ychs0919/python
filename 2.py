l = float(input("거리(km) : "))
v = float(input("속력(km/h) : "))
t = (l // v) * 3600
h = int(t) // 3600
m = int((t - (h * 3600))) // 60
s = (t - (h * 3600) - (m * 60))

print("예상 소요 시간 : ",h,"시간",m,"분",s,"초")
