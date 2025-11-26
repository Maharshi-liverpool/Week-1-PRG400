import array_manager

ptr = array_manager.init(4)
array_manager.set(ptr, 3, 88)
print(array_manager.get(ptr, 3))
array_manager.free(ptr)