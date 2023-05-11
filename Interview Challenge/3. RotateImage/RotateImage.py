import numpy as np
def solution(a):
    a = np.rot90(a, k = -1)
    return a

