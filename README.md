# PLMBR 

> ⚠️ Warning  
> ---
> This library is currently in active development and may undergo breaking changes. Do not use it in production environments

## Installation

Installing `plmbr`, which is available as a Python package, can be done with `pip`, preferably in a virtual environment.  Launch a terminal and use the following command to install `plmbr`.

```
pip install plmbr
```

## Introduction

It is a Python library for building predictable, reproducible, scalable, and robust data pipelines with ease. It wraps pandas with a clean, modular API inspired by TensorFlow’s Keras. `plmbr` simplifies complex data workflows into composable steps.

### Creating Pipe

```py
from pandas import DataFrame
from plmbr import Pipe

class DoubleIt(Pipe):
    def __init__(self, col: str, name = "DoubleIt"):
        self.name = name
        self.col = col

    def flow(self, data):
        data = data[self.col] * 2
        return data
```

### Building PipeLine

```py
from plmbr import PipeLine

pipeline = PipeLine([
    DoubleIt(col="A"),
])
```

### Processing Data

```py
df = DataFrame({ "A": [1, 2, 3] }, columns=["A"])
doubled_df = pipeline.flow(df)
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

## Inspiration

It is inspired by Keras `Sequential` API. Instead of layers, you stack `Pipe` objects inside a `PipeLine` and use the `flow` method similar to Keras `predict` function to process a pandas `DataFrame` through each step. This makes data transformations simple and consistent.

## Motivation

The motivation behind `plmbr` comes from the need to streamline data processing in machine learning and data-driven applications. Preparing data often takes significant time, especially when the desired structure is known but the raw data is far from it. plmbr was created to make this transformation process more organized and efficient.

## Contribute

This is an open-source project and welcomes contributions from the community. Whether you have ideas for new features, find bugs or usability issues, or want to submit a pull request, your input is appreciated. Contributions of all kinds—code, documentation, or feedback—help improve the library and shape its future.