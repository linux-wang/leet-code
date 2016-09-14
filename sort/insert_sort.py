# -*- coding:utf-8 -*- 

def insert_sort(array): 
	for i in range(1, len(array)): 
		key = array[i] 
		j = i - 1 
		while j >= 0 and key < array[j]: 
			array[j + 1] = array[j] 
			j-=1 

		array[j + 1] = key 
	return array
mylist0 = [12, 11, 13, 1, 2, 4, 3]  
print insert_sort(mylist0)
