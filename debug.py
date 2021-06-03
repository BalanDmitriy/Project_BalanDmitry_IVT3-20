from solution.transposition import Transposition


structure = {
    "name": "main",
    "children": {
        "first": {
            "count": [1, 2, 3, 4],
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

tp = Transposition()
flat_array = tp.struct_to_array(structure)
print(flat_array)

new_structure = tp.array_to_struct(flat_array)
print(new_structure)
