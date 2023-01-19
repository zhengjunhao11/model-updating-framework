import os

import numpy as np
from functools import lru_cache
from types import MethodType, FunctionType
import warnings
import sys
import multiprocessing



def func_transformer(func):
    def func_transformed(X):
        from multiprocessing import Pool
        with multiprocessing.Pool(12) as pool:
            return np.array(pool.map(func, X,chunksize=1))


    return func_transformed



