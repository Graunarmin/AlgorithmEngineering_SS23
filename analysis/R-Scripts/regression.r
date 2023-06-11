######################################################
# Example on Linear and Multiple Regression
######################################################

# create data points
x = c(1,2,3,4)
y = c(1,1,3,8)

# plot data points
plot(x, y, ylim=c(-3,10))
grid()

######################################################
# Linear Regression: y = beta*x + alpha
######################################################

lm1 = lm(y ~ x)

# extract coefficients
alpha = lm1$coefficients[1]
beta = lm1$coefficients[2]

# plot line
xx = seq(0, 5, 0.1)
yy = beta*xx + alpha
lines(xx, yy, col="grey")

# calculate regression error
sum((y - (beta*x + alpha))^2)

######################################################
# Linear regression: y = C*x^k
#                log y = log C + k * log x
#                 y1   = c + k * x1
######################################################

x1 = log(x)
y1 = log(y)
lm2 = lm(y1 ~ x1)

# extract coefficients
C = exp(lm2$coefficients[1])
k = lm2$coefficients[2]

# plot curve
xx = seq(0, 5, 0.1)
yy = C*xx^k
lines(xx, yy, col='red')

# calculate regression error
sum((y - (C*x^k))^2)

######################################################
# Multiple Regression: y = a + b*x*log(x) + c*exp(x)
#                        = a + b*x1 + c*x2
######################################################

x1 = x*log2(x)
x2 = exp(x)
lm3 = lm(y ~ x1 + x2)

# extract coefficients
a = lm3$coefficients[1]
b = lm3$coefficients[2]
c = lm3$coefficients[3]

# plot curve
xx = seq(0, 5, 0.1)
yy = a + b*xx*log2(xx) + c*exp(xx)
lines(xx, yy, col="blue")

# calculate regression error
sum((y - (a + b*x*log2(x) + c*exp(x)))^2)

