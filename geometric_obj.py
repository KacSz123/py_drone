from abc import ABC, abstractmethod
import numpy as np
import math
from vector_and_matrix import MatrixNxN, Vector
class Geometric_obj(ABC):
    __vertexesList=[]
    __midPoint = Vector(3)
    __fileHandler = None
    def moveObject(self, vector):
        for i in self.__vertexesList:
            i = i+vector


    def rotateObject(self, angle, axis='Z'):
        if not isinstance(angle, float) or not isinstance(angle, int) or not isinstance(axis,str):
            print("Angle must be int or float, axis must be one of strings: \"X\",\"Y\", \"Z\"")
            raise TypeError
        if axis.upper() != 'Z' or axis.upper() != 'X' or axis.upper() != 'Y': 
            print(" axis must be one of strings: \"X\",\"Y\", \"Z\" ")
            raise ValueError
        
        m=MatrixNxN(3)
        if axis.upper() == 'Z':
            m=m.rot_Z_martrix(angle)
        if axis.upper() == 'X':
            m=m.rot_X_martrix(angle)
        if axis.upper() == 'Y':
            m=m.rot_Y_martrix(angle)
        for i in self.__vertexesList:
            i=i.dot(m)
        


    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
    
    @abstractmethod
    def printVertexes(self):
        raise NotImplementedError
    
