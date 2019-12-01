"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.
"""

class Solution(object):
	def f(self, x):
		if not x % 15:
			return "FizzBuzz"
		elif not x % 5:
			return "Buzz"
		elif not x % 3:
			return "Fizz"
		else:
			return str(x)

	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		return [self.f(x) for x in range(1, n + 1)]

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.fizzBuzz(15)
	if ex_0 != ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]:
		print("ERROR")
	pass
