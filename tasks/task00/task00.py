k = int(input())

n1 = k % 10
n2 = int((k - n1) % 100 / 10)
n3 = int((k - n2*10 - n1) % 1000 / 100)
n4 = int((k - n3*100 - n2*10 - n1) % 10000 / 1000)

for i in range(1,int((k+1)**(1/3))):
    if n1**i + n2**i + n3**i + n4**i == k:
        print(i)