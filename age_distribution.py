import matplotlib.pyplot as plt

# Age group data (example population counts)
age_groups = ['0-20', '21-40', '41-60', '60+']
population = [52, 70, 45, 20]

colors = ['gold', 'dodgerblue', 'mediumseagreen', 'tomato']

plt.figure(figsize=(8,5))

plt.bar(age_groups, population, color=colors, edgecolor='black')

plt.title("Population Distribution by Age Groups", fontsize=14)
plt.xlabel("Age Groups")
plt.ylabel("Population Count")

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig("population_bar_chart.png")
plt.show()
