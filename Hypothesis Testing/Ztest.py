#-----------------------------------------------Z-Test---------------------------------------------------#
#Z test is used if:
#Your sample size is greater than 30. Otherwise, use a t test.
#Data points should be independent from each other. In other words, one data point isn’t related or doesn’t affect another data point.
#Your data should be normally distributed. However, for large sample sizes (over 30) this doesn’t always matter.
#Your data should be randomly selected from a population, where each item has an equal chance of being selected.
#Sample sizes should be equal if at all possible.

#-----------One Sample Z-test-----------#
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
df = pd.read_csv("blood_pressure.csv")

ztest ,pval = stests.ztest(df['bp_before'], x2=None, value=156)
print('One-sample z-test')
print(float(pval))
if pval<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

#-----------Two Sample Z-test-----------#
#Two-sample Z test- Just check two independent data groups and decide whether sample mean of two group is equal or not.
#H0 : mean of two group is 0
#H1 : mean of two group is not 0
#Example : we are checking in blood data after blood and before blood data.

ztest ,pval1 = stests.ztest(df['bp_before'], x2=df['bp_after'], value=0,alternative='two-sided')
print('Two-sample z-test')
print(float(pval1))
if pval1<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")
