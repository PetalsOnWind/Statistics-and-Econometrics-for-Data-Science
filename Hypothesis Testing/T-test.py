#-----------------------------------------T-test---------------------------------#
#A t-test is a type of inferential statistic which is used to determine if there
#is a significant difference between the means of two groups which may be related in certain features.

#T-test has 2 types : 1. one sampled t-test 2. two-sampled t-test.
#One sample t-test : The One Sample t Test determines whether the
#sample mean is statistically different from a known or hypothesised population mean. The One Sample t Test is a parametric test.

from scipy.stats import ttest_1samp
import numpy as np

#10 ages and you are checking whether avg age is 30 or not.
#H0: The average age is 30
#H1: The average age is not 30.
ages = np.array([32,34,29,29,22,39,38,37,38,36,30,26,22,22])
print(ages)
#mean of the age 
ages_mean = np.mean(ages)
print(ages_mean)
#One Sample t-test
tset, pval = ttest_1samp(ages, 30)
print('p-values',pval)
if pval < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")

