import numpy as np
from scipy import stats
from scipy.stats import gmean, hmean

# Data sets
X = np.array([3, 1, 2, 3, 1, 4, 3, 3])
Y = np.array([1, 4, 3, 1, 1, 3])
Z = np.array([3, 3, 1, 4, 2, 1, 4, 2])

# Mean (a)
mean_X = np.mean(X)
mean_Y = np.mean(Y)
mean_Z = np.mean(Z)

# Harmonic mean (b)
harmonic_mean_X = hmean(X)
harmonic_mean_Y = hmean(Y)
harmonic_mean_Z = hmean(Z)

# Geometric mean (c)
geometric_mean_X = gmean(X)
geometric_mean_Y = gmean(Y)
geometric_mean_Z = gmean(Z)

# Arithmetic-Geometric mean (d)
def ag_mean(data):
    return (np.mean(data) + gmean(data)) / 2

ag_mean_X = ag_mean(X)
ag_mean_Y = ag_mean(Y)
ag_mean_Z = ag_mean(Z)

# Arithmetic-Harmonic-Geometric mean (e)
def ahg_mean(data):
    return (np.mean(data) + hmean(data) + gmean(data)) / 3

ahg_mean_X = ahg_mean(X)
ahg_mean_Y = ahg_mean(Y)
ahg_mean_Z = ahg_mean(Z)

# Median (f)
median_X = np.median(X)
median_Y = np.median(Y)
median_Z = np.median(Z)

# Printing results
print(f"Mean: μ(X) = {mean_X}, μ(Y) = {mean_Y}, μ(Z) = {mean_Z}")
print(f"Harmonic Mean: μh(X) = {harmonic_mean_X}, μh(Y) = {harmonic_mean_Y}, μh(Z) = {harmonic_mean_Z}")
print(f"Geometric Mean: μg(X) = {geometric_mean_X}, μg(Y) = {geometric_mean_Y}, μg(Z) = {geometric_mean_Z}")
print(f"Arithmetic-Geometric Mean: μag(X) = {ag_mean_X}, μag(Y) = {ag_mean_Y}, μag(Z) = {ag_mean_Z}")
print(f"Arithmetic-Harmonic-Geometric Mean: μahg(X) = {ahg_mean_X}, μahg(Y) = {ahg_mean_Y}, μahg(Z) = {ahg_mean_Z}")
print(f"Median: μi(X) = {median_X}, μi(Y) = {median_Y}, μi(Z) = {median_Z}")
