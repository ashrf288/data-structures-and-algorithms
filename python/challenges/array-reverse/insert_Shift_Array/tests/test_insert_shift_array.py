from insert_shift_array import __version__
from insert_shift_array.insert_shift_array import array_insert_shift

def test_version():
    assert __version__ == '0.1.0'


def test_array_insert_shift():
    #input
     arr=[2,4,6,-8]
     value= 5
    #output
     output= [2,4,5,6,-8]
     assert  array_insert_shift(arr,value)==output