"""Grid Excersice By Aaron Shapiro"""


def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_hor():
    print '+ - - - -',

def print_vert():
    print '|        ',

def print_horz():
    do_twice(print_hor)
    print '+'

def print_verts():
    do_twice(print_verts)
    print '|'

def print_row():
    print_horz()
    do_four(print_horz)

def print_grid():
    do_twice(print_row)
    print_verts()

print_grid()
