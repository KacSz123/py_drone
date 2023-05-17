from abc import ABC, abstractmethod
import numpy as np

class Geometric_obj(ABC):
    __vertexesList=[]
    __midPoint = np.array([0,0,0])
    __fileHandler = None


    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError
    
    @abstractmethod
    def printVertexes(self):
        raise NotImplementedError
    
