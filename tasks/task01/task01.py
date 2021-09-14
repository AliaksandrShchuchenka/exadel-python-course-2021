# Function to check if number is narcissistic
def checkN(k):
    n1 = k % 10
    n2 = int((k - n1) % 100 / 10)
    n3 = int((k - n2*10 - n1) % 1000 / 100)
    n4 = int((k - n3*100 - n2*10 - n1) % 10000 / 1000)

    for q in range(1, k+1):
        if n1**q + n2**q + n3**q + n4**q == k:
            print('Narciss number:', k, 'Pow:', q)

# Main
for i in range(1, 1001):
    checkN(i)
