import sys
ans = 100
print("당신의 인생 점수는 " + str(ans))
print("당신은 ",3000,"만큼 열심히 하면 다 해결됩니다.")
print(f"당신은 매일 주식으로 {ans}만원만큼 벌 것입니다 오늘부터")

data = list(sys.stdin.readline().split()) #['5', '6', '7', '8']
print(data)

#elif
score=85
if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
else :
    print("학점 : F")
print("학점 협상은 없습니다")

'''
n = int(input())
# data = input().split() ['1', '2', '3', '4', '5', '6']
a,b,c = list(map(int,input().split()))

print(n)
print(a,b,c)
'''