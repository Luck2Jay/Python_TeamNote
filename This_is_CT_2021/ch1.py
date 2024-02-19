import time

start_time = time.time()  #측정시작

#프로그램 소스코드
a = 0
print(a)

a = 1e9
print(a)

a = int(1e9)
print(a)

a = 0.3 + 0.6
print(a)
if a == 0.9:
  print(True)
else:
  print(False)

a = 0.3+0.6
print(round(a,3))

end_time = time.time()  # 측정완료
print("time: ", end_time - start_time)
