import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        [2999, 2.5, 365, 0],
        [2879, 2, 365, 0],
        [2023, 2.5, 252, 0],
        [2545, 1.5, 336, 0],
        [749, 2, 90, 0],
        [899, 2.5, 90, 0],
        [999, 3, 84, 40],
        [719, 2, 84, 0],
        [666, 1.5, 84, 0],
        [533, 2, 56, 0],
        [479, 1.5, 56, 0],
        [299, 2, 30, 0],
        [296, 0, 30, 25],
        [349, 2.5, 30, 0],
        [259, 1.5, 30, 0],
        [239, 1.5, 28, 0],
        [209, 1, 28, 0],
        [399, 3, 28, 6],
        [179, 1, 24, 0],
        [199, 1.5, 23, 0],
        [249, 2, 23, 0],
        [149 + 2, 1, 20, 0],
        [119, 1.5, 14, 0],
        [219, 3, 14, 2],
    ],
    columns=["cost", "data", "dur", "bonus"],
)

df["perday"] = df["cost"] / df["dur"]
df["pergb"] = df["cost"] / (df["data"] * df["dur"] + df["bonus"])
df["perannum"] = df["perday"] * 365
df["numtrans"] = np.ceil(365 / df["dur"])
df = df.astype({"numtrans": int})

print(df)
print(df.sort_values(by=["perday"]))
# print(df.dtypes)
