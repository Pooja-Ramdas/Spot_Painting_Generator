import colorgram
from turtle import Turtle, Screen
import random
my_screen= Screen()
my_screen.setup(width=500,height=500)
my_screen.setworldcoordinates(-1, -1, my_screen.window_width() - 1, my_screen.window_height() - 1)
width=my_screen.window_width()
height=my_screen.window_height()
my_screen.colormode(255)
dog=Turtle()
dog.pensize(1)
dog.shape('circle')
row_number=0

def color_extractor(filename):
    colors=colorgram.extract(filename,5)
    color_list=[]
    for color in colors:
        Rgb=color.rgb
        color_tuple=(Rgb.r,Rgb.g,Rgb.b)
        color_list.append(color_tuple)
    return(color_list)
filenames={
    'p':'Pink.jpg',
    'g':'Green.jpg',
    'i':'icy.jpg',
    'b':'beach.jpg',
    's':'sages.jpg',
    'r':'rosy.jpg',
    'w':'warms.jpg',
}
def random_colour_generator():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)
print("Hello! Pick a colour palette for your spot painting!")
print("Given below is a list of available colour palettes: ")
print("Random (r)\nPink (p)\nGreen (g)\nBeachy (b)\nSage (s)\nIce (i)\nRose (r)\nWarm (w)")
print("Enter the letter provided in parenthesis corresponding to whichever color you want to pick.")
c=input("Enter Colour Letter Here : ").lower()
if c!='r':
    filename=filenames[c]
    colors=color_extractor(filename)
    dog.color(random.choice(colors))
elif c=='r':
    print("Each dot will have a random colour now.")

else:
    while c not in filenames.keys():
        c=input("Sorry! We don't have that colour palette, try another: ")
        c=input("Enter Colour Letter Here : ").lower()
        filename=filenames[c]
        colors=color_extractor(filename)
        dog.color(random.choice(colors))

def a_row_of_spots():
    dog.penup()
    number_of_dots=0
    global row_number
    while(number_of_dots<=10):
        if c!='r':
            dog.dot(20,random.choice(colors))
        elif c=='r':
            dog.dot(20,random_colour_generator())
        number_of_dots+=1
        dog.forward(50)
    row_number+=1
    return(row_number)

def going_up(row_num):
    if(row_num%2!=0):
        dog.left(90)
        dog.forward(50)
        dog.left(90)
    else:
        if c!='r':
            dog.dot(20,random.choice(colors))
        else:
            dog.dot(20,random_colour_generator())
        dog.right(90)
        dog.forward(50)
        dog.right(90)

n=0
while(n<=10):
    num_row=a_row_of_spots()
    going_up(num_row)
    n+=1
print(dog)
my_screen.exitonclick()
