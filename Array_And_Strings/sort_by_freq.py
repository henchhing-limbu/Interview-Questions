# Given a list of numbers
# You want to sort the number based on frequency
# if a number has same frequency, just order by their time of occurence


# TODO: Get it done
def sortByFreq(a):
	num_count_map = {}
	for i, num in enumerate(a):
		if num in num_count_map:
			count, idx, _ = num_count_map[num]
			num_count_map[num] = (count+1, idx, num)
		else:
			num_count_map[num] = (1, i, num)

	values = [value for _, value in num_count_map.items()]
	_sort_helper(values, 0, len(values)-1)

	i = 0
	for count, _, num in values:
		while count != 0:
			a[i] = num
			i += 1
			count -= 1

def _sort_helper(a, low, high):
	if low >= high:
		return
	i = low - 1
	pivot_count, pivot_idx, _ = a[high]
	j = low
	while j <= high:
		count, idx, _ = a[j]
		if count > pivot_count or (count == pivot_count and idx < pivot_idx):
			i ++ 1
			a[i], a[j] = a[j], a[i]
		j += 1
	a[i+1], a[high] = a[high], a[i+1]
	_sort_helper(a, low, i)
	_sort_helper(a, i+1, low)
	
		

arr = [2, 5, 2, 8, 5, 6, 8, 8]	
sortByFreq(arr)
assert arr == [8, 8, 8, 2, 2, 5, 5, 6]
