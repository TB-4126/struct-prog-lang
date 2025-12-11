//cevaluator.c
//Thomas Bond
//2025-12-4

#define PY_SSIZE_T_CLEAN //uses py_ssize_t for memory size instead of int
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

//Evaluate Function
PyObject* evaluate(PyObject *self, PyObject *args) {
   PyDictObject *ast = 0, *environment = 0; //Arguments Declaration
   void* sts;                              //The value that will be returned at the end of the function

   //Parses the arguments, checks if the arguments are the correct type
   if (!PyArg_ParseTuple(args, "O|O", &ast, &environment)) { return NULL; }
   //Verifies the arguments received are dictionaries;
   assert(PyDict_Check(ast));
   //Checks if environment is defined and if it is the correct type
   if (environment != 0) {
      assert(PyDict_Check(environment));
   }
   else { environment = PyDict_New(); }
   
   PyObject* string_check = PyLong_FromLong(10);
   if(PyDict_Contains(ast,string_check)) {
      printf("Should return true if we managed to update the dependencies.\n");
   }


   sts = 0;
   return PyLong_FromLong(sts);
}

//Defines the methods for the module
PyMethodDef evaluator_methods[] = {
   { "evaluate", evaluate, METH_VARARGS, "For now prints to console." },
   {NULL, NULL, 0, NULL} //Required for proper functionality
};

//Defines the module structure
struct PyModuleDef cevaluator_module = {
   PyModuleDef_HEAD_INIT,
   "cevaluator",
   NULL,
   -1,
   evaluator_methods
};

//Initializes the module
//PyMODINIT_FUNC declares the return as PyObject* and declares any necessary linkages
PyMODINIT_FUNC PyInit_cevaluator(void) { return PyModule_Create(&cevaluator_module); }
