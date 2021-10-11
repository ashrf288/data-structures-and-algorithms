from insert_array import __version__
from insert_array.insert_array import array_insert_shift

def test_version():
    assert __version__ == '0.1.0'


def test_array_insert_shift():
    assert array_insert_shift([2,4,6,-8], 5)==[2,4,5,6,-8]
