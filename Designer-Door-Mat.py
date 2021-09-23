N = int(input('input an odd number: '))
while N % 2 == 0:
    N = int(input('Wrong number. Input an odd number: '))
    
M = N * 3
print(f'{N} {M}')

a = '.|.'
b = 'WELCOME'

for i in range(N//2): 
    print((a * (2*i+1)).center(M,'-'))
    
print(b.center(M,'-'))

for i in range(N//2-1,-1,-1): 
    print((a * (2*i+1)).center(M,'-'))