import time

start_time = time.time()  #측정시작

#프로그램 소스코드
"""
# n x m 크기의 2차원 리스트 초기화
n = 3 
m = 4
li = [['a'] * m for _ in range(n)]
print(li)

#reverse
a=[1,2,3,4,5,6,3,3,3,5,5,5,5]
print(a)
a.sort()
a.reverse()
print(a)
a.insert(2,'c')
print(a)
a.append(12)
print(a)

a.remove('c')
print(a)
"""

#특정 값의 원소를 모두 제거
a=[1,2,3,4,5,6,3,3,3,5,5,5,5]
print(a)
remove_set={3,5} #리스트가 아니라 집합
result=[i for i in a if i not in remove_set]
print(result)

'''
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
'''

'''
#수 자료형 연산
a=7
b=3
#몫 연산자
print(a//b)

#거듭제곱
print(a**b)
'''

"""
#List
a = [1,2,3,4,5]
print(a)
print(a[1:3])
li = list()
print(li) 
print()
n=10
li=[10] * n
print(li)
print()
#홀수
li=[i for i in range(20) if i%2 ==1]
print(li)
#1~9 제곱
li=[i * i for i in range(1,10)]
print(li)
#1~9 거듭제곱
li=[i**i for i in range(1,10)]
print(li)
"""
end_time = time.time()  # 측정완료
print("time: ", end_time - start_time)
