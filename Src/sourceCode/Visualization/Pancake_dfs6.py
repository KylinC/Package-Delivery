import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager as fm
import matplotlib as mpl
from  matplotlib import cm

#############################
# import the data
#############################

dict = {2:0, 1:0}
file = open("/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs2/opt_size.txt", "r")
lines = file.readlines()
for item in lines:
    tem_value = int(item)
    if tem_value in dict:
        dict[tem_value] += 1
    else:
        dict[tem_value] = 0
print(dict)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:

labels = []
sizes = []
for i in dict.keys():
    labels.append(str(i))
    sizes.append(dict[i])
explode = (0.06, 0.03)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots(figsize=(6,6))

colors = cm.rainbow(np.arange(len(sizes))/len(sizes)) # colormaps: Paired, autumn, rainbow, gray,spring,Darks
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.6f%%', explode=explode,
        shadow=False, startangle=170, colors=colors)

ax.axis('equal')
ax.set_title('DFS depth = 2', loc='left')

proptease = fm.FontProperties()
proptease.set_size('xx-small')
# font size include: ‘xx-small’,x-small’,'small’,'medium’,‘large’,‘x-large’,‘xx-large’ or number, e.g. '12'
plt.setp(autotexts, fontproperties=proptease)
plt.setp(texts, fontproperties=proptease)

ax.legend(labels, loc=2)

plt.savefig('Demo_official_dfs2.jpg')
plt.show()