
import copy

from geometric_obj import Geometric_obj
from vector_and_matrix import Vector, MatrixNxN


class Cuboid(Geometric_obj):

    def __init__(self, midPt, xLen, yLen, zLen):
        if isinstance(midPt,Vector) and midPt.getSize()==3:
            self.midPt = midPt
        elif isinstance(midPt, list) and len(midPt)==3:
            self.midPt = Vector(3,midPt)
        elif isinstance(midPt, tuple) and len(midPt)==3:
            self.midPt = Vector(3,list(midPt))
        elif (isinstance(midPt,list) or isinstance(midPt,tuple)) and len(midPt)!=3:
            raise ValueError('midPt should be tuple/list with lenght 3 or instance of class Vector(3)')
        elif (isinstance(midPt, Vector) and midPt.getSize()!=3):
            raise ValueError('midPt should be tuple/list with lenght 3 or instance of class Vector(3)')
        else:
            raise ValueError('midPt should be tuple/list with lenght 3 or instance of class Vector(3)')
        self.__initCuboid__(xLen, yLen, zLen)

    def __initCuboid__(self, xLen, yLen, zLen):
        tmp = (xLen, yLen, zLen)
        for i in tmp:
            if not(isinstance(i,int) or isinstance(i, float)):
                raise TypeError('Dimensions must be int or float values')
        tmpVec = Vector(3)
        # self.vertexesList.append(Vector(3),)
        
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)-xLen/2.0,
                                        self.midPt.getCoord(1)-yLen/2.0,self.midPt.getCoord(2)-zLen/2.0)))
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)+xLen/2.0,
                                        self.midPt.getCoord(1)-yLen/2.0,self.midPt.getCoord(2)-zLen/2.0)))
        
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)-xLen/2.0,
                                        self.midPt.getCoord(1)+yLen/2.0,self.midPt.getCoord(2)-zLen/2.0)))
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)+xLen/2.0,
                                        self.midPt.getCoord(1)+yLen/2.0,self.midPt.getCoord(2)-zLen/2.0)))
        
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)-xLen/2.0,
                                        self.midPt.getCoord(1)-yLen/2.0,self.midPt.getCoord(2)+zLen/2.0)))
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)+xLen/2.0,
                                        self.midPt.getCoord(1)-yLen/2.0,self.midPt.getCoord(2)+zLen/2.0)))
        
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)-xLen/2.0,
                                        self.midPt.getCoord(1)+yLen/2.0,self.midPt.getCoord(2)+zLen/2.0)))
        self.vertexesList.append(Vector(3,(self.midPt.getCoord(0)+xLen/2.0,
                                        self.midPt.getCoord(1)+yLen/2.0,self.midPt.getCoord(2)+zLen/2.0)))



        
        # print(self.vertexesList)
    def getFileString(self):
        cuboidStr = ''
        return cuboidStr

    def __str__(self):
        s=''
        for i in range(0, len(self.vertexesList)):
            s+=self.vertexesList[i].getStr()
            if i%2==1 and i!=0:
                s+='\n'
        return s 
            
        

C=Cuboid([0,0,0], 20,20,20)
print(C)
