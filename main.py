import random

# arrays & strings
arr = [0, 1, 2, 3, 4]
print("Max value: " + str(max(arr)))
print("size of list: " + str(len(arr)))
arr.append(5)
arr.pop(0)  # uses the index
# Note: The list's remove() method only removes the first occurrence of the specified value.
arr.remove(2)  # uses the element as argument, not index
print(arr)

# Random
min_val = 1
max_val = 100
# random.randint has the range be inclusive. So if range is 1-3, possible random
# numbers would be 1, 2, and 3
print("Random int within range " + str(min_val) + "-" + str(max_val) + ": " +
      str(random.randint(min_val, max_val)))

# round
num = 4.7
print(round(num))
print(num // 2)  # integer division
print(num / 2)

# for loops
# for x in range(start, stop, step):
# use end=" " to not print a new line
for x in range(10):
    print(x, end=" ")
print()

for x in range(1, 10):
    print(x, end=" ")
print()

for x in range(1, 10, 2):
    print(x, end=" ")
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x, end=" ")
print()

for x in range(1, 10):
    print(x % 3, end=" ")
print()

# enumerate
lst = ["car", "boat", "plane"]
obj = enumerate(lst)
print(list(obj))

for i, val in enumerate(lst):
    print(i, end=" ")
    print(val, end=" ")
print()


# printing index of key
def search(array, key):
    for index, item in enumerate(array):
        if item == key:
            print("Found at index: " + str(index))
            break


nums = [1, 45, 6, 87, 32, 67, 8, 9, 3]
search(nums, 32)

# swap with one line, no use of a temp
x = 2
y = 5
x, y = y, x
print("x:" + str(x))
print("y:" + str(y) + '\n')


# generators
# yield will pause and store the current state of the function, and start back up from where it left off
# so you can stop the function and then resume
def gen(my_lst):
    for j in my_lst:
        yield j * 2


# using the generator in the for loop because its an iterable
for num in gen([1, 2, 3]):
    num += 1
    print(num, end=" ")
print()
myNums = [1, 2, 3]
for i in gen(myNums):
    i += 1

print(myNums, end=" ")
print()

#