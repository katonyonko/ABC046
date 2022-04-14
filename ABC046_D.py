from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="046"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc062_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  s=input()
  ans=0
  for i in range(len(s)):
    if i%2==0 and s[i]=='p': ans-=1
    elif i%2==1 and s[i]=='g': ans+=1
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])