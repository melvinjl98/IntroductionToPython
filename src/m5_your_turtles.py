"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Josh Melvin.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

link = rg.SimpleTurtle()
link.pen = rg.Pen('gold', 3)
link.speed = 15
size= 100
for k in range(5):
    link.draw_regular_polygon(3, size)
    link.pen_up()
    link.right(45)
    link.forward(10)
    link.left(45)
    link.pen_down()
    size = size - 10

zelda = rg.SimpleTurtle()
zelda.pen_up()
zelda.forward(100)
zelda.pen = rg.Pen('gold', 3)
zelda.speed = 15
size= 100
zelda.pen_down()
for k in range(5):
    zelda.draw_regular_polygon(3, size)
    zelda.pen_up()
    zelda.right(45)
    zelda.forward(10)
    zelda.left(45)
    zelda.pen_down()
    size = size - 10

ganon = rg.SimpleTurtle()
ganon.pen = rg.Pen('gold', 3)
ganon.speed = 15
size= 100
ganon.pen_up()
ganon.forward(50)
ganon.left(90)
ganon.forward(89)
ganon.right(90)
ganon.pen_down()
for k in range(5):
    ganon.draw_regular_polygon(3, size)
    ganon.pen_up()
    ganon.right(45)
    ganon.forward(10)
    ganon.left(45)
    ganon.pen_down()
    size = size - 10

window.close_on_mouse_click()
