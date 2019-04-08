def convert(arabicN):
    nForwards = arabicN % 5
    nBackwards = int(arabicN / 5)
        
    return get_forward_slashes(nForwards) + get_backward_slashes(nBackwards)

def get_forward_slashes(n):
    return n * '/'

def get_backward_slashes(n):
    return n * '\\'




