#time module for calculating time
import time,math
from past.builtins import xrange

#Time at the start of execution
start =time.time()

#Sieve of Eratosthenes
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False

	#Using the sieve algorithm
	for i in xrange(2,int(math.sqrt(n)+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index += i
	
	#List to store the prime numbers
	prime = []

	#adding prime to the list
	for i in xrange(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

#Printing the result
print(sum(sieve(2000000)))

#Time at the end of execution
end_time = time.time()

#Printing the total time 
print(end_time  - start)