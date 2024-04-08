

import matplotlib.pyplot as plt

# Laden der Daten
from load_data import load_data
from sort import bubble_sort

power = load_data("activity.csv")
print(power)
power = power["PowerOriginal"]
sorted_power_W = bubble_sort(power)
#print(sorted_power_W)
# Plotte mir eine Liste mit Matplotlib
plt.plot(sorted_power_W[::-1])
plt.xlabel('Dauerlinie')
plt.ylabel('P in W')
plt.savefig("figures\power_curve3.png")


#save_figure('power_curve.png')
#plt.show()
