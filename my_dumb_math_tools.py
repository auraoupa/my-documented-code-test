"""My dumb math tools
This is a collection of math tools i often use. 
This is also an example code to test the automatic building of a code documentation.
"""

import numpy as np
import random as rd

print("This is a collection of math tools i often use.")

def main():
    msg = "Example application: compute ((a+b)*2) where a=3, b=5:"
    print(msg)
    print('RESULT:')
    res_add = add(3,5)
    res_mul = mul(res_add,2)
    print(res_mul)


def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def mul(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def random_number_generator(arg1, arg2):
    """
    Summary: Random number generator in the 0-1 range.

    This is an example function which generates a random number between 0 and 1 from a given seed 
    computed from to input arguments (arg1, arg2). The seed is computed as (arg1+arg2)*(arg1+arg2)

    Parameters
    ----------
    arg1 : int
        argument 1 from which computing the seed for the random generator.
    arg2 : int
        argument 2 from which computing the seed for the random generator.

    Returns
    -------
    int
        Random number between 0 and 1.

    """
    # compute nseed
    nsum = add(arg1,arg2)
    nseed = mul(nsum,nsum)
    
    # initialize randomness with seed nseed
    rd.seed(a=nseed)
    
    return rd.random()


if __name__ == "__main__":
    main()
