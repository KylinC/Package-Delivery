import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
import os
from astropy import modeling


def func(x, a, b, c):
    return (a * x+b) / np.exp(x) + c


money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs2/sol_cost"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs2/sol_time"
f2 = open(money_fixstr + ".txt", "r")
lines2 = f2.readlines()


dict = {}
dict[0] = 0
a_list = np.arange(1, 130, 1)
for i in a_list:
    dict[i] = 0

x_max = 1
x_min = 1
for i in range(len(lines1)):
    x = (float(lines1[i])*60*24/float(lines2[i]))
    x = int(x)
    dict[x] += 1

fig = plt.figure(figsize=(18, 10))

ax1 = fig.add_subplot(111)

print(dict)
# dict[10] = 20000
ax1.set_xlim([0, 0.52])
x_ruler = np.arange(0, 0.5, 0.05)
plt.xticks(x_ruler)

a_list = np.delete(a_list, 9)  # delete

value = []

tmp_val = np.array([0])
tmp_val = np.append(tmp_val, a_list)
a_list = tmp_val

for i in a_list:
    if(i == 10):  # delete
        continue  # delete
    value.append(dict[i])
a_list = 0.1 * a_list + 0.05
plt.scatter(a_list,  value, color="violet", s=50, label='DFS2Cost/Day')

# new_scale_ru = np.arange(0, 10.5, 0.01)
# z1 = np.polyfit(a_list, value, 18)
# p1 = np.poly1d(z1)
# yvals = p1(new_scale_ru)
# plot2 = ax1.plot(new_scale_ru, yvals, 'r', label='Rate Fitcurve')

# new_scale_ru = np.arange(0.15, 10.5, 0.01)
# popt, pcov = optimize.curve_fit(func, a_list, value)
# y3 = func(new_scale_ru, *popt)
# plot1 = ax1.plot(new_scale_ru, y3, "purple", label='Rate Fitcurve')

new_scale_ru = np.arange(0, 10.5, 0.01)
fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D() # depending on the data you need to give some initial values
fitted_model = fitter(model, a_list, value)
# plt.plot(a_list, value)
ax1.plot(new_scale_ru, fitted_model(new_scale_ru), "purple", label='DFS2Cost/Day Distribution')


###################################################
# type 2
###################################################

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs3/sol_cost"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs3/sol_time"
f2 = open(money_fixstr + ".txt", "r")
lines2 = f2.readlines()

dict = {}
dict[0] = 0
a_list = np.arange(1, 130, 1)
for i in a_list:
    dict[i] = 0

x_max = 1
x_min = 1
for i in range(len(lines1)):
    x = (float(lines1[i])*60*24/float(lines2[i]))
    x = int(x)
    dict[x] += 1

a_list=np.delete(a_list, 9)  # delete

value = []

tmp_val = np.array([0])
tmp_val = np.append(tmp_val, a_list)
a_list = tmp_val

for i in a_list:
    if(i == 10):  # delete
        continue  # delete
    value.append(dict[i])
a_list = 0.1 * a_list + 0.05
plt.scatter(a_list,  value, color="orangered", s=50, label='DFS3Cost/Day')

# new_scale_ru = np.arange(0.15, 10.5, 0.01)
# z2 = np.polyfit(a_list, value, 18)
# p2 = np.poly1d(z2)
# yvals2 = p2(new_scale_ru)
# plot2 = ax1.plot(new_scale_ru, yvals2, 'b', label='Distribution Shift')

new_scale_ru = np.arange(0, 10.5, 0.01)
fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D()  # depending on the data you need to give some initial values
fitted_model = fitter(model, a_list, value)
# plt.plot(a_list, value)
ax1.plot(new_scale_ru, fitted_model(new_scale_ru), "red", label='DFS3Cost/Day Distribution')

###################################################
###################################################
# type 3
###################################################
###################################################

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs4/sol_cost"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs4/sol_time"
f2 = open(money_fixstr + ".txt", "r")
lines2 = f2.readlines()

dict = {}
dict[0] = 0
a_list = np.arange(1, 130, 1)
for i in a_list:
    dict[i] = 0

x_max = 1
x_min = 1
for i in range(len(lines1)):
    x = (float(lines1[i])*60*24/float(lines2[i]))
    x = int(x)
    dict[x] += 1

a_list=np.delete(a_list, 9)  # delete

value = []

tmp_val = np.array([0])
tmp_val = np.append(tmp_val, a_list)
a_list = tmp_val

for i in a_list:
    if(i == 10):  # delete
        continue  # delete
    value.append(dict[i])
a_list = 0.1 * a_list + 0.05
plt.scatter(a_list,  value, color="cyan", s=50, label='DFS4Cost/Day')

# new_scale_ru = np.arange(0.15, 10.5, 0.01)
# z2 = np.polyfit(a_list, value, 18)
# p2 = np.poly1d(z2)
# yvals2 = p2(new_scale_ru)
# plot2 = ax1.plot(new_scale_ru, yvals2, 'b', label='Distribution Shift')

new_scale_ru = np.arange(0, 10.5, 0.01)
fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D()  # depending on the data you need to give some initial values
fitted_model = fitter(model, a_list, value)
# plt.plot(a_list, value)
ax1.plot(new_scale_ru, fitted_model(new_scale_ru), "blue", label='DFS4Cost/Day Distribution')

###################################################

###################################################
###################################################
# type 4
###################################################
###################################################

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs5/sol_cost"
f2 = open(money_fixstr + ".txt", "r")
lines1 = f2.readlines()

money_fixstr = "/Users/kylinchan/Documents/Spring2019-Git/Package-Delivery/problem1/dfs5/sol_time"
f2 = open(money_fixstr + ".txt", "r")
lines2 = f2.readlines()

dict = {}
dict[0] = 0
a_list = np.arange(1, 130, 1)
for i in a_list:
    dict[i] = 0

x_max = 1
x_min = 1
for i in range(len(lines1)):
    x = (float(lines1[i])*60*24/float(lines2[i]))
    x = int(x)
    dict[x] += 1

a_list=np.delete(a_list, 9)  # delete

value = []

tmp_val = np.array([0])
tmp_val = np.append(tmp_val, a_list)
a_list = tmp_val

for i in a_list:
    if(i == 10):  # delete
        continue  # delete
    value.append(dict[i])
a_list = 0.1 * a_list + 0.05
plt.scatter(a_list,  value, color="deepskyblue", s=50, label='DFS5Cost/Day')

# new_scale_ru = np.arange(0.15, 10.5, 0.01)
# z2 = np.polyfit(a_list, value, 18)
# p2 = np.poly1d(z2)
# yvals2 = p2(new_scale_ru)
# plot2 = ax1.plot(new_scale_ru, yvals2, 'b', label='Distribution Shift')

new_scale_ru = np.arange(0, 10.5, 0.01)
fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D()  # depending on the data you need to give some initial values
fitted_model = fitter(model, a_list, value)
# plt.plot(a_list, value)
ax1.plot(new_scale_ru, fitted_model(new_scale_ru), "dodgerblue", label='DFS5Cost/Day Distribution')

###################################################



ax1.legend(loc=1)
plt.savefig('costperday,.jpg')
plt.show()



