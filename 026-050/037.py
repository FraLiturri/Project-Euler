import numpy as np # Status: done ✅ (takes around 40 sec, could be improved...)

sum = 0
counter = 0


def prime_checker(n):
    isPrime = True
    for i in range(2, int(np.sqrt(n)) + 1):
        r = n % i
        if r == 0:
            isPrime = False
    return isPrime


def truncable_checker(n):
    while n > 22: #23 is the firs one to be LT and RT; 
        global sum
        global counter
        t1 = str(n)
        t2 = str(n)
        isPrime = True
        isRT = True
        aux_bool = prime_checker(n)
        if int(str(n)[0]) == 1 or int(str(n)[len(str(n)) - 1]) == 1:
            isPrime = False
        else:
            if aux_bool:
                while len(t1) > 1:
                    t1 = str(t1)[:-1]  # removing from right;
                    if not prime_checker(int(t1)):
                        isRT = False

            if isRT and aux_bool:
                while len(t2) > 1:
                    t2 = str(t2)[1:]  # removing from left;
                    if not prime_checker(int(t2)):
                        isPrime = False
            else:
                isPrime = False

        if isPrime:
            counter += 1
            sum += n
            print(n)
        n = n - 1


truncable_checker(8*10**5)
print("The total sum is:", sum)
