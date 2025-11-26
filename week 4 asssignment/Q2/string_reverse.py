import ctypes

lib = ctypes.CDLL('./libstringlib.dylib')

lib.reverse_string.restype = ctypes.c_char_p
lib.reverse_string.argtypes = [ctypes.c_char_p]

result = lib.reverse_string(b"Hello Class")
print(result.decode())