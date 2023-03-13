#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

void print_python_list_info(PyObject *p){
    int size, alloc, i;
    PyObject *obj;

    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] SIze of the Python List = %d", size);
    printf("[*] Allocated = %d", alloc);

    for (i = 0; i < size; i++)
    {
        printf("Element %d", i);
        obj = PyList_GetItem(p, i);

        printf("%s", Py_TYPE(obj)->tp_name);
    }
}
