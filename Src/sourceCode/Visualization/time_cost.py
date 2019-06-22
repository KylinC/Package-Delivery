import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
import os


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


x = np.arange(0, 10, 0.1)

file_number = 100
file_range = range(1, file_number+1, 1)

money_cost = []
money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/x/data/sol_cost_"
for item in file_range:
    f2 = open(money_fixstr + str(item) + ".txt", "r")
    lines = f2.readlines()
    sol = 0
    for line3 in lines:
        sol += float(line3)
    money_cost.append(sol / len(lines))

time_cost = []
time_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/x/data/sol_time_"
for item in file_range:
    f2 = open(time_fixstr + str(item) + ".txt", "r")
    lines = f2.readlines()
    sol = 0
    for line3 in lines:
        sol += float(line3)
    time_cost.append(sol / len(lines))

# figsize=(14,10)
fig = plt.figure(figsize=(18,10))

ax1 = fig.add_subplot(111)
ax1.scatter(x, money_cost, s=10, label='Money Cost')
ax1.set_ylabel('Average Money Cost')
ax1.yaxis.label.set_color('purple')
ax1.set_title("----  Rate influence on Average Money Cost/Average Time Cost  ----")

ax2 = ax1.twinx()  # this is the important function
ax2.scatter(x, time_cost, s=10, color='orange', label='Time Cost')
ax2.set_xlim([0, 10])
x_ruler = np.arange(0, 10.3, 0.5)
plt.xticks(x_ruler)
ax2.set_ylabel('Average Time Cost')
ax2.yaxis.label.set_color('red')
ax1.set_xlabel('Rate of CostFunction')

aimlist = money_cost
x_list = x

# x_list=[]
# aimlist=[]
# for i in range(0, 17):
#     aimlist.append(money_cost[i])
#     x_list.append(0.1*i)
#
# for i in range(20, 100, 10):
#     aimlist.append(money_cost[i])
#     x_list.append(0.1 * i)

aimlist = np.array(aimlist)
x_list = np.array(x_list)
popt, pcov = optimize.curve_fit(func, x_list, aimlist)
y3 = func(x_list, *popt)
plot1 = ax1.plot(x_list, y3, "purple", label='Money Cost')

z1 = np.polyfit(x, time_cost, 5)
p1 = np.poly1d(z1)
yvals = p1(x)
plot2 = ax2.plot(x, yvals, 'r', label='Time Cost')

x1 = 0.5
y1 = 770
ax2.scatter([x1, ], [y1, ], 20, color='black')
ax2.plot([x1, x1], [0, y1+700], color="grey", linewidth=2.5, linestyle="--")
ax2.plot([0, x1], [y1, y1], color="purple", linewidth=2.5, linestyle='--')
ax2.plot([x1, x1+100], [y1+240, y1+50], color="red", linewidth=2.5, linestyle='--')

ax1.legend(bbox_to_anchor=(1.02, 0), loc=3)
ax2.legend(bbox_to_anchor=(1.03, 0.1), loc=3)

plt.savefig('Rate.jpg')
plt.show()