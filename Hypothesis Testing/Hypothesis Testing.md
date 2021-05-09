# What is Hypothesis Testing?

Hypothesis testing is a statistical method that is used in making statistical decisions using experimental data.
It evaluates two mutually exclusive statements about a population to determine which statement is best supported by the sample data.

## Important Parameters:

**Null Hypothesis** : 
1) A statement about a population paramter.
2) Contains: '=', '<=', '>='
3) We consider Null Hypothesis to be true, to decide whether to reject or accept the alternative hypothesis.

**Alternative Hypothesis** :
1) A statement that directly contardicts the null hypothesis.
2) COntains : 'Not equal to', '>', '<'

**Level Of Significance**:
Degree of significance in which we accept or reject the null-hypothesis. (Ussually taken as 5%, which means your output should be 95% confident to give similar kind of result in each sample.)

**Type I error:**
 When we reject the null hypothesis, although that hypothesis was true. (alpha)

**Type II error :**
When we accept the null hypothesis but it is false. (Beta)

**One tailed test :-**
 A test of a statistical hypothesis , where the region of rejection is on only one side of the sampling distribution , is called a one-tailed test.

 A box has ≥ 40 chocolates.

**Two-tailed test :-** 
A two-tailed test is a statistical test in which the critical area of a distribution is two-sided and tests whether a sample is greater than or less than a certain range of values. If the sample being tested falls into either of the critical areas, the alternative hypothesis is accepted instead of the null hypothesis.

A box != 40 chocolates.

**P-value** 
P-value or the calculated probability, is the probability of finding the observed, or more extreme, results when the null hypothesis (H0) of a study question is true.
If your P value is less than the chosen significance level then you reject the null hypothesis i.e. accept that your sample gives reasonable evidence to support the alternative hypothesis. 

Example : You have a coin and you don’t know whether that is fair or tricky so let’s decide null and alternate hypothesis
H0 : The coin is a fair coin.
H1 : The coin is a tricky coin.
Level of significance :  95%
alpha = 5% or 0.05

Now let’s toss the coin and calculate p- value ( probability value).
Toss a coin 1st time and result is tail- P-value = 50% (as head and tail have equal probability)
Toss a coin 2nd time and result is tail, now p-value = 50/2 = 25%
and similarly we Toss 6 consecutive time and got result as P-value = 1.5% but we set our significance level as 95% means 5% error rate we allow and here we see we are beyond that level (p-value < alpha) i.e. our null- hypothesis does not hold good so we need to reject the null hypothesis and propose that this coin is a tricky coin which is actually.

Some of the widely used hypothesis tests and codes are discussed.



