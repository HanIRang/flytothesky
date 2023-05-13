1.
원주율 = 3.141592

int(원주율)

2. b

3.
my_name = input()
print(f'안녕하세요. {my_name}입니다.')

4. c

5.
num = int(input())

def divisor(num):
    data = []

    for i in range(1, num + 1):
        if num % i == 0:
            data.append(i)
    return data

divisor(num)

6.
def solution(l, a):
    print(l.count(a))

solution(['a', 'b', 'c', 'a', 'a'], 'a')

7.**중요
def solution(l):
    return sorted(l, key=lambda x:x[1], reverse=True)

solution([[10, 5], [20, 3], [30, 4], [40, 1]]) 

8.
def solution(l):
    return list(map(lambda x: x[0]-x[1], l))

solution([[10, 5], [20, 3], [30, 4], [40, 1]])


9.
def solution(s):
    return sum([int(i) for i in s])

solution('11123')


or

s=0
for i in '11123':
    s += int(i)
s

10.def solution(s):
    return s.replace('!', '').replace(' ', '')

solution('!hello!wor     ld!     ') 
