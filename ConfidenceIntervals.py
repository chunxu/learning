#Calculate Confidence Intervals

#A confidence interval for a mean is a range of values that is likely to contain a population mean with a certain level of confidence.
'''
Confidence Interval = x  +/-  t*(s/√n)
where:

x: sample mean
t: t-value that corresponds to the confidence level
s: sample standard deviation
n: sample size
'''
#with a small sample (n <30), we can use the t.interval() function

import numpy as np
import scipy.stats as st

#define sample data
data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]
#create 95% confidence interval for population mean weight
st.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(data), scale=st.sem(data)) 
#(16.758, 24.042)

#create 99% confidence interval for same sample
st.t.interval(alpha=0.99, df=len(data)-1, loc=np.mean(data), scale=st.sem(data)) 
#(15.348, 25.455)


#with larger samples (n≥30), we can assume that the sampling distribution of the sample mean is normally distributed  and can instead use the norm.interval() function from the scipy.stats library.
import numpy as np
import scipy.stats as st

#define sample data
np.random.seed(0)
data = np.random.randint(10, 30, 50)
#create 95% confidence interval for population mean weight
st.norm.interval(alpha=0.95, loc=np.mean(data), scale=st.sem(data))
#(17.40, 21.08)



