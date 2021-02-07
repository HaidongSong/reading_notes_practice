import matplotlib.pyplot as plot

squares = [i**2 for i in range(1, 100)]
print(squares)

fig, ax = plot.subplots()
ax.plot(squares)
plot.show()