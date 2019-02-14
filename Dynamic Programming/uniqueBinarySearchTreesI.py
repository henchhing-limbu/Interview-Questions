# takes input integers
# retuns number of structurally unique BSTs that stores values 1 ... n

def numTrees(n):
	# n+1 because we take into account zero as well
	counts = [-1]*n+1
	counts[0] = counts[1] = 1
	for i in range(2, n+1):
		count = 0
		# using subproblem to solve the present problem
		for j in range(1, i+1):
			count += counts[j-1] * counts[i-j]
		counts[i] = count
	return counts[-1]

