'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.


Example
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

'''
def sum():
	array1 = []
	print("Start programme(enter 0: exit) : ")
	while True:
		a = int(input())
		if a == 0:
			break
		array1.append(a)
	sum = int(input("input sum: "));
	for i in range(len(array1)):
		for j in range(len(array1)):
			if i!=j:
				if array1[i]+array1[j] == sum:
					return i,j


def main():
	a,b = sum()
	print(a,b)
main()