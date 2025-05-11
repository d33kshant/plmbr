import abc
import pandas as pd
import typing as tp

class Layer:
    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        ...

class PipeLine:
    def __init__(self, layers: list[Layer], name: str = ""):
        self.layers = layers
        self.name = name

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        result = data.copy()
        for layer in self.layers:
            try:
                result = layer.flow(result)
            except Exception as e:
                raise RuntimeError(f"PipeLine failed on {layer.name}: {e}") from e
        return result
    
    def build(self) -> tp.Callable:
        def pipeline(data: pd.DataFrame) -> pd.DataFrame:
            return self.flow(data)
        return pipeline

    def __repr__(self):
        return str(
            pd.Series(
                [layer.name for layer in self.layers],
                name=self.name if self.name else "Unnamed",
            )
        )