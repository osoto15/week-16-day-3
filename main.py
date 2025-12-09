# Festival Inventory Disaster – Real‑World Python Collections Challenge
# Scenario
# You are hired as the Data Assistant for the Chicago Fall Music & Food Festival.
# The festival opens in 3 hours, but the digital system has scrambled the inventory lists, vendor data, and safety rules. Your job is to fix the data using Python lists, sets, and tuples.
# If you fail, the festival cannot legally open.

# Starting Data
foods = ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"],
stages = ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley"),
restricted = ["glass bottles", "weapons", "alcohol", "alcohol"],
attendance = [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]

# # Task 1 — Clean the Food Vendor List
#     # 1. Remove duplicates while keeping only the first occurrence.
# unique_list = list(set(foods))
# print(unique_list)

#     # 2. Add "ramen" and "fried rice".
# foods += ["ramen"]
# print(foods)
# foods += ["fried rice"]
# print(foods)
#     # 3. Insert "smoothies" at index 2.
# foods [1:1]+= ["smoothies"]

# print(foods)
#     # 4. Sort the list alphabetically.
# foods.sort()

#     # 5. Print the final vendor list.
# print(foods)
# #Task 1.5 
#     # combine all the list into a nested list called festival_data
# all_lists= [
# ["pizza", "tacos", "bbq", "tacos", "sushi", "corn", "bbq", "ice cream"],
# ("Main Stage", "Hip-Hop Zone", "Jazz Corner", "Indie Alley"),
# {"glass bottles", "weapons", "alcohol", "alcohol"},
# [120, 130, 125, 145, 150, 148, 155, 160, 158, 162]]
#     #print out the new nested list(use a for loop to print each item on a new line)
# for row in all_lists:
#     for all_lists in row:
#         print(all_lists, end=" ")
#     print()

# Task 2 — Stage Map
    # 1. Print the second stage.
print(all_lists[1][2]) 
    # 2. Print the last two stages.

    # 3. Convert the tuple into a list and add "Rock Arena".
    # 4. Convert it back into a tuple.
    # 5. Print the updated tuple.


# Task 3 — Restricted Items
    # 1. Add "fireworks".
restricted += ["fireworks"]
print(restricted)
    # 2. Try adding "weapons" again.
    # 3. Remove "alcohol".
    # 4. Check if "glass bottles" is still restricted.
    # 5. Print the final restricted set.


# Task 4 — Attendance Analysis
    # 1. Print the first three hours.
    # 2. Print the last hour.
    # 3. Print every 2nd hour.
    # 4. Remove the 5th hour using pop().
    # 5. Add five projected values using extend(range(...)).
    # 6. Delete every 3rd value using del attendance[::3].
    # 7. Print the length and cleaned list.
# Task 5 — Festival Master List
    # 1. Convert vendors, restricted set, and stages into lists.
    # 2. Combine everything into festival_data.
    # 3. Print: total items, first 10, last 10.
    # 4. Remove duplicates.
    # 5. Print final cleaned festival_data.

# Extension
# Write a function festival_search(item) that returns True/False if item appears in festival_data.
