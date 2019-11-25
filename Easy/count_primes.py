"""
Count the number of prime numbers less than a non-negative number, n.
"""

class Solution(object):
	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <= 1:
			return 0
		factor = 2
		primes = [True for i in range(n)]
		primes[0] = False
		primes[1] = False
		while factor * factor < n:
			if primes[factor * factor]:
				if primes[factor]:
					cofactor = factor * 2
					while cofactor < n:
						primes[cofactor] = False
						cofactor += factor
			factor += 1
		primes = [p for p in primes if p]	
		return len(primes)

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.countPrimes(10)
	if ex_0 != 4:
		print("ERROR")
	# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
	ex_1 = s.countPrimes(100)
	if ex_1 != 25:
		print("ERROR")
	ex_2 = s.countPrimes(5)
	if ex_2 != 2:
		print("ERROR")
	ex_3 = s.countPrimes(2)
	if ex_3 != 0:
		print("ERROR")
	pass
