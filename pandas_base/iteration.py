# Pandas rows iteration benchmark

import numpy as np
import pandas as pd


rows = 100000
df = pd.DataFrame(
    {
        "a": np.random.normal(size=(rows)),
        "b": np.random.normal(size=(rows)),
        "c": np.random.randint(0, 5, size=(rows)),
    }
)


def iteration_itertuples():
    a = 0
    for row in df.itertuples():
        a += row[1] + row[2] + row[3]  # row[0] is the index
    return a


def iteration_zip():
    a = 0
    for row in zip(df["a"], df["b"], df["c"]):
        a += row[0] + row[1] + row[2]
    return a


def iteration_range():
    a = 0
    for i in range(df.shape[0]):
        a += df["a"].values[i] + df["b"].values[i] + df["c"].values[i]
    return a


# with rows = 10:
# - 689 µs ± 76.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# - 40.3 µs ± 1.19 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# - 90.5 µs ± 3.21 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
#
# with rows = 1000:
# - 2.34 ms ± 360 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# - 480 µs ± 35.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# - 11.1 ms ± 461 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
#
# with rows = 10000:
# - 11 ms ± 504 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# - 4.34 ms ± 126 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# - 107 ms ± 3.87 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
#
# with rows = 100000:
# - 114 ms ± 13.6 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# - 48.5 ms ± 5.71 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
# - 1.3 s ± 160 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
#
# SUMMARY: Always Use zip, unless it is necessary to get the index, then use itertuples
