# agc024_a.py
'''
操作の周期が K%2 == 0, K%2 == 1 で分けられる
A,B,Cの係数を[自,他,他]で表すと
0 : [1,0,0]
1 : [0,1,1]
2 : [2,1,1]    -> [1,0,0]+1
3 : [2,3,3]    -> [0,1,1]+2
4 : [6,5,5]    -> [2,1,1]+4
5 : [10,11,11] -> [2,3,3]+8
...
-> 解説AC。差を考えると、結局のところ A-B か B-A に落ち着く。
'''

A, B, C, K = map(int,input().split())
if K%2==0:
    print(A-B)
else:
    print(B-A)