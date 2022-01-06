import csv
from scipy import spatial as sp


DMC_CSV = "dmc.csv"

dmc_colors = []
with open(DMC_CSV, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for index, row in enumerate(reader):
        dmc_colors.append(
            {
                "index": index,
                "floss": "#" + row["floss#"],
                "description": row["description"],
                "red": int(row["red"]),
                "green": int(row["green"]),
                "blue": int(row["blue"]),
                "hex": "#" + row["hex"],
                "dmc_row": row["row"],
            }
        )

rgb_colors = []
for color in dmc_colors:
    rgb_colors.append((color["red"], color["green"], color["blue"]))

print(dmc_colors)
print(rgb_colors)


# look up the nearest neighbors with k-d tree
def rgb_to_dmc(r, g, b):
    tree = sp.KDTree(rgb_colors)
    # don't need the Euclidean distance only the index
    _, dmc_thread = tree.query((r, g, b))
    return dmc_colors[dmc_thread]


print(rgb_to_dmc(241, 195, 107))
