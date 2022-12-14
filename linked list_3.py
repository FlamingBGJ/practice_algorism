# -*- coding: utf-8 -*-
"""연결리스트3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tR1tHefU5UURiKD8ElnoqoO6F7lo1Y2F
"""

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

## 변수
memory = []
head, current, pre = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# 첫 노드 만들기
node = Node()
node.data = dataAry[0]
head = node
memory.append(node)

# 두번째 이후 노드 만들기
for data in dataAry[1:] : # ['정연', '쯔위',....
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)