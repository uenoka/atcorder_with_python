# abc176_d.py

import sys
sys.setrecursionlimit(500000)

def printseen():
    for i in seen:
        print(i)

def canGo(nh,nw,i,j):
    # 自身のマスならスキップ
    if i==0 and j==0:return False
    # for 迷路
    # 斜めには動けない（迷路）
    if (i==1 or i==-1) and (j==1 or j==-1) : return False
    # 範囲外
    if nh < 0 or nw < 0 or nh >= H or nw >= W : return False
    # すでに見ている
    if seen[nh][nw] : return False
    # 壁
    if glid[nh][nw] == '#' : return False
    # すべての条件を超えたらOK
    return True

def dsf(h,w):
    seen[h][w] =True
    for i in range(4):
        nh = h + dx[i]
        nw = w + dy[i]
        if canGo(nh,nw,dx[i],dy[i]):
            dsf(nh,nw)


H,W = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
glid = [0]*H
start = list(map(int,input().split()))
goal = list(map(int,input().split()))

seen = [[False] * W for i in range(H)]

for i in range(H):
    glid[i] = list(input())

for i in range(H):
    for j in range(W):
        if glid[i][j] == 's': start = [i,j]
        if glid[i][j] == 'g': goal = [i,j]

def resetStart():
    pass

while not seen[goal[0],goal[1]]:
    dsf(start[0],start[1])
    resetStart()

if seen[goal[0]][goal[1]]:
    print('Yes')
else:
    print('No')