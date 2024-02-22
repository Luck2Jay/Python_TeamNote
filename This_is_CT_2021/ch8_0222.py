for i in range(10):
    print(i)

a = 15
if 10<a<20:
    print("해당")

a = [1,2,3,4,5,5,5]
remove_set = {3,5}
result = {i for i in a if i not in remove_set}
print(result)

score = 85
if score>=80:result="success"
print(result)

result = "success" if score >= 80 else "fail"
print(result)

arr = [1,2,3,4,5]
for x in arr:
    print(x)

a = 50

if a>=30:
   pass
else:
    print("a < 30")


a=15
if a <= 20 and a >=0:
    print("Yes")