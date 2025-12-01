# dot_product.pyx
import numpy as np
cimport numpy as np

def dot(np.ndarray[np.double_t, ndim=1] a, np.ndarray[np.double_t, ndim=1] b):
    cdef int n = a.shape[0]
    cdef int i
    cdef double s = 0
    for i in range(n):
        s += a[i] * b[i]
    return s
