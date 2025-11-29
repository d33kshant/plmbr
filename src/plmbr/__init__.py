from abc import abstractmethod 
import pandas as pd
import typing as tp

class Pipe:
    @abstractmethod
    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        ...

class Pipeline:
    def __init__(self, pipes: tp.List[Pipe]):
        self.pipes = pipes
    
    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        for pipe in self.pipes:
            data = pipe.flow(data)
        return data
