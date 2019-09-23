from app.services.combination import Combination
from rx import from_list

lists1 = []
expected_output1 = []

lists2 = [[1, 2, 3]]
expected_output2 = [[1], [2], [3]]

lists3 = [
    [1, 2, 3],
    ['A', 'B'],
]
expected_output3 = [[1, 'A'], [1, 'B'], [2, 'A'], [2, 'B'], [3, 'A'], [3, 'B']]

lists4 = [
    [1],
    ['A', 'B'],
    ['#', '$'],
]
expected_output4 = [[1, 'A', '#'], [1, 'A', '$'], [1, 'B', '#'], [1, 'B', '$']]


def tuples_to_lists(_list):
    return [list(_tuple) for _tuple in _list]


def test_py_combine():
    output1 = Combination.py_combine(lists1)
    assert tuples_to_lists(output1) == expected_output1

    output2 = Combination.py_combine(lists2)
    assert tuples_to_lists(output2) == expected_output2

    output3 = Combination.py_combine(lists3)
    assert tuples_to_lists(output3) == expected_output3

    output4 = Combination.py_combine(lists4)
    assert tuples_to_lists(output4) == expected_output4


def test_custom_combine():
    output1 = Combination.custom_combine(lists1)
    assert output1 == expected_output1
    
    output2 = Combination.custom_combine(lists2)
    assert output2 == expected_output2

    output3 = Combination.custom_combine(lists3)
    assert output3 == expected_output3

    output4 = Combination.custom_combine(lists4)
    assert output4 == expected_output4


def test_rx_combine():
    output1 = Combination.rx_combine(lists1)
    assert output1 == expected_output1
    
    output2 = Combination.rx_combine(lists2)
    assert output2 == expected_output2

    output3 = Combination.rx_combine(lists3)
    assert output3 == expected_output3

    output4 = Combination.rx_combine(lists4)
    assert output4 == expected_output4

def test_observable_to_list():
    _list = [1, 2, 3]
    stream = from_list(_list)
    assert  _list == Combination.observable_to_list(stream)
