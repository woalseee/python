n,m = map(int, input().split())

arr = [input() for _ in range(n)]

w_board = [
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW'
]

b_board = [
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB'
]

def check (i,j):
    result_w = 0
    result_b = 0
    
    for di in range(8):
        for dj in range(8):
            ni, nj = i+di ,j+dj
            if arr[ni][nj] != w_board[di][dj]:
                result_w += 1 
            if arr[ni][nj] != b_board[di][dj]:
                result_b += 1
    return min(result_b, result_w)
                
result = 1000000000
for i in range(n-7):
    for j in range(m-7):
        result = min(result, check(i,j))
        
print(result)