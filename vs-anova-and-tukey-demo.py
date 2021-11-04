'''
Goal: demo how to perform ANOVA One-Way test in Python
Also demo how to use Tukey test to tell which groups have statistically significant averages

Author: Vincent Stevenson
'''

import scipy.stats as stats # for ANOVA one-way
from statsmodels.stats.multicomp import pairwise_tukeyhsd # for Tukey test if ANOVA rejects Null Hypo.

group_a = [1,1,1]
group_b = [2,2]
group_c = [3,3]
group_d = [5,5]

groups = [group_a, group_b, group_c, group_d]

# f_val, p_val = stats.f_oneway(*groups)


data_1d = [1, 1, 1, 2, 2, 3, 3, 5, 5]
groups_1d = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']
tukey_test = pairwise_tukeyhsd(data_1d, groups_1d, alpha=0.05)
print(tukey_test)
print()