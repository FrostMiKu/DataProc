from typing import Callable, Tuple
import numpy as np

class Data:
    def __init__(self,t:list) -> None:
        self.t = np.array(t)

    def __str__(self) -> str:
        return self.t.__str__()

    def value(self) -> np.array:
        return self.t

    def getArray(self, func:Callable) -> list:
        return np.array(list(map(func,self.t)))

    def getSet(self, func:Callable) -> set:
        l = set()
        for line in self.t:
            l.add(func(line))
        return l

    def toCsv(self, path:str) -> None:
        np.savetxt(path, self.t, delimiter=",", fmt='%s')

    def row(self, row:int) -> np.array:
        return self.t[row]

    def col(self, col:int) -> np.array:
        return self.getArray(lambda x:x[col])

    def head(self, row:int):
        return Data([i for i in self.t[:row]])
    
    def tail(self, row:int):
        return Data([i for i in self.t[-row:]])

    def window(self, pos1:Tuple[int, int], pos2:Tuple[int, int]):
        return Data(self.t[pos1[0]:pos2[0],pos1[1]:pos2[1]])