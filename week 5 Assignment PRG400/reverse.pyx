# reverse.pyx
def reverse_string(str s):
    cdef int n = len(s)
    cdef char[:] result = s.encode()
    cdef int i
    cdef char temp
    for i in range(n // 2):
        temp = result[i]
        result[i] = result[n - i - 1]
        result[n - i - 1] = temp
    return result.tobytes().decode()
