from abc import abstractmethod 
import pandas as pd
import typing as tp

class Pipe:
    @abstractmethod
    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Pipe must implement the flow method") 
    
    def __call__(self, data: pd.DataFrame) -> pd.DataFrame:
        return self.flow(data)

class Pipeline:
    def __init__(self, pipes: tp.List[Pipe]):
        self.pipes = pipes
    
    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        assert isinstance(data, pd.DataFrame), "Input must be a pandas DataFrame"
        for pipe in self.pipes:
            try:
                data = pipe.flow(data)
                assert isinstance(data, pd.DataFrame), "Pipe must return a pandas DataFrame"
            except Exception as e:
                raise Exception(f"Error in pipe {pipe.__class__.__name__}: {str(e)}") from e
        return data

    def __call__(self, data: pd.DataFrame) -> pd.DataFrame:
        return self.flow(data)