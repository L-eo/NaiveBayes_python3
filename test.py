# the first row is title and the first column is classs in the LearnSample
TrainingSample = [['sex', 'height(feet)', 'weight(lbs)', 'footSize(inches)'],
               ['male', 6, 180, 12],
               ['male', 5.92, 190, 11],
               ['male', 5.58, 170, 12],
               ['male', 5.92, 165, 10],
               ['female', 5, 100, 6],
               ['female', 5.5, 150, 8],
               ['female', 5.42, 130, 7],
               ['female', 5.75, 150, 9]]
TestSample = [6, 130, 8]

import NaiveBayes as Bayes
import math

Bayes.NaiveBayes(TestSample, TrainingSample)