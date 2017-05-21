######################################################
## Set each colour to a brightness of your choosing ##
##                                                  ##
## Example by Jason - @Boeeerb                      ##
######################################################

from piglow import PiGlow

piglow = PiGlow()

val = eval(input("White: "))
piglow.white(val)

val = eval(input("Blue: "))
piglow.blue(val)

val = eval(input("Green: "))
piglow.green(val)

val = eval(input("Yellow: "))
piglow.yellow(val)

val = eval(input("Orange: "))
piglow.orange(val)

val = eval(input("Red: "))
piglow.red(val)

val = eval(input("All: "))
piglow.all(val)
