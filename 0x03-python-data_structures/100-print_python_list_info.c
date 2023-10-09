#include <Python.h>
/**
 *print_python_list_info - prints info about python
 *@p: python object list
 *
 *
 */
void print_python_list_info(PyObject *p)
{

	int size, x, allocate;
	PyObject *object;

	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);

	for (x = 0; x < size; x++)
	{

		printf("Element %d:", x);

		object = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);

	}
}
