# ButterflySystem

> ButterflySystem provides a time-slice method to fully utilize multi-processes.



**Sample:**

```python
from ButterflySystem import *

dataFolderPath = "../sourceData"
# the folder must contains *.csv

nodeNumber = 665

coreNumber = 16
# this variable equals to time-slice number, relations with cores are not necessary

model = ButterflySystem(dataFolderPath, nodeNumber, coreNumber)

model.parse_matrix()
# process origin data to time-slice data

aim_variable = model.data_out()
# dict type sliceNumber -> orderlist
```

