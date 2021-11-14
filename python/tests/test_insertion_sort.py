from challenges.insertion_sort.insertion_sort import insertion_Sorts


def test_insertion_error():
    assert insertion_Sorts([8,4,23,42,16,15])==[4,8,15,16,23,42]
def test_insertion_error1():
    assert insertion_Sorts([20,18,12,8,5,-2])==[-2, 5, 8, 12, 18, 20]
def test_insertion_error2():
    assert insertion_Sorts([5,12,7,5,5,7])==[5, 5, 5, 7, 7, 12]
def test_insertion_error3():
    assert insertion_Sorts([2,3,5,7,13,11])==[2, 3, 5, 7, 11, 13]