#include <Python.h>

static PyObject* square(PyObject* self, PyObject* args) {
int num;
if (!PyArg_ParseTuple(args, "i", &num)) {
return NULL;
}
int result = num * num;
return PyLong_FromLong(result);
}

static PyMethodDef SquareMethods[] = {
{"square", square, METH_VARARGS, "Returns square of a number"},
{NULL, NULL, 0, NULL}
};

static struct PyModuleDef squaremodule = {
PyModuleDef_HEAD_INIT,
"squaremodule",
"Square Module",
-1,
SquareMethods
};

PyMODINIT_FUNC PyInit_squaremodule(void) {
return PyModule_Create(&squaremodule);
}