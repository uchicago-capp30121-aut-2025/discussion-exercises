def only_negatives(lst):
    """
    Make a new list with the negative numbers from the input list.

    Args:
        lst (List[int]): a list of integers

    Returns (List[int]): a list with the negative numbers from the input
    """

    # Replace None with the appropriate return value 
    return [item for item in lst if item < 0]

def lst_min_idx(lst):
    """
    Find the index of the minimum value in the list
    Assumes the list has at least one element and
    that the values are unique.

    Args:
      lst (List[int]): the values of interest

    Return (int): the index of the minimum value in the
    list.
    """
    assert len(lst) > 0

    # Your Code Goes Here
    min_value = min(lst)
    min_idx = lst.index(min_value)

    # Replace None with the appropriate return value
    return min_idx


def identify_values(lst):
    """
    Given a list of integers, generate a new list where the ith entry is
    "neg" if the ith entry of lst was less than zero, "zero", if it was
    zero, and "pos" was greater than zero.

    Args:
       lst (List[int]): the list of interest

    Returns (List[int]): a new list where the ith entry is "neg", "zero", "pos"
      depending on the ith value in the original list.
    """
    # Your Code Goes Here

    result = []
    for item in lst:
        if item < 0:
            result.append("neg")
        elif item == 0:
            result.append("zero")
        else:
            result.append("pos")


    # Replace None with the appropriate return value
    return result


def split_by_identity(lst):
    """
    Give a list, construct a new list with three sublists, where the first sublist
    contains the indexes of all the negative values, in the input list, the second
    sublist contains the indexes of all the occurrences of zero in the input list,
    and the third sublist contains the index of all the positive values in the
    input list.

    Args:
        lst (List[int]): a list of integers

    Returns: List(List[int]): a list of length three, where each element is itself
      a list.  The first sublist contains the indexes of the negative values, the
      second contains the indexes of the zeros, and the third contains the indexes
      of the positive value.
    """
    # Your Code Goes Here

    result = [[], [], []]
    for ix, value in enumerate(lst):
        if value < 0:
            result[0].append(ix)
        elif value == 0:
            result[1].append(ix)
        else:
            result[2].append(ix)

    # Replace None with the appropriate return value
    return result
