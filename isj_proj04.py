#!/usr/bin/env python3

def can_be_a_set_member_or_frozenset(item):
    """ returns item if item can be element of a set, otherwise returns frozenset(item) """
    # check whether the item can be a member of a set
    try:
       s = set()
       s.add(item)
       return item
    except TypeError:
        return frozenset(item)

def all_subsets(lst):
    """ returns powerset of lst  """
    # generate powerset using list comprehension
    return [[lst[j] for j in range(len(lst)) if (i&(1<<j))] for i in range(1<<len(lst))]

def all_subsets_excl_empty(*args, exclude_empty=True):
    """ returns powerset of given input arguments with or without empty set  """
    # adding arguments to list
    lst = [*args]
    # if we want to exclude empty set
    if exclude_empty:
        lst = all_subsets(lst)
        lst.remove([])
        return lst
    else:
        return all_subsets(lst)   
