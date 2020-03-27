import time

from bst import BinarySearchTree

start_time = time.time()

names_1_f = open("names_1.txt", "r")
names_1 = names_1_f.read().split("\n")  # List containing 10000 names
names_1_f.close()

names_2_f = open("names_2.txt", "r")
names_2 = names_2_f.read().split("\n")  # List containing 10000 names
names_2_f.close()

duplicates = []  # Return the list of duplicates in this data structure

# ORIGINAL: ~4.8 seconds
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# FIRST PASS SOLUTION: ~0.86 seconds
# BASK IN THE GLORY OF THIS FASTER CODE
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# BST SOLUTION: 0.18 seconds
# Fill tree A
bst_a = BinarySearchTree(names_1[0])

for name in range(1, len(names_1)):
    bst_a.insert(names_1[name])

# Fill tree B
bst_b = BinarySearchTree(names_2[0])

for name in range(1, len(names_2)):
    bst_b.insert(names_2[name])

# Create func to apply to each node in tree A
find_duplicates = lambda name: duplicates.append(name) if bst_b.contains(name) else None

# YEET
bst_a.for_each(find_duplicates)

end_time = time.time()
print("BST SOLUTION\n")
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n")
print(f"runtime: {end_time - start_time} seconds\n")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# RUNTIME: 0.003969669342041016 seconds
# O(n)

start_time = time.time()

# Clear duplicates array
duplicates.clear()

# Setup hash table
names_table = {}

# Add names of first file
for i in range(0, len(names_1)):
    names_table[names_1[i]] = i

# Find names from second file that are in hash table
for name in names_2:
    if name in names_table:
        duplicates.append(name)

end_time = time.time()
print("HASH TABLE SOLUTION\n")
print(f"runtime: {end_time - start_time} seconds")
