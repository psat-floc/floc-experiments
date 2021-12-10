import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sys

fmt = "pgf"

# Latex
matplotlib.use(fmt)
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "font.family": "serif",
    "text.usetex": True,
    "pgf.rcfonts": False,
})

# ou
plt.rcParams.update({
    "text.usetex": True,
})

filename = sys.argv[1]
plotname = filename[:-3] + fmt

# Ajouter 0 au début et à la fin (pour compléter le polygone)
data = pd.read_csv(filename, header=1).to_numpy().flatten()
plt.fill(data, color="lightblue")

plt.axis([1, 25, 0, 100])
plt.title("Average uniqueness of cohort paths on X users\nand Y movie ratings")
plt.ylabel("Uniqueness (%)")
plt.xlabel("Number of cohorts in the path")
plt.grid(True)
plt.savefig(plotname)

