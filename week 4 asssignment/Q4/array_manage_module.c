#include <Python.h>
#include "array_manager.c"

static PyObject* py_init(PyObject* self, PyObject* args) {
int size;
if (!PyArg_ParseTuple(args, "i", &size)) return NULL;
int* arr = init_array(size);
return PyLong_FromVoidPtr(arr);
}

static PyObject* py_set(PyObject* self, PyObject* args) {
void* ptr;
int index, value;
if (!PyArg_ParseTuple(args, "kii", &ptr, &index, &value)) return NULL;
set_value(ptr, index, value);
Py_RETURN_NONE;
}

static PyObject* py_get(PyObject* self, PyObject* args) {
void* ptr;
int index;
if (!PyArg_ParseTuple(args, "ki", &ptr, &index)) return NULL;
return PyLong_FromLong(get_value(ptr, index));
}

static PyObject* py_free(PyObject* self, PyObject* args) {
void* ptr;
if (!PyArg_ParseTuple(args, "k", &ptr)) return NULL;
free_array(ptr);
Py_RETURN_NONE;
}

static PyMethodDef ArrayMethods[] = {
{"init", py_init, METH_VARARGS, "Initialize array"},
{"set", py_set, METH_VARARGS, "Set array value"},
{"get", py_get, METH_VARARGS, "Get array value"},
{"free", py_free, METH_VARARGS, "Free array"},
{NULL, NULL, 0, NULL}
};

static struct PyModuleDef arraymodule = {
PyModuleDef_HEAD_INIT,
"array_manager",
"Array Manager Module",
-1,
ArrayMethods
};

PyMODINIT_FUNC PyInit_array_manager(void) {
return PyModule_Create(&arraymodule);
}