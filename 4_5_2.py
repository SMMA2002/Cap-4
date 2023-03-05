import random

# Create a PriorityQueue object
pq = PriorityQueue()

# Insert some elements with random priorities
for i in range(10):
    item = random.randint(1, 100)
    pq.insert(item)
    print(f"Inserted {item}: {pq}")

# Remove some elements with highest priorities
for i in range(3):
    max_item = pq.remove()
    print(f"Removed {max_item}: {pq}")

# Peek at the frontmost element
print(f"Frontmost element: {pq.peek()}")

# Insert some more elements
pq.insert(200)
pq.insert(50)
print(f"Inserted 200 and 50: {pq}")

# Remove all remaining elements
while not pq.isEmpty():
    max_item = pq.remove()
    print(f"Removed {max_item}: {pq}")
