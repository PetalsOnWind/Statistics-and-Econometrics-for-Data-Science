#ANOVA (F-TEST) :- 
# The t-test works well when dealing with two groups, but sometimes we want to compare more than two groups at the same time.
#For example, if we wanted to test whether voter age differs based on some categorical variable like race, we have to compare the means of
#  each level or group the variable. 
#The analysis of variance or ANOVA is a statistical inference test that lets you compare multiple groups at the same time.

#------------------------One Way F-test(Anova)------------------------# 
#To tell whether two or more groups are similar or not based on their mean similarity and f-score.
#Example : there are 3 different category of plant and their weight and need to check whether all 3 group are similar or not.
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
print('One-way Anova')
df_anova = pd.read_csv('PlantGrowth.csv')
df_anova = df_anova[['weight','group']]
grps = pd.unique(df_anova.group.values)
d_data = {grp:df_anova['weight'][df_anova.group == grp] for grp in grps}
 
F, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])
print("p-value for significance is: ", p)
if p<0.05:
    print("reject null hypothesis")
else:
    print("accept null hypothesis")

#------------------------------------Two Way F-test-----------------------------------# 
#Two way F-test is extension of 1-way f-test, it is used when we have 2 independent variable and 2+ groups.
#2-way F-test does not tell which variable is dominant. If we need to check individual significance then Post-hoc testing need to be performed.

#e.g: Grand mean crop yield (the mean crop yield not by any sub-group), as well the mean crop yield by each factor, 
# as well as by the factors grouped together.
import statsmodels.api as sm
from statsmodels.formula.api import ols
print('Two-way ANova')
df_anova2 = pd.read_csv("https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/crop_yield.csv")
model = ols('Yield ~ C(Fert)*C(Water)', df_anova2).fit()
print(f"Overall model F({model.df_model: .0f},{model.df_resid: .0f}) = {model.fvalue: .3f}, p = {model.f_pvalue: .4f}")
res = sm.stats.anova_lm(model, typ= 2)
print(res)