from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="046"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc062_a".format(times, problem)) as res:
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
  N=int(input())
  t,a=1,1
  for i in range(N):
    T,A=map(int,input().split())
    tmp=max((t-1)//T+1,(a-1)//A+1)
    t,a=tmp*T,tmp*A
  print(t+a)
  """ここから上にコードを記述"""

  print(test_case[__+1])