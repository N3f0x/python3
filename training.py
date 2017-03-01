import matplotlib.pyplot as plt
day = [1, 2, 3, 4,]
knee_bend = [15, 20, 25, 0,]

plt.scatter(day, knee_bend)

plt.title("Träningsdagbok")
plt.xlabel("Dag")
plt.ylabel("Antal knäböj x3")
plt.xticks(day)
plt.yticks(knee_bend)

plt.show()
