# 🚨 Don't change the code below 👇
sum = 0
i = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
    sum += int(student_heights[n])
    i = n+1

print("Average Height is", round(sum/i))


# Write your code below this row 👇

# 🚨 Don't change the code below 👇 === First Attempt
# sumofheight = 0
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     sumofheight += int(student_heights[n])
# # 🚨 Don't change the code above 👆
# print(f"Average Height of student:{round(sumofheight/len(student_heights))}")

# Write your code below this row 👇
