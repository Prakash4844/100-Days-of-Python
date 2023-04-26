### This code will not work in repl.it as there is no access to the colorgram package here.###
## We talk about this in the video tutorials##
# import colorgram
import random
import turtle as t
#
# rgb_colors = []
# colors = colorgram.extract('img2.jpg', 30)
#
# for color in colors:
#     rgb = color.rgb
#     new_color = (rgb.r, rgb.g, rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = t.Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")
tim.shape("turtle")
tim.up()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
color_list = [(53, 29, 35), (54, 14, 11), (38, 37, 49), (148, 71, 61), (144, 19, 14), (108, 66, 73),
              (208, 143, 121), (218, 78, 64), (115, 34, 39), (70, 67, 79), (62, 59, 73), (231, 47, 50),
              (250, 205, 173), (12, 17, 13), (247, 170, 145), (72, 64, 51), (71, 75, 71), (185, 138, 142),
              (151, 124, 102), (227, 211, 216), (145, 147, 159), (58, 67, 63), (226, 188, 153), (54, 67, 71),
              (246, 11, 21), (219, 168, 172), (221, 222, 231), (123, 126, 139), (150, 158, 148)]

for j in range(20):
    for i in range(20):
        tim.down()
        tim.dot(10, random.choice(color_list))
        tim.penup()
        tim.forward(20)

    tim.setheading(90)
    tim.forward(20)
    tim.setheading(180)
    tim.forward(400)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
