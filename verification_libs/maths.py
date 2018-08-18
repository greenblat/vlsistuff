
import math


def sqrt(X):
    if X<0: X = -X
    return math.sqrt(X)
def buf(A):
    return A
def divi(A,B):
    try: 
        return A/B 
    except:
        return 0

def question(Cond,Yes,No):
    if Cond: return Yes 
    return No

def sqdist(A,B):
    return (A*A+B*B)

def dist2(A,B):
    return math.sqrt(A*A+B*B)
def dist3(A,B,C):
    return math.sqrt(A*A+B*B+C*C)

def cos(A):
    return math.cos(A)
def sin(B):
    return math.sin(B)
def arccos(A):
    return math.acos(A)
def arctan(A):
    return math.atan(A)



