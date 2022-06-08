import numpy as np

def text_list(input):
    f = open(input)
    num = f.read()
    f.close
    a = num.split()
    b = [float(s) for s in a ]
    return b