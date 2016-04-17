import xlrd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import xlsxwriter as xw

data = xlrd.open_workbook(r"C:/Users/DY/Desktop/data2/test.xlsx")
table = data.sheets()[0]

time = table.col_values(11)
a = table.col_values(1)
b = table.col_values(2)
c = table.col_values(3)
d = table.col_values(4)
accx = table.col_values(5)
accy = table.col_values(6)
accz = table.col_values(7)
anglex = table.col_values(8)
angley = table.col_values(9)
anglez = table.col_values(10)


interval = 5

a1 = []
b1 = []
c1 = []
d1 = []
accx1 = []
accy1 = []
accz1 = []
anglex1 = []
angley1 = []
anglez1 = []

a2 = 0
b2 = 0
c2 = 0
d2 = 0
accx2 = 0
accy2 = 0
accz2 = 0
anglex2 = 0
angley2 = 0
anglez2 = 0

for i in range(len(time)):
    a2 += a[i]
    b2 += b[i]
    c2 += c[i]
    d2 += d[i]
    accx2 += accx[i]
    accy2 += accy[i]
    accz2 += accz[i]
    anglex2 += anglex[i]
    angley2 += angley[i]
    anglez2 += anglez[i]
    if i % interval == 0:
        a1.append(a2/interval)
        b1.append(b2/interval)
        c1.append(c2/interval)
        d1.append(d2/interval)
        accx1.append(accx2/interval)
        accy1.append(accy2/interval)
        accz1.append(accz2/interval)
        anglex1.append(anglex2/interval)
        angley1.append(angley2/interval)
        anglez1.append(anglez2/interval)
        a2 = 0
        b2 = 0
        c2 = 0
        d2 = 0
        accx2 = 0
        accy2 = 0
        accz2 = 0
        anglex2 = 0
        angley2 = 0
        anglez2 = 0
time = time[:int(len(time)/interval)]
a = a1
b = b1
c = c1
d = d1
accx = accx1
accy = accy1
accz = accz1
anglex = anglex1
angley = angley1
anglez = anglez1

# wbk = xw.Workbook(r'C:\Users\DY\Desktop\data2\test222.xlsx')
# sheet = wbk.add_worksheet()
# for i in range(len(time)):
#     sheet.write(i, 0, time[i])
#     sheet.write(i, 1, a[i])
#     sheet.write(i, 2, b[i])
#     sheet.write(i, 3, c[i])
#     sheet.write(i, 4, d[i])
#     sheet.write(i, 5, accx[i])
#     sheet.write(i, 6, accy[i])
#     sheet.write(i, 7, accz[i])
#     sheet.write(i, 8, anglex[i])
#     sheet.write(i, 9, angley[i])
#     sheet.write(i, 10, anglez[i])
# wbk.close()

X = []
Y = []
v0 = 0
vx = 0
Hz = 50
threshold = 50
n = 0
t = 0
S = []
acc = 0
zore = []
minusacc = 0
positiveacc = 0
angle = 0
x = 0
y = 0
minusnum = 0
positivenum = 0
s = 0
v = 0
flag = False

for i in range(len(time)):
    if a[i] > threshold and b[i] > threshold and c[i] > threshold:
        if minusnum != 0:
            acc = minusacc*16/32768/minusnum
            s = acc*pow(minusnum/10, 2)*0.5
            if positivenum != 0:
                acc = positiveacc*16/32768/positivenum
                s += acc*pow(positivenum/10, 2)*0.5
            angle = angle*100/32768/180*math.pi
            S.append(s)
            zore.append(0)
            x += s*math.cos(angle)
            y = s*math.sin(angle)
            X.append(x)
            Y.append(y)
    

            n = 0
            acc = 0
            minusnum = 0
            positivenum = 0
            minusnum = 0
            positiveacc = 0
            # angle = 0
            t = 0
        flag = True
    if a[i] <= threshold and b[i] <= threshold and c[i] <= threshold and d[i] <= 60 and flag is True:
        # t += 1/Hz
        # acc += accx[i]
        # angle += anglex[i]*1000/32768
        # acc += math.sqrt(pow(-accx[i], 2)+pow(accy[i], 2))
        # n += 1

        if accx[i] < 0:
            # minusacc += math.sqrt(pow(accx[i], 2)+pow(accy[i], 2))
            minusacc += -1*accx[i]
            minusnum += 1
            angle += anglex[i]
        elif accx[i] > 0 and minusnum != 0:
            positiveacc += accx[i]
            positivenum += 1
            angle += anglex[i]
        
        
    #     if v < 0:
    #         continue
    #     if accx[i] < 0:
    #         s += v/60+(-1*accx[i]*0.5/3600)
    #         v += -1*accx[i]/60
    #     elif accx[i] > 0 and v != 0:
    #         s += v/60-accx[i]*0.5/3600
    #         v -= accx[i]/60
    # elif a[i] > threshold and b[i] > threshold and c[i] > threshold:
    #     if s != 0:
    #         print(s/32768*16)
    #     s = 0
    #     v = 0

# print(S)
plt.plot(X, Y, '-k')
# plt.plot(S, zore, '*r')
plt.show()