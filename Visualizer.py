import matplotlib.pyplot as plt

timestamp=input("Ingrese la timestamp de la simulacion que desea visualizar: ")
x = []
y = []
colors = []

with open(f"data/{timestamp}.txt") as f:
    for line in f:
        vals = line.strip().split(' ')
        if len(vals) > 1:
            colors.append(vals[1])

with open(f"data/{timestamp}-0.txt") as f:
    for line in f:
        vals = line.strip().split(' ')
        x.append(float(vals[0]))
        y.append(float(vals[1]))

plt.scatter(x, y, c=colors, s=50)

plt.title("Partículas")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)

plt.show()
