import pandas as pd

dis = pd.read_csv("dis.csv", encoding='utf-8')
df = pd.DataFrame(dis.values, index=range(1, dis.index[-1] + 2))
