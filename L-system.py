#coding:utf-8
import turtle
import string
import time
lsystem_string="0F"
lsystem_rules=[["F", "0FF-[-1F+F+F]+[+1F-F-F]"] ]
lsystem_length=10
lsystem_angle=22.5
lsystem_iterations=4
lsystem_colours=["brown", "lime green" ]

starting_position=(0,-250)
starting_angle=90
#animation_timing means the the time interval between two showing iterations
animation_timing = 2

operation_dict={}
def _no_action():pass

def _move_forward(distance):
    turtle.penup()
    turtle.forward(distance)
    turtle.pendown()

func_list=[lambda:turtle.forward(lsystem_length),lambda:_move_forward(lsystem_length),lambda:_no_action()]
operation_dict={val:func_list[ind//6] for ind,val in enumerate(string.ascii_uppercase[:-10]+'XY')}
operation_dict['+'],operation_dict['-'],operation_dict['^']=\
    lambda:turtle.left(lsystem_angle),lambda:turtle.right(lsystem_angle),lambda:turtle.left(180)

def drawing(action_string):
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(starting_position)
    turtle.setheading(starting_angle)
    turtle.pendown()

    stack=[]
    for act in action_string:
        if act.isdigit():
            turtle.pencolor(lsystem_colours[int(act)])
            continue
        elif act=='[':
            stack.append((turtle.pos(),turtle.heading()))
        elif act==']':
            if stack:
                info=stack.pop()
                turtle.goto(info[0])
                turtle.setheading(info[1])
        else:
            operation_dict[act]()
    turtle.tracer(True)

iteration_dict={k:v for k,v in lsystem_rules}
def _iteration(cur_string):

    for i in range(lsystem_iterations):
        last_string=''
        for k in cur_string:
            last_string+=iteration_dict.get(k,k)
        cur_string=last_string
        turtle.clear()
        drawing(cur_string)
        time.sleep(animation_timing)

_iteration(lsystem_string)
