"""Koch By Aaron Shapiro"""


from swampy.TurtleWorld import *

def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
    return
    koch(t, n)
    lt(t, 60)
    koch(t, n)
    rt(t, 120)
    koch(t, n)
    lt(t, 60)
    koch(t, n)

print koch(10, 45)

