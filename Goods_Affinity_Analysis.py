import numpy as np
from collections import defaultdict
from operator import itemgetter

# @Auther: Chulong Li

X = np.loadtxt("affinity_dataset.txt")
n_samples, n_features =X.shape
print("This dataset has {0} samples and {1} kinds of goods".format(n_samples, n_features))
valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurances = defaultdict(int)
for sample in X:
    for premise in range(n_features):
        if sample[premise] != 0:
            num_occurances[premise] += 1
            for conclusion in range(n_features):
                if premise != conclusion:
                    if sample[conclusion] == 1:
                        valid_rules[(premise, conclusion)] += 1
                    else:
                        invalid_rules[(premise, conclusion)] += 1

support = valid_rules
features = ["bread", "milk", "cheese", "apples", "bananas"]
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = valid_rules[rule] / num_occurances[premise]

def print_rule(premise, conclusion, support, confidence, features):
    print("Rule: If someone buys {0}, he/she will also buy {1}".format(features[premise], features[conclusion]))
    print(" - Support: {0}".format(support[(premise, conclusion)]))
    print(" - Confidence: {0:.3f}".format(confidence[(premise, conclusion)]))

sorted_support = sorted(support.items(), key = itemgetter(1), reverse = True)
for index in range(5):
    print("Rule #{0}".format(index + 1))
    premise, conclusion = sorted_support[index][0]
    print_rule(premise, conclusion, support, confidence, features)
