import re

def solution(numbers):
    s = ''
    d = {
        'one':   '1',
        'two':   '2',
        'three': '3',
        'four':  '4',
        'five':  '5',
        'six':   '6',
        'seven': '7',
        'eight': '8',
        'nine':  '9',
        'zero':  '0',
    }
    for i in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)', numbers):
        s += d[i]
    return int(s)





