
from DataProc.data import Data

class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, path:str, offset:int, delimiter:str) -> Data:
        with open(path) as f:
            lines = f.readlines()[offset:]
            t = list(map(lambda x: x[:-1].split(delimiter), lines))
            return Data(t)

    def loadCsv(self, path:str) -> Data:
        return self.parse(path,0,',')
