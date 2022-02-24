#“how far is a value from the mean” 
#“how likely is a value this far from the mean to be from the same group of observations?”
import numpy as np
tokaji_avg = np.average(tokaji)
lambrusco_avg = np.average(lambrusco)
tokaji_std = np.std(tokaji)
lambrusco = np.std(lambrusco)
# Let's see what the results are
print("Tokaji: ", tokaji_avg, tokaji_std)
print("Lambrusco: ", lambrusco_avg, lambrusco_std)
# Tokaji: 90.9 2.65015722804
# Lambrusco: 84.4047619048 1.61922267961

z = (tokaji_avg - lambrusco_avg) / lambrusco_std
#4.0113309781438229
# We'll bring in scipy to do the calculation of probability from the Z-table
import scipy.stats as st
st.norm.cdf(z)
# 0.99996981130231266
# We need the probability from the right side, so we'll flip it!
1 - st.norm.cdf(z)
# 3.0188697687338895e-05
