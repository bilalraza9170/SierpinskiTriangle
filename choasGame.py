#Sierpinski triangle
import turtle
import random

#to get midpoint
def midpoint(point1,point2):
    return ((point1[0]+point2[0])/2,(point1[1]+point2[1])/2)

#to get random vertex
def random_vertex(vertices):
    return random.choice(vertices)

#intialize the turtle screen
screen=turtle.Screen()
screen.setup(width=800, height=600)

#create a turtle
t=turtle.Turtle()
t.speed(0) #set the drawing speed to the fastest

#define the vertices of the triangle
vertices=[(-200,-100),(0,200),(200,-100)]

#draw the triangle 
for vertex in vertices:
    t.penup()
    t.goto(vertex)
    t.pendown()
    t.dot(5)

#pick a random starting point inside the traingle
current_point=random.choice(vertices)
t.penup()
t.goto(current_point)
t.pendown()
t.dot(5)

#infinite loop to generate new points
while True:
    random_vertex_point=random_vertex(vertices)

    #find the midpoint between the current point and the random vertex
    current_point=midpoint(current_point,random_vertex_point)

    #move the turtle to the new point and draw it
    t.penup()
    t.goto(current_point)
    t.pendown()
    t.dot(5)
    
#close the turtle graphics window on click
screen.exitonclick()
    
    




