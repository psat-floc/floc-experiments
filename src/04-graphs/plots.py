import matplotlib.pyplot as plt
import matplotlib

# Latex
matplotlib.use("pgf")
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

# Ajouter 0 au début et à la fin (pour compléter le polygone)
plt.fill([0, 0.009474532579472257, 0.5150751707774244, 4.367219187239179, 13.781417947136134, 25.494695697290737, 35.61704431497284, 42.96166246637691, 48.34400756321995, 52.229826537883476, 55.40582837560984, 58.10529856056831, 60.47502739968026, 62.67895484831519, 64.72033722773536, 66.70551933470212, 68.60712066493993, 70.46502455107053, 72.3319039503879, 74.0920752302496, 75.79267179767977, 77.26518232322923, 78.58540306753373, 79.77084756051293, 80.64242252723928, 80.64303775662755, 0], color="lightblue")

plt.axis([1, 25, 0, 100])
plt.title("Average uniqueness of cohort paths on 162,541 users\nand 25M movie ratings")
plt.ylabel("Uniqueness (%)")
plt.xlabel("Number of cohorts in the path")
plt.grid(True)
plt.savefig("graph.pgf")

