import copy
import NormalDistribution as ND
import math

def SolveDisperseP(element, List0):
    count = 0
    for i in List0:
        if(element == i):
            count += 1
    return count/len(List0)


def NaiveBayes(testSample0, TrainingSample0):
    testSample = copy.deepcopy(testSample0)
    TrainingSample = copy.deepcopy(TrainingSample0)

    titleP = {}  # solve the probability of each class
    TrainingSample = TrainingSample[1:]
    for i in TrainingSample:
        if(i[0] not in titleP):
            column = []
            for ele in TrainingSample:
                column.append(ele[0])
            titleP[i[0]] = [SolveDisperseP(i[0], column)]

    for i in titleP:  # solve every Property's probility of each class
        for j in range(1,len(TrainingSample[1])):
            ClassProperty = []
            for k in TrainingSample:
                if(i == k[0]):
                    ClassProperty.append(k[j])
            [mu, sigma2] = ND.solveMuSigma2(ClassProperty)
            titleP[i].append(ND.solveP(testSample[j-1], mu, sigma2))

    MaxValue = float("-inf")
    for i in titleP:  # change element's product to summation of logarithmic,
        LogSum = 0    # which can prevent error caused by too small value.
        for j in titleP[i]:
            LogSum += math.log(j)
        titleP[i] = LogSum
        if(LogSum > MaxValue):
            MostProbility = i
    print(MostProbility)


    