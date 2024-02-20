#Set
data=set([1,1,2,3,4,4,5,6,])
print(data)
data={1,1,2,2,4,4,5,5}
print(data)

a = set([1,2,3,4,5])
b = {3,5,6,7,8}

print(a|b)
print(a&b)
print(a-b)

a.add(8)
print(a)
a.update([7,9])
print(a)
a.remove(1)
print(a)

'''
#dictionary
data={
    '사과':'apple',
    '바나나':'banana',
    '코코넛':'coconut'
}

print(data)
print()
print(data.keys())
print(list(data.keys()))
print()
print(data.values())
print(list(data.values()))
'''

'''
data = 'hello_world'
print(data)

data = "Don't you 'know' \"python\""
print(data)

print('a'+' '+'b')

a="abcdefg"

#Tuple
a=(1,2,3,4,5)
print(a)
print(a[3])
'''
