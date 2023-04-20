# ###########DEBUGGING#####################

# # Describe Problem


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# The 2nd parameter of the range() function is exclusive, meaning loop only runs till i == 19.
