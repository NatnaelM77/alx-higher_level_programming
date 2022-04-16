#include <Python.h>

/**
 * print_item_info - Display the information of items of a python list
 *
 * @prmItem: item of a python object
 * @prmItemIndex: item index
 */

void print_item_info(PyObject *prmItem, int prmItemIndex)
{
	char *itemName;

	itemName = (char *)Py_TYPE(prmItem)->tp_name;

	printf("Element %d: %s\n", prmItemIndex, itemName);
}	

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: py object
 */

void print_python_list_info(PyObject *p)
{
	int itemIndex, objAllocatedNb = 0;
	PyObject *item;
	Py_ssize_t objListSize = 0;

	/* Check if item list is not empty */
	if (PyList_Check(p))
	{
		objListSize = PyList_Size(p);
		objAllocatedNb = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %d\n", (int) objListSize);
		printf("[*] Allocated = %d\n", objAllocatedNb);

		for (itemIndex = 0; itemIndex < objListSize; itemIndex++)
		{
			item = PyList_GetItem(p, itemIndex);
			print_item_info(item, itemIndex);
		}
	}
}
