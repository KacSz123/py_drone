import numpy as np
import math

class matrixNxN:
    def __init__(self, n):
        self.__mSize = n
        self.__matrix = np.array([[round(0.0,3)]*n]*n)
        # print(self.__matrix)


    def getMatrix(self):
        return self.__matrix
    def getsize(self):
        return self
    def __add__(self, other):
        if isinstance(other,matrixNxN):
            if self.__mSize != other.__mSize:
                print('***Matrices are different size!***\n')
                raise TypeError
            self.__matrix = np.add(self.__matrix,other.getMatrix())
        elif isinstance(other, int) or  isinstance(other, float):

            self.__matrix = np.add(self.__matrix,other)
        return self
    def __sub__(self, other):
        if isinstance(other,matrixNxN):
            if self.__mSize != other.__mSize:
                print('***Matrices are different size!***\n')
                raise TypeError
            self.__matrix = np.subtract(self.__matrix,other.getMatrix())
        elif isinstance(other, int) or  isinstance(other, float):

            self.__matrix = np.subtract(self.__matrix,other)
        return self
    

    
    def __str__(self) -> str:
        return str(self.__matrix.round(4))
    

    def rot_X_martrix(self, angle):
        theta = math.radians(angle)
        c,s = math.cos(round(theta,4)), math.sin(round(theta,4))
        if self.__mSize==3:
            self.__matrix[0]=[1.0, 0.0, 0.0]
            self.__matrix[1]=[0.0, c,-s]
            self.__matrix[2]=[0.0, s, c]
        elif self.__mSize == 2:
            self.__matrix[0]=[c,s]
            self.__matrix[1]=[-s,c]
        else:
            print('rotation matrix must have size 2x2 or 3x3')
            raise ValueError       
        return self
    def rot_Y_martrix(self, angle):

        theta = math.radians(angle)
        c,s = math.cos(round(theta,4)), math.sin(round(theta,4))
        if self.__mSize==3:
            self.__matrix[0]=[ c ,0, s]
            self.__matrix[1]=[ 0, 1, 0]
            self.__matrix[2]=[-s, 0, c]
        elif self.__mSize == 2:
            self.__matrix[0]=[c,s]
            self.__matrix[1]=[-s,c]
        else:
            print('rotation matrix must have size 2x2 or 3x3')
            raise ValueError      
        return self 
    def rot_Z_martrix(self, angle):
        theta = math.radians(angle)
        c,s = math.cos(round(theta,4)), math.sin(round(theta,4))
        if self.__mSize==3:
            self.__matrix[0]=[c,-s, 0]
            self.__matrix[1]=[s, c, 0]
            self.__matrix[2]=[0, 0, 1]
        elif self.__mSize == 2:
            self.__matrix[0]=[c,s]
            self.__matrix[1]=[-s,c]
        else:
            print('rotation matrix must have size 2x2 or 3x3')
            raise ValueError     
        return self   

def test():

    m = matrixNxN(3)
    mm = matrixNxN(3)
    m = m+3
    m=m.rot_X_martrix(90)
    print(m)
    print()
    mm.rot_Z_martrix(90)
    print(mm)
    print()
    print(m+mm)

test()