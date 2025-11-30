# PLMBR 
create data processing pipelines

## Installation

Installing `plmbr`, which is available as a Python package, can be done with `pip`, preferably in a virtual environment.  Launch a terminal and use the following command to install `plmbr`.

```
pip install plmbr
```

## Introduction

It is a Python library for building predictable and reproducible data pipelines with ease. It wraps pandas with a clean, modular API inspired by TensorFlow’s Keras. `plmbr` simplifies complex data workflows into composable steps. This works with Jupyter notebooks as well.

### Creating Pipes
`Pipe` objects are simple python classes that implements `flow` method which takes a pandas `DataFrame` as input and returns a pandas `DataFrame` as output. `Pipe` objects are mean to perform a specific operation on the data. Following is an example of a `Pipe` object that doubles the values in a column.

```py
from pandas import DataFrame
from plmbr import Pipe, Pipeline

class DoubleIt(Pipe):
    def __init__(self, col: str):
        self.col = col

    def flow(self, data: DataFrame) -> DataFrame:
        data[self.col] = data[self.col] * 2
        return data
```

### Building Pipeline
`Pipeline` is similar to `Sequential` in Keras. It takes a list of `Pipe` objects as input and builds a pipeline of operations. Each `Pipe` object is called in sequence to process the data.

```py
pipeline = Pipeline([
    DoubleIt(col="A"),
])
```

### Processing Data

```py
df = DataFrame({ "A": [1, 2, 3] }, columns=["A"])
doubled_df = pipeline(df) # or pipeline.flow(df)
doubled_df
```
<div class="result" style="font-family: var(--font-monospace);">
    <table>
    <thead>
        <tr style="text-align: right;">
        <th></th>
        <th>A</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td>0</td>
        <td>2</td>
        </tr>
        <tr>
        <td>1</td>
        <td>4</td>
        </tr>
        <tr>
        <td>2</td>
        <td>6</td>
        </tr>
    </tbody>
    </table>
</div>

## Contribute

Data transformation is a complex task, and `plmbr` is designed to be extensible and flexible to accommodate a wide range of use cases. If you have ideas for new features, find bugs or usability issues, or want to submit a pull request, your input is appreciated. Contributions of all kinds code, documentation, or feedback help improve the library and shape its future.