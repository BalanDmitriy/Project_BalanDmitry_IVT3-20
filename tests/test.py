import pytest
from solution.transposition import Transposition


structure = {
    "name": "main",
    "children": {
        "first": {
            "count": 1,
            "children": {
                "third": {
                   "count": 3
                }
            }
        },
        "second": {
            "count": 2
        },
    }
}


def test_flat_array():
    tp = Transposition()
    assert tp.struct_to_array(structure)

def test_structure_back():
    tp =Transposition()
    assert tp.array_to_struct(tp.struct_to_array(structure))
