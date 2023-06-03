library(BSDA) # SIGN.test

##############################################################################
# Two algorithms (X and Y) produce solutions to some maximization problem. 
#
# We run a (one-sided) Hypothesis Test to test whether X is superior to Y.
#
# H0: No algorithm is better (median(Z)=0)
# H1: X is superior to Y (median(Z)>0)
# H2: X and Y differ
#
# We ran both algorithm on a set of instances and got the following results:
##############################################################################

X = c(20, 12, 13, 12, 18, 12, 8, 10, 13, 51, 17)
Y = c(10, 13, 12, 15,  9, 10, 7,  8,  3, 20, 1 )

# Auxiliary Variable: Z>0 iff X is superior to Y
Z = X - Y

##############################################################################
# We observe that many entries of Z are positive, which speaks against H0. 
# 
# Question: How many values of Z must be positive in order to reject H0? 
#
# Answer: It has to be "extremely" unlikely that the observed values are 
# produced under the assumption that H0 is true.
##############################################################################

# significance level
alpha = 0.05

# number of data points
n = length(Z)

##############################################################################
# 1. Sign Test. 
#
# Test statistic S := number of positive entries in Z.
#
# What is a test statistic? It is a function that maps the samples Z to some
# real number on which we decide whether we reject H0.
##############################################################################

# calculate test statistic
S = sum(Z>0)

# plot distribution of the test statistic under H0 (binomial distribution)
data = dbinom(x=0:n, size=n, prob=0.5)
names(data) = 0:n

# create colored bars
cols <- rep("grey", n + 1)
cols[S+1:n] <- "red"

# plot histogram
barplot(data, col=cols, xlab="k", ylab="Pr(S=k)")

##############################################################################
# p-value: The probability of finding a value of S that is "at least as
# extreme" as the observed one. Thus, sum up the probability of the red bars.
##############################################################################

p = sum(dbinom(S:n, size=n, prob=0.5))

##############################################################################
# As p < alpha, we reject H0 in favor of H1.
# Consequently, we conclude that X is superior to Y.
##############################################################################

# and now the same in one line
SIGN.test(Z, alternative = "greater")

##############################################################################
# Wilcoxon Rank Test:
#
# 1. Ignore all entries with Z=0
# 2. Calculate ranks R of the absolute values |Z|
# 3. Average identical ranks
#
# Test statistic: W+ := sum of ranks of positive Z
##############################################################################

# calculate ranks (ties are averaged)
R = rank(abs(Z))

# calculate test statistic
W = sum(R[Z>0])

# plot distribution of the test statistic under H0 (normal approximation for n>20)
x = seq(0, 80)  
mean = n*(n+1)/4
sd = sqrt(n*(n+1)*(2*n+1)/24)
y = dnorm(x=x, mean = mean, sd = sd)
plot(x, y, type="l", xlab="k", ylab="Pr(W+=k)")
abline(v=W)

# calculate p-value: accumulate all entries right of W+
p = sum(y[x>=W])

##############################################################################
# As p < alpha, we reject H0 in favor of H1.
# Consequently, we conclude that X is superior to Y.
##############################################################################

# and now all in one line
wilcox.test(Z, alternative = "greater")

