library(BSDA) # SIGN.test

##############################################################################
# Two algorithms D (average distance) and G (greedy) produce solutions
# to the CVR problem.
#
# We run a (one-sided) Hypothesis Test to test whether D is superior to G.
#
# H0: No algorithm is better (median(Z)=0)
# H1: X is superior to Y (median(Z)>0)
# H2: X and Y differ
#
# We ran both algorithms on 11 instances and got the following results:
##############################################################################

D <- c(215574, 137389, 43979, 34909, 19708, 47666, 40818, 58779, 121950, 351177, 88177)
G <- c(214037, 136515, 43852, 35360, 21812, 47490, 41404, 59372, 119462, 351618, 87106)

# Auxiliary Variable: Z>0 iff D is superior to G
Z <- D - G

print("The Differences between D and G (=Z) are:")
print(Z)
##############################################################################
# We observe that 6 entries of Z are positive and 5 are negative,
# which speaks for H0.
# 
# Question: How many values of Z must be positive in order to reject H0? 
#
# Answer: It has to be "extremely" unlikely that the observed values are 
# produced under the assumption that H0 is true.
##############################################################################

# significance level
alpha <- 0.05

# number of data points
n <- length(Z)

##############################################################################
# 1. Sign Test. 
#
# Test statistic S: number of positive entries in Z.
#
# The test statistic is a function that maps the samples Z to some
# real number on which we decide whether we reject H0.
##############################################################################

# calculate test statistic
S <- sum(Z>0)

plot_test_statistic <- function (n){
  # plot distribution of the test statistic under H0 (binomial distribution)
  data <- dbinom(x=0:n, size=n, prob=0.5)
  names(data) <- 0:n

  # create colored bars
  cols <- rep("grey", n + 1)
  cols[S+1:n] <- "red"

  # plot histogram
  barplot(data, col=cols, xlab="k", ylab="Pr(S=k)")
}

plot_test_statistic(n)

##############################################################################
# p-value: The probability of finding a value of S that is "at least as
# extreme" as the observed one. Thus, sum up the probability of the red bars.
##############################################################################
sign_test <- function (S, n){
  p <- sum(dbinom(S:n, size=n, prob=0.5))
  print(paste0("The p-Value for the Sign Test is ", p))
}

sign_test(S,n)
##############################################################################
# As p > alpha, we accept H0.
# Consequently, we conclude that G and D are equally good.
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

wilcoxon_test <- function (Z, n){
  # calculate ranks (ties are averaged)
  R <- rank(abs(Z))

  # calculate test statistic
  W <- sum(R[Z>0])

  # plot distribution of the test statistic under H0 (normal approximation for n>20)
  x <- seq(0, 80)
  mean <- n*(n+1)/4
  sd <- sqrt(n*(n+1)*(2*n+1)/24)
  y <- dnorm(x=x, mean = mean, sd = sd)
  plot(x, y, type="l", xlab="k", ylab="Pr(W+=k)")
  abline(v=W)

  # calculate p-value: accumulate all entries right of W+
  p <- sum(y[x>=W])
  print(paste0("The p-value for the wilcoxon rank test is ", p))
}

#wilcoxon_test(Z,n)

##############################################################################
# As p > alpha, we accept H0.
# Consequently, we conclude that D and G are equally good..
##############################################################################

# and now all in one line
#wilcox.test(Z, alternative = "greater")

