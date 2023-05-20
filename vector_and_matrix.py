import numpy as np
import math
import sys
class MatrixNxN:
    def __init__(self, n):
        self.__mSize = n
        self.__matrix = np.array([[round(0.0,4)]*n]*n)
        # print(self.__matrix)


    def getMatrix(self):
        return self.__matrix
    def getSize(self):
        return self.__mSize
    def __add__(self, other):
        if isinstance(other,MatrixNxN):
            if self.__mSize != other.__mSize:
                raise TypeError('***Matrices are different size!***\n')
            self.__matrix = np.add(self.__matrix,other.getMatrix())
        elif isinstance(other, int) or  isinstance(other, float):
            self.__matrix = np.add(self.__matrix,other)
        return self
    

    def __sub__(self, other):
        if isinstance(other,MatrixNxN):
            if self.__mSize != other.__mSize:
                raise TypeError('***Matrices are different size!***\n')
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
            raise ValueError('rotation matrix must have size 2x2 or 3x3')       
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
            raise ValueError('rotation matrix must have size 2x2 or 3x3')      
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
            raise ValueError('rotation matrix must have size 2x2 or 3x3')     
        return self   




class Vector():
    def __init__(self, size, coord=None): 
        self.__size = size
        if coord == None:
            self.__coordinates = np.array([0.0]*size)
        elif (isinstance(coord, list) or isinstance(coord, tuple))and len(coord) == size:
            self.__coordinates = np.array(coord)
        else:
            raise ValueError
    def getSize(self):
        return self.__size
    def getCoords(self):
        return self.__coordinates
    def getCoord(self, i):
        if i>=self.__size:
            raise ValueError('Vector size exceeded')
        return self.__coordinates[i]
    def setCoords(self,coords):
        # print('ugabuga')
        print(coords)
        if self.__size!=3:
            raise ValueError('Object must be instance of Vector(3)')
        if not isinstance(coords,tuple) and len(coords)!=3:
            raise TypeError('Coords should be tuple of lenghth 3: (x,y,z)')
        else:
            self.__coordinates[0]=coords[0]
            self.__coordinates[1]=coords[1]
            self.__coordinates[2]=coords[2]


    def __add__(self, other):
        if isinstance(other, Vector):
            if self.__size != other.getSize():
                raise ValueError('Both Vectors must be the same size!')
            self.__coordinates = self.__coordinates+other.getCoords()
        elif isinstance(other, int) or isinstance(other, float):
            self.__coordinates = self.__coordinates*other
        else:
            raise TypeError('Unsuported type')
        return self

    def __str__(self):
        return str(self.__coordinates.round(2))
    def __mul__(self, other):
        if isinstance(other, MatrixNxN):
            print(self.__size,'  ',other.getSize())
            if self.__size != other.getSize():
                raise ValueError('Matrix and Vector must be the same size!')
            else:
                return self.__coordinates.dot(other.getMatrix())
        elif isinstance(other, Vector):
            if self.__size != other.getSize():

                raise ValueError('Both Vectors must be the same size!')
        elif isinstance(other, int) or isinstance(other,float):
            self.__coordinates=np.dot(self.__coordinates,other)
        else:
            raise TypeError
        return self
    def __rmul__(self, other):
        pass
    def getStr(self):
        return str(self.__coordinates[0])+' '+str(self.__coordinates[1])+' '+str(self.__coordinates[2])+'\n'
def test():

    m = MatrixNxN(3)
    mm = MatrixNxN(3)
    m = m+3
    m=m.rot_X_martrix(90)
    v0,v1,v2,v3 = Vector(3), Vector(2),Vector(3), Vector(3,[1,1,1])

    mm.rot_Z_martrix(90)
    print(mm)
    v1=v1+v3
    v2=v3*mm
    v0=v0+10
    print(v0)
    print(v2)
    print(v1)
    # print(mm)
    # print()
    # print(m+mm)

# test()