#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *check_cycle - does list contain cycle ?
 *@list: points to linked list to check
 *
 * Return:(0) if no cycle else (1)
 */
int check_cycle(listint_t *list)
{

	listint_t *slow = list;
	listint_t *fast = list;
	if (list == NULL || list->next == NULL)
		return (0);

	while (fast != NULL && fast->next !=  NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}

	}

	return (0);

}
