import time

start_time = time.time()

names_1_f = open("names_1.txt", "r")
names_1 = names_1_f.read().split("\n")  # List containing 10000 names
names_1_f.close()

names_2_f = open("names_2.txt", "r")
names_2 = names_2_f.read().split("\n")  # List containing 10000 names
names_2_f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# BASK IN THE GLORY OF THIS FASTER CODE
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
