import matplotlib as mpl
import matplotlib.pyplot as plt

idades = [22, 65, 45, 55, 21, 22, 34, 42, 41, 4, 99, 101, 120, 130, 111, 115, 80, 75, 54, 44, 64, 13, 18, 48, 59]

ids = [x for x in range(len(idades))]

print(ids)

plt.bar(ids, idades)
plt.show()

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(idades, bins, histtype = 'bar', rwidth = 0.8)
plt.show()

plt.hist(idades, bins, histtype = 'stepfilled', rwidth = 0.8)
plt.show()