import pandas as pd
from .core import Pipe

class ReplaceValues(Pipe):
    def __init__(self, column: str, old_value: str, new_value: str, name: str = "ReplaceValues"):
        super().__init__(name)
        self.column = column
        self.old_value = old_value
        self.new_value = new_value

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.column] = data[self.column].replace(self.old_value, self.new_value)
        return data
    
class ConvertType(Pipe):
    def __init__(self, column: str, dtype: type, name: str = "ConvertType"):
        super().__init__(name)
        self.column = column
        self.dtype = dtype

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        data[self.column] = data[self.column].astype(self.dtype)
        return data
    
class DropDuplicates(Pipe):
    def __init__(self, subset: list[str] = None, keep: str = 'first', name: str = "DropDuplicates"):
        super().__init__(name)
        self.subset = subset
        self.keep = keep

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop_duplicates(subset=self.subset, keep=self.keep)

class DropNa(Pipe):
    def __init__(self, subset: list[str] = None, how: str = 'any', name: str = "DropNa"):
        super().__init__(name)
        self.subset = subset
        self.how = how

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.dropna(subset=self.subset, how=self.how)

class FillNa(Pipe):
    def __init__(self, value: str, subset: list[str] = None, name: str = "FillNa"):
        super().__init__(name)
        self.value = value
        self.subset = subset

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.fillna(value=self.value, subset=self.subset)

class SortValues(Pipe):
    def __init__(self, by: str, ascending: bool = True, name: str = "SortValues"):
        super().__init__(name)
        self.by = by
        self.ascending = ascending

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.sort_values(by=self.by, ascending=self.ascending)

class DropColumns(Pipe):
    def __init__(self, columns: list[str], name: str = "DropColumns"):
        super().__init__(name)
        self.columns = columns

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.drop(columns=self.columns) 

class RenameColumns(Pipe):
    def __init__(self, columns: dict[str, str], name: str = "RenameColumns"):
        super().__init__(name)
        self.columns = columns

    def flow(self, data: pd.DataFrame) -> pd.DataFrame:
        return data.rename(columns=self.columns)