# # 1- WHILE LOOP:
# # in the while loop we can execute a set of statements as long as a condition is true.

# i = 1
# while i <= 10:
#     print(f"{i} Ajab Gul ")
#     i = i+1

# # while loop break
# x = 0
# while x <= 10:
#     print(f"{x} raddy gul ")
#     if x == 5:
#         break
#     x = x+1

# # while loop continue
# z = 0
# while z <= 10:
#     if z == 5:
#         continue
#     print(f"{z} kakar ")
#     z = z+1


# 2- FOR LOOP:
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
# a set, or a string).

# for b in range(5, 10):
#     print(b)


day = ["mon", "thu", "wed", "thr", "fri", "sut", "sun"]

for i in day:
    # if (i == "fri"): # break loop
    if (i == "thu"):  # skip the day
        continue
    print(i)
