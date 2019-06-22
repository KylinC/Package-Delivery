import matplotlib.pyplot as plt
import numpy as np

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem2/deg_info_after"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem2/deg_info"
f2 = open(money_fixstr + ".txt", "r")
lines2 = f2.readlines()

dict = {}
for item in lines2:
    tmp = item.split()
    dict[int(tmp[0])] = int(tmp[1])

Y1 = []
Y2 = []
Tag = []

for item in lines1:
    tmp = item.split()
    Tag.append(int(tmp[0]))
    Y1.append(int(tmp[1]))
    Y2.append(dict[int(tmp[0])])

Y1 = np.array(Y1)
Y2 = np.array(Y2)

n = 20
X = np.arange(n)

fig = plt.figure(figsize=(18,10))
ax1 = fig.add_subplot(111)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white', label="After set Hub")
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white', label="Before Set Hub")
plt.grid(color='gray')
ax1.set_ylabel('Degree')
plt.xticks([])
ax1.set_ylabel('City Tag')

for x, y in zip(X, Y1):
    plt.text(x , -950, '%d' % y, ha='center', va='bottom', size=15)

plt.ylim(-1000, +1000)

ax1.legend(loc=1)

plt.savefig('DegreeChange.jpg')
plt.show()