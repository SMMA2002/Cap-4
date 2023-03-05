import Array
maxSize = 10 # Max size of the array
arr = Array.Array(maxSize) # Create an array object

arr.insert(90) # Insert 10 items
arr.insert(98)
arr.insert(4)
arr.insert(9)
arr.insert(55)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert(1)
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()

print("Get max num", arr.getMaxNum())
arr.traverse()

print("Delete max num", arr.deleteMaxNum())
arr.traverse()

print("Delete duplicated num", arr.removeDupes())
arr.traverse()

print("Array ordenado mayor a menor:")
maxSize2 = 10
arr2 = Array.Array(maxSize2)

n = len(arr)-1
while n > 0:
    p = arr.getMaxNum()
    arr2.insert(p)
    arr.delete(p)
    n = n - 1
arr2.traverse()