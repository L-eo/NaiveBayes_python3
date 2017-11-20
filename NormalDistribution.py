import math

def solveMuSigma2(List0):   # solving mu and sigma in normal distribution
    Mu = sum(List0) / len(List0)
    sigma2 = 0
    for i in List0:
        sigma2 += (i-Mu)**2
    sigma2 = sigma2/len(List0)
    return Mu, sigma2

def solveP(x, mu=0, sigma2=1):  # solving probability of normal distribution
    P = 1/(math.sqrt(2*math.pi*sigma2)) * math.e**(-(x-mu)**2/(2*sigma2))
    return P
