from typing import List
from DataProc.data import Data

class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, text:List[str], offset:int, delimiter:str) -> Data:
        return Data(list(map(lambda x: x[:-1].split(delimiter) if x[-1]=='\n' else x.split(delimiter), text[offset:])))

    def loadFile(self, path:str, offset:int, delimiter:str) -> Data:
        with open(path) as f:
            return self.parse(f.readlines(), offset, delimiter)

    def loadCsv(self, path:str) -> Data:
        return self.parse(path,0,',')
