# Package-Delivery-on-Double-11-Day
> Team project for SJTU-CS214, Dr.Xiaofeng Gao.



### ButterflySystem

- **Download** and **Install**

```bash
ubuntu@ git clone https://github.com/KylinC/Package-Delivery.git
```

```
ubuntu@ cd Butterfly
```

```
ubuntu@ tar -zxvf ButterflySystem-1.1.tar.gz
```

```
ubuntu@ cd Butterfly
```

```
ubuntu@ cd ButterflySystem-1.1/
```

```
ubuntu@ sudo python setup.py install
```

- **Test**

```
ubuntu@ Python
```

```
>> import ButterflySystem
```

> If no report error, butterfly installed.

### Pre-processed Data

```
linux@ cd DataSet
```

```
linux@ python
```

```
>> from ButterflySystem.Data import *
```

### Data Analysis

> Cost Function Rate Infulence 

![](http://kylinhub.oss-cn-shanghai.aliyuncs.com/2019-06-22-Rate.jpg)



> IDDFS Depth Influence

![](http://kylinhub.oss-cn-shanghai.aliyuncs.com/2019-06-22-costperday-.jpg)

> Approximation Analysis

![](http://kylinhub.oss-cn-shanghai.aliyuncs.com/2019-06-22-time_dfs4dfs6_norm.jpg)