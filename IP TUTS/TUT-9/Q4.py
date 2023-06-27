# Write a recursive function that takes a list that may contain more lists in it and returns a list with all values flattened

def flatten(arr):
    res = []
    for i in arr:
        if isinstance(i, list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res
