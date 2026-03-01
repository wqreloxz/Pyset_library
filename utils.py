"""
utility functions for pyset library
"""

def compare_sets(set1, set2):
    """compare two sets and return differences"""
    return {
        'union': set1 | set2,
        'intersection': set1 & set2,
        'only_in_first': set1 - set2,
        'only_in_second': set2 - set1,
        'symmetric_diff': set1 ^ set2
    }

def filter_common(data, condition):
    """filter data using condition"""
    if isinstance(data, dict):
        return {k: v for k, v in data.items() if condition(k, v)}
    elif isinstance(data, (list, tuple, set)):
        return type(data)([x for x in data if condition(x)])
    return data

def merge_sets(*sets):
    """merge multiple sets"""
    result = set()
    for s in sets:
        result.update(s)
    return result

def chunk_set(s, chunk_size):
    """split set into chunks"""
    items = list(s)
    return [set(items[i:i + chunk_size]) 
            for i in range(0, len(items), chunk_size)]

def random_sample(s, count):
    """get random sample from set"""
    import random
    items = list(s)
    if count >= len(items):
        return s
    return set(random.sample(items, count))
