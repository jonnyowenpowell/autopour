from colours import Colour
from solutions import find_solutions
from tube import Tube

a = Tube([Colour.DARK_BLUE, Colour.DARK_GREEN, Colour.LIGHT_BLUE, Colour.LIGHT_BLUE])
b = Tube([Colour.PURPLE, Colour.PINK, Colour.LIGHT_GREEN, Colour.GREY])
c = Tube([Colour.ORANGE, Colour.PURPLE, Colour.RED, Colour.BROWN])
d = Tube([Colour.ORANGE, Colour.PINK, Colour.RED, Colour.ORANGE])
e = Tube([Colour.DARK_GREEN, Colour.RED, Colour.YELLOW, Colour.DARK_BLUE])
f = Tube([Colour.YELLOW, Colour.DARK_GREEN, Colour.BROWN, Colour.DARK_GREEN])
g = Tube([Colour.BROWN, Colour.PURPLE, Colour.RED, Colour.NEON_GREEN])
h = Tube([Colour.NEON_GREEN, Colour.PURPLE, Colour.PINK, Colour.NEON_GREEN])
i = Tube([Colour.LIGHT_GREEN, Colour.GREY, Colour.LIGHT_BLUE, Colour.DARK_BLUE])
j = Tube([Colour.BROWN, Colour.YELLOW, Colour.GREY, Colour.LIGHT_GREEN])
k = Tube([Colour.GREY, Colour.YELLOW, Colour.NEON_GREEN, Colour.DARK_BLUE])
l = Tube([Colour.LIGHT_GREEN, Colour.LIGHT_BLUE, Colour.PINK, Colour.ORANGE])
m = Tube()
n = Tube()

tubes = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
solutions = find_solutions(tubes)   
