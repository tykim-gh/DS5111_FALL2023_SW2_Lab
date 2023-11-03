import sys
import pytest
import os
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "Training Set [1,1]"
    assert the_perceptron.predict([1,0]) ==  1, "Training Set [1,0]"
    assert the_perceptron.predict([0,1]) ==  1, "Training Set [0,1]"
    assert the_perceptron.predict([0,0]) ==  0, "Training Set [0,0]"

@pytest.mark.xfail(reason="Training Set [1,1] does not yield Prediction: 20")
def test_negative_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  20, "Training Set [1,1]"

@pytest.mark.skip(reason="This test is still a Work In Progress")
def test_always_skip():
    str1 = "Pass this test"
    str2 = "Always"
    assert str1 == str2

@pytest.mark.skipif('ubuntu' not in open('/etc/os-release', 'r').read().lower() if os.path.exists('/etc/os-release') else True, reason="This is not a Linux Ubuntu environment")
def test_conditional_skip():

    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])

    assert total_memory > 0, "Total Memory should be positive"
    assert used_memory >= 0, "Used Memory should be non-negative"
    assert free_memory >= 0, "Free Memory should also be non-negative"

@pytest.mark.parametrize(["trainingset","labels","expected"],[
    ([[1,1],[1,0],[0,1],[0,0]],[1,1,1,0],[1,1,1,0]),
    ([[1,0],[0,0],[1,1],[0,0]],[1,0,1,0],[1,0,1,0]),
    ([[1,1],[0,1],[0,0],[0,0]],[1,0,0,0],[1,0,0,0]),
    ([[0,1],[1,1],[0,0],[1,0]],[0,1,0,1],[0,1,0,1]),
    ([[0,0],[0,1],[1,0],[1,1]],[0,0,0,1],[0,0,0,1])
])
def test_parametrization(trainingset, labels, expected):
    model_perceptron = Perceptron()
    model_perceptron.train(trainingset, labels)
    perceptron_predict = [model_perceptron.predict(dataset) for dataset in trainingset]

    assert perceptron_predict == expected, f"Failed for dataset: {trainingset}, Expected: {expected}, Actual: {perceptron_predict}"
