# -*- coding: utf-8 -*-
"""단순연결리스트1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y7tfhN1BYK9_LcwjPUUxiESl-JFSGlND
"""

## 함수 선언부


## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']


## 메인 코드부
print(katok)

# 데이터 추가(모모가 톡1회)
katok.append(None)
katok[5] = '모모'
print(katok)

# 데이터 삽입(미나 톡40회)
# 1단계
katok.append(None)
# 2단계
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계
katok[3] = '미나'
print(katok)

# 데이터 삭제(사나가 톡 차단)
# 1단계
katok[4] = None
# 2단계
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
# 3단계
del(katok[6])
print(katok)