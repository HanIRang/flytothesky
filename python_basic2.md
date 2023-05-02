## str (문자열)

- 순서가 있는 **시퀀스 자료형**입니다.
- 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표('''str''', """str""")로 감싸는 것도 가능합니다. (삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
- 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
- 이스케이프 문자도 사용이 가능합니다.
- 리스트, 튜플도 시퀀스 자료형입니다.

s = 'paullab CEO leehojun'
s[0] # 0은 index입니다. 이렇게 호출하는 것을 indexing이라고 합니다.

type(s)

dir(s)

# 문자열의 메서드
# 'capitalize','casefold','center','count','encode',
# 'endswith','expandtabs','find','format','format_map',
# 'index','isalnum','isalpha','isascii','isdecimal','isdigit',
# 'isidentifier','islower','isnumeric','isprintable','isspace',
# 'istitle','isupper','join','ljust','lower','lstrip',
# 'maketrans','partition','removeprefix','removesuffix',
# 'replace','rfind','rindex','rjust','rpartition','rsplit',
# 'rstrip','split','splitlines','startswith','strip','swapcase',
# 'title','translate','upper','zfill'

s = 'paullab CEO leehojun'
s.lower(), s.upper() 
# 특히 사용자에게 입력을 받는 경우 lower도 많이 사용합니다.

s = 'paullab CEO leehojun'
s.find('C'), s.index('C')

# 견고한 코드란?
# 시간이 지나도 그대로 사용할 수 있고
# error가 예측 가능하게 나는 코드
# 네이버에 이미지 슬라이딩 코드
# bool(s.find('Z')) => -1은 True이기 때문에 주의가 필요합니다.
s.find('Z')

# Error가 나면 Error를 주는 것이 좋을 수 있습니다.
# Error를 안주는 언어로 JavaScript
s.index('Z')

s = 'paullab CEO leehojun'
s.find('CEO')

# 별 5개
s = 'paullab CEO leehojun'
s.count('l')

str([1, 2, 3, 4, 5])

str([1, 2, 3, 4, 5]).count(' ')

str([1, 2, 3, 4, 5]).count(',')

str([1, 2, 11, 4, 111]).count('1')

str(list(range(0, 10001))).count('8')

* https://codingdojang.com/scode/393?answer_mode=hide

str([1,2,3,4,5]).count(' ') 
# list는 콤마 다음에 공백이 없더라도 공백으로 인식해줍니다.

str([1,
     2,
     3,
     4,
     5]).count(' ')
# list는 콤마 다음에 공백이 없더라도 공백으로 인식해줍니다.

'hello'.count('')

'a'.count('')

''.count('')

'' + ''

'   hello   !  '.strip() # 공백제거 메서드

'   hello   !  '.rstrip()

'   hello   !  '.lstrip()

# 별 5개
'hello world hi'.replace(' ', '!')
'hello world hi'.replace('world', 'W@O@R@L@D').upper()

'hello world hi'.replace('world', 'W@O@R@L@D').upper().split('@')
# 반환값이 list이기 때문에 메서드 체이닝을 하려면 
# 이후로 list 메서드를 사용해야 합니다.

'hello world hi'.replace(' ', '')

data = '''  "+ +-+ -+-"  
  "++ -- +-+"  
  "++-+ -+ -"  
  "+ ++-+ -+"  '''

data.split('\n')[0].replace(' ', '').replace('"', '')

# Pythonic하지 않다!
data.split('\n')[0].replace(' ', 
                '').replace('"', 
                '')

# Pythonic하게 하려면
data.split('\n')[0]\
                .replace(' ', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')

# 제가 사용하는 기법
processed_string = data.split('\n')[0].replace(' ', '').replace('"', '')
processed_string.replace('"', '').replace('"', '')

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 79자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 39자

data = '''  "+ +-+ -+-"  
  "++ -- +-+"  
  "++-+ -+ -"  
  "+ ++-+ -+"  '''

data.split('\n')[0].replace(' ', '').replace('"', '').replace('+', '1').replace('-', '0')
ord('A'), chr(65) # ord는 문자를 가지고 숫자로 변경 chr은 숫자를 가지고 문자로 변경합니다.

숫자 = data.split('\n')[0].replace(' ', '').replace('"', '').replace('+', '1').replace('-', '0')
int(숫자, 2)
chr(int(숫자, 2))

# 별 4.5개
'paullab CEO leehojun'.split(' ') #문자열을 쪼개어 줍니다.
'paullab!CEO!leehojun'.split('!')
'paullab,CEO,leehojun'.split(',')

# 퀴즈
'010 5044 2903' # 1번
'010-5044-2903' # 2번
'010 5044-2903' # 3번

# 원하는 결과값
# ['010', '5044', '2903']
# [10, 5044, 2903] # 010은 error가 나기 때문에 10으로 저장

'010 5044 2903'.split(' ')
'010-5044-2903'.split('-')
'010 5044-2903'.replace(' ', '-').split('-')

'010 5044 2903'.split() # 공백단위가 들어가기 됩니다.

# '01050442903'.split('') # 빈 문자열을 넣지는 못합니다.

list(map(int,'010 5044 2903'.split(' ')))

int('010')

# print(010) # error

num ='010 5044-2903'.replace('-',' ').split(' ')
[int(i) for i in num] # 리스트 컴프리헨션 사용
list(map(int, '010 5044 2903'.split(' ')))

# 2개 모두 새로운 리스트를 만드는 것입니다.
# 원본을 변경시키지 않습니다.

# 이 코드 보다는
s = []
for i in '010 5044-2903'.replace('-',' ').split(' '):
    s.append(int(i))
s

# 요 코드를 추천합니다.
[int(i) for i in num]

# 지금 진도에서 과하기 때문에 
# 지금은 잊으셔도 됩니다.
# 뒤에서 상세하게 다룹니다.
def 제곱함수(x):
    return x ** 2

def 정수함수(x):
    return int(x)

list(map(제곱함수, [1, 2, 3]))
list(map(정수함수, ['1', '2', '3']))
list(map(int, ['1', '2', '3']))

list(map(int, ['010', '5044', '2903']))
list(map(int,'010 5044 2903'.split(' ')))

# 별 4.5 개
'~'.join(['hello', 'world', 'hello'])
'!'.join(['hello', 'world', 'hello'])
''.join(['hello', 'world', 'hello'])
' '.join(['hello', 'world', 'hello'])

'hello'.isalpha()

'he llo'.isalpha()

'123'.isdigit()

'12a3'.isdigit(), '12 3'.isdigit()

'12a3'.isalnum(), '12 3'.isalnum()

'안녕하세요!'.isalpha(), '안녕하세요!'.isalnum()

# 퀴즈
# 숫자를 모두 더하라!
result = 0
for i in '123abc913sldlf':
    # print(i.isdigit())
    if i.isdigit():
        result += int(i) # result = result + int(i)
result

result = 0
for i in '123abc913sldlf':
    if i.isdigit():
        result += int(i)
result

'paullab CEO leehojun'.isascii()

'paullab CEO leehojun'.rjust(30) #오른쪽 정렬
'paullab CEO leehojun'.ljust(30) #왼쪽 정렬
'paullab CEO leehojun'.center(30)#가운데 정렬

'hello'.zfill(20) # 데이터의 빈 공간을 0으로 채워줍니다.

'1001'.zfill(5)
'hello'.zfill(10).replace('0', '-')

규칙테이블 = str.maketrans({'\n':'', '\t':''})
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)

'paullab \n\n\n CEO \t\t\t leehojun'.replace('\n', '').replace('\t', '')

규칙테이블 = str.maketrans('\n\t', '  ') # 똑같은 길이를 가지고 있어야 함
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)

규칙테이블 = str.maketrans('le','12')
'paullab CEO leehojun'.translate(규칙테이블) #어떤 규칙을 정하는것

## pep

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa => 80자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 => 40자면 한글 넘어갑니다.
# line에 딱 맞춰 들어간 것을 볼 수 있습니다. 
# 강제사항은 아닙니다.
# 띄어쓰기 4번도 강제사항은 아닙니다.
# pep8, pep20에 기술되어 있습니다. => pep(Python Enhancement Proposal)란 무엇인가요? 8이란 무엇인가요?
# pep8 : Style Guide for Python Code (https://peps.python.org/pep-0008/)
# pep20 : The Zen of Python(https://peps.python.org/pep-0020/) #이스터애그로 숨겨져 있습니다.
# https://peps.python.org/

## cpython

* 공식홈페이지에서 다운로드 받는 것이 cpython입니다.
* https://github.com/python/cpython
* list를 구현한 코드 : https://github.com/python/cpython/blob/main/Objects/listobject.c

## 인덱싱과 슬라이싱

name = 'Guido van Rossum'
print(name[0])
print(name[1])
print(name[2])

# s[start:stop:step]
s = 'paullab CEO leehojun'
s[5:]
s[:5]
s[3:10]
s[:]
s[0:20:2]

# 자주 사용되는 코드
s = 'paullab CEO leehojun!'
s[:] # string에서는 많이 사용하지 않지만 list에서 많이 사용합니다.
s[:-1] # 마지막 요소만 제외하고 다 슬라이싱 합니다.

test = [1, 2, 3, 4]
test2 = test
test2[0] = 1000
test, test2

test = [1, 2, 3, 4]
test2 = test[:] # 새로운 리스트를 만들어서 test2에게 줍니다.
test2[0] = 1000
test, test2

## 문자열의 연산

s = 'hello world'
dir(s)
s + s
s * 3

## 형변환

* 형변환 : type을 변경하는 것입니다.

x = int(input())
x + x # but 알파벳 입력하면 error!

x = input()
if x.isdigit():
    x = int(x) # but 알파벳 입력하면 error!
x + x

# int('abc') # error
int(10.1) # 버림
int('10') # 형변환 가능
# int('10.1') # 형변환 불가능

float('10') # 형변환 가능
float('10.1') # 형변환 가능

int('10a') # 되는 언어가 있어서 보여드린 것입니다.
# Python에서는 허용하지 않습니다.

def hello():
    pass

str(type)
str(hello)

str('123')
str(True)
str(None)
str([1, 2, 3])
str({1, 2, 3})
str({'one':1, 'two':2})

# 별 5개
# bool 형으로 형변환 하는 것
if True:
    print('hi')

if 'hello':
    print('hi')

# 정말 많이 사용하는 코드
l = [1, 2, 3]
while l:
    print(l.pop())

bool('') # 빈 문자열을 제외하고 모두 True
bool('a')
bool('False') # 문자열 False이기 때문에 True
bool(0) # 0을 제외하고 모두 True
bool(-1)
bool(100)
bool(None) # None은 비어있음을 명시해주는 키워드, False
bool([]) # 컨벤션 자료형은 비어있으면 False입니다.
bool({})

# list로 형변환
s = '10'
l = list(s)
l

s = 'leehojun'
l = list(s)
l

# tuple로 형변환
s = 'leehojun'
l = tuple(s)
l

# dict
# name = 'leehojun' # error
# dict(name)

s = [('name','leehojun'), ('age',10)]
d = dict(s)
d

# set(집합)으로 형변환
name = 'leehojun'
set(name)

len('hello world') # __len__
len([1, 2, 3, 4])

## 문제풀이

# 1번의 오답(아래처럼 변수를 선언하지 않도록 주의해주세요.)

#1번
# print = 100

#2번
# 10 = a

#4번
# 100k = 10000

# 2번
user_input = input('문자를 입력해주세요!')
print(user_input * 2)

print(input('문자를 입력해주세요!') * 2)

# 3번
num = 1234567890
list(str(num))
list(str(num))[3]

## 산술연산

a = 10
b = 3

print(f'10 + 3 == {a + b}')
print(f'10 - 3 == {a - b}')
print(f'10 / 3 == {a / b}')
print(f'10 // 3 == {a // b}') # 몫만 나옵니다.(정수만요!)
print(f'10 * 3 == {a * b}')
print(f'10 ** 3 == {a ** b}')
print(f'10 % 3 == {a % b}') # 나머지

# 연산자 우선순위는 and, or, 4칙연산, 제곱 정도만 아셔도 
# 코딩하는데 큰 무리가 없습니다.
# (모르시면 읽는데 어려움이 생기기도 합니다.)

print(3 ** 2 * 3)
print(3 * 3 ** 2) # 왜 81이 아니지?
# 곱하기 보다 제곱이 우선순위가 더 높습니다.
print(3 + 3 * 2) # 3 + 3부터 먼저 하지 않습니다.

a = 10
b = 3

print(f'10 > 3 == {a > b}')
print(f'10 >= 3 == {a >= b}')
print(f'10 < 3 == {a < b}')
print(f'10 <= 3 == {a <= b}')
print(f'10 == 3 == {a == b}')
print(f'10 != 3 == {a != b}')

## 논리연산

# and 는 곱
# or 는 합
# not은 반대
# True 1
# False 0
# 중요한 포인트는 저렇게 했을 때 언제 True가 되는지 정리하는 것

print(True and False)
print(True or False)
print(True or True)

if True and False:
    print('hello')

if 10 > 3 and 8 % 3 == 0:
    print('hello')

# and는 언제 True가 되나요?
# 모두 True일 때만 True
# or는 언제 True가 되나요?
# 둘 중에 하나라도 참이라면 True

# https://codingdojang.com/scode/350?answer_mode=hide
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

result = 0
for i in range(101):
    if i % 3 == 0:
        result += i # result = result + i
    if i % 5 == 0:
        result += i
    if i % 15 == 0:
        result -= i
print(result)

result = 0
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        result += i
result

not True

not False

# python 입장에서 보는 코드
# False and ????? => 물음표에 무엇이 나오든 False
# 그래서 Python도 저 물음표를 보지 않습니다.
def solution():
    1/0

if False and solution():
    print('hello')

# True or ?????  => 물음표에 무엇이 나오든 True
# 그래서 Python도 저 물음표를 보지 않습니다.
def solution():
    1/0

if True or solution():
    print('hello')

# 단락 평가(컴퓨터가 어디까지 보는지 판단해서 활용)
username = '' # 사용자가 아무것도 입력하지 않았을 경우
username = username or 'licat'
username

username = 'leehojun' # 사용자가 이름을 입력했을 경우
username = username or 'licat'
username

# and와 or의 우선순위(and가 더 높습니다.)
for i in range(21):
    if i % 3 == 0 and i % 5 == 0 or i % 2 == 0:
        print(i)

for i in range(21):
    if (i % 3 == 0 and i % 5 == 0) or i % 2 == 0:
        print(i)

# 아래는 출력되는 값이 다릅니다! 우선순위가 낮은 or가 먼저 나왔기 때문입니다.
# 결론 : 헷갈리시면 괄호를 사용해주세요!
for i in range(21):
    if (i % 3 == 0 or i % 5 == 0) and i % 2 == 0:
        print(i)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0 and i % 2 == 0:
        print(i)

## 비트연산 (중요도 하)

# and(곱하기)
# 1001 == 9
# 0010 == 2
# ----
# 0000

9 & 2

# and(곱하기)
# 1001 == 9
# 1000 == 8
# ----
# 1000

9 & 8

# or(더하기, 대신 자리올림이 되진 않습니다.)
# 1001 == 9
# 0011 == 3
# ----
# 1011

9 | 3

# xor(같을 경우 0, 다를경우 1)
# 1001 == 9
# 0011 == 3
# ----
# 1010
9 ^ 3

~9 # 2보수를 취하는 것입니다.(9에게 +1한 다음에 -를 취하시면 됩니다.)
~-7 # 2보수를 취하는 것입니다.(7에게 +1한 다음에 -를 취하시면 됩니다.)

3 << 2 
# 3을 2진수로 표현하면 11인데 2칸을 왼쪽으로 미는 것입니다.
# 1100

7 >> 2

## 디스코드 단축키

* `:ok`

## 할당연산

# a = 10
# a = a + 10
a = + 10 # 이렇게 a를 지우면 양수를 표현하는 10만 남아요.
a

a = 10
a += 10 # a = a + 10
a

a = 10
a //= 10 # 산술연산 모두 됩니다.
a

# Python에서 특이하게 ++a, ++b, a++, b++가 없습니다.

## 식별연산자

# 앞으로 아래 2개를 활용해서 Python에 
# 컨벤션 자료형이 어떻게 구성이되는지 확인해볼겁니다.
# id()
# is

a = 256
b = 256
a is b

a = 999
b = 999
a is b

a = [1, 2, 3]
b = [1, 2, 3]
a is b

a[0] = 100
a, b

a = [1, 2, 3]
b = [1, 2, 3]
a == b # Python에 등호는 type과 value를 봅니다.

# is는 주소값을 비교합니다.
id(a) == id(b) # 이게 False면 is도 False입니다.

a = [1, 2, 3]
b = [1, 2, 3]

id(a) #5152

id(b) #9280

a == b # 값이 같은 것과 메모리에 같은 공간에 저장되어 있다는 얘기는 다른 얘기입니다!

## not의 위치

a = 10
b = 100
a is not b
# a not is b # error

a = 10
b = [10, 20, 30]
a not in b

## 멤버연산

'a' in 'helalo world'
'a' in 'hello world'
'a' in ['a', 'b']
'a' in {'a':10, 'b':20}
# 10 in {'a':10, 'b':20} # dict안에있는 value값이 있는지 확인하고 싶으면
10 in {'a':10, 'b':20}.values()
10 in {10, 20, 30}

'a' not in ['aa', 'bb']

10 in [10, 20, 30]
[10] in [10, 20, 30]
[10] in [[10], 20, 30]
[10, 20] in [10, 20, 30]
[10, 20] in [[10, 20], 30]
set([10, 20]).issubset(set([10, 20, 30]))
{10, 20}.issubset({10, 20, 30, 40})

## 연습문제

#1번
a = 100
print((a > 100) and (a < 200))
print((a > 100) or (a < 200))
print((a >= 100) and (a <= 200))
print((a >= 100) or (a <= 200))

#2번
b = 25
(b % 2 == 0) and (b % 5 == 0)

#3번
c = 1000
c / 100
c // 100

#4번
# 그리디 알고리즘(욕심쟁이 알고리즘)
남은금액 = int(input())

오천원 = 남은금액 // 5000
남은금액 = 남은금액 % 5000

천원 = 남은금액 // 1000
남은금액 = 남은금액 % 1000

오백원 = 남은금액 // 500
남은금액 = 남은금액 % 500

백원 = 남은금액 // 100
남은금액 = 남은금액 % 100

print(오천원, 천원, 오백원, 백원)
