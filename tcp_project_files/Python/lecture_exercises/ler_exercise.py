import pandas as pd

data = {
    "G_ratio": [1, 0.9, 0.67, 0.5, 0.33, 0.1, 0],
    "B_ratio": [0, 0.1, 0.33, 0.5, 0.67, 0.9, 1],
    "yield": [1368, 1300, 1393, 1579, 1498, 1469, 1535]
}
df = pd.DataFrame(data)

# Monocrop yield values

G_mono = 1368  # Yield for green monocrop
B_mono = 1535  # Yield for blue monocrop

df["partial_yield_G"] = df["yield"] * df["G_ratio"]
df["partial_yield_B"] = df["yield"] * df["B_ratio"]

df["LER_G"] = df["partial_yield_G"] / G_mono
df["LER_B"] = df["partial_yield_B"] / B_mono
df["LER_total"] = df["LER_G"] + df["LER_B"]

print(df[["G_ratio", "B_ratio", "yield", "LER_G", "LER_B", "LER_total"]].round(3))

