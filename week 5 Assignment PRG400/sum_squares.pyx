# sum_squares.pyx
def sum_squares(int n):
    cdef int i
    cdef long s = 0
    for i in range(1, n+1):
        s += i*i
    return s
