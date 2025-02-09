from random import random

def get_total(example, weights, bias):
    total = 0
    for i in range(len(example) - 1):
        total += example[i] * weights[i] + bias
    return total

def threshold(val):
    if val < 0 :
        return 0
    else :
        return 1

def convergence_test(errors):
    for error in errors:
        if error != 0:
            return False
    return True

def perceptron_training() :
    training_examples = [
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0],
    ]

    alpha = 0.1
    bias = -0.1
    weights = []
    for i in range(len(training_examples[0]) - 1):
        weights.append(random() / 10 - 0.05)

    converged = False
    while not converged:
        errors = []
        for example in training_examples:
            total = get_total(example, weights, bias)
            output = threshold(total)
            expected = example[-1]
            error = expected - output
            errors.append(error)
            if error != 0:
                for i in range(len(example) - 1):
                    weights[i] += alpha * error * example[i]
        converged = convergence_test(errors)

    print("Final weights: ", weights)