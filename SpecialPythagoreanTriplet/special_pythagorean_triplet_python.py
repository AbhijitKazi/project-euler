def pythagoreanTriplet(n):
    for i in range(1, int(n/3) + 1):
        for j in range(1, int(n/2) + 1):
            k = n-i-j
            if (i*i + j*j == k*k):
                print(i,", ",j,", ",k)
                prod = i*j*k
                print(prod)
                return
    print("No Triplet")
    
    
n = 1000;
pythagoreanTriplet(n);

