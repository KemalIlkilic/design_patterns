## What does do

The **init**.py file is a Python file that is executed when a package is imported.

## What Includes

It can contain initialization code for the Package, such as importing submodules, defining variables, or executing other code.

### Usage Example 1

labeling a directory as a Python package and defining /\_\_all/\_\_

<pre>
```python
from .abstract import HouseBuilder
from .concrete import SmallHouseBuilder, BigHouseBuilder, HouseDirector

__all__ = [
"HouseBuilder",
"SmallHouseBuilder",
"BigHouseBuilder",
"HouseDirector"
]
```
</pre>

### Usage Example 2

Allows you to define any variable at the package level. Doing so is often convenient if a package defines something that will be imported frequently, in an API-like fashion

An example
Here is an example from one of my projects, in which I frequently import a sessionmaker called Session to interact with my database. I wrote a "database" package with a few modules:

database/
_init_.py
schema.py
insertions.py
queries.py

My _init_.py contains the following code:

<pre>
```python

import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=engine)
```
</pre>

Since I define Session here, I can start a new session using the syntax below. This code would be the same executed from inside or outside of the "database" package directory.

<pre>
```python

from database import Session
session = Session()
```
</pre>
