import math

def domino(m, n):
    area = m * n
    squares = 2 * 1
    
    return math.floor(area // squares)