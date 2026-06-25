#---------------------Numpy Arithmatic-------------------------------------
# scalar arithmatic

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr + 2)
print(arr - 2)
print(arr * 2)
print(arr / 2)
print(arr ** 2) # 2**2 = 2 * 2 * 2 = 8

# vectorized math functions

print(np.sqrt(arr))

arr2 = np.array([1.4,2.2,3.7,4.2,5.5,6.6,7.4,8.9,9.8])

print(np.round(arr2))
print(np.floor(arr2))
print(np.ceil(arr2))


# Element-wise arithmatic

arr3 = np.array([1,2,3,4,5,6,7,8,9])
arr4 = np.array([11,12,13,14,15,16,17,18,19])

print(arr3+arr4)
print(arr3-arr4)
print(arr3*arr4)
print(arr3/arr4)

# Comparison operators

marks = np.array([91,72,33,44,75,46,78,81,90])

print(marks >=50)
print(marks < 50)
marks[marks < 40 ] = 0
marks[0] = 44
print(marks)
