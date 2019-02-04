# pySwat
### A simple script that will automatically search for errors when programming.
## Installation:
`pip install pySwat`
## Usage:
```python
import sys
from pySwat import *
try:
#Your Code in this try block




#End your code
except: # On error call pySwat
    searchError(str(sys.exc_info()[1]))

```

