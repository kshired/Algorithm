import sys
import re
import requests

DEFAULT_URL = 'https://acmicpc.net/problem/'

if len(sys.argv) > 1:
    NUMBER = sys.argv[1]
else:
    NUMBER = int(input("문제 번호를 입력해주세요 : "))

URL = DEFAULT_URL+NUMBER

resp = requests.get(URL)
title = re.search('(?<=<title>).+?(?=</title>)', resp.text, re.DOTALL).group().strip().split(':')[1].strip()

f = open('./baekjoon/'+NUMBER+'.py','w')
f.write(f'''# {URL}
# {title}

import sys
input = lambda : sys.stdin.readline().rstrip()
input_multiple_int = lambda : map(int,input().split())

''')
f.close()
print(f'{NUMBER}번 문제의 코드가 생성되었습니다.')