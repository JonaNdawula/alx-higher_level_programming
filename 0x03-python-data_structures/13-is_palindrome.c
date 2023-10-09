#include "lists.h"
/**
 *is_palindrome - a function in C that checks if list is a palindrome.
 *
 *@head: points to head of limked list
 *
 * Return: if is palindrome 1 if not 0
 */
int is_palindrome(listint_t **head)
{
	int length = 0, mid = length / 2, index;

	listint_t *current = *head, *prev = NULL, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		length++;
		current = current->next;

	}

	for (index = 0; index < mid; index++)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	if (length % 2 != 0)
		current = current->next;

	while (prev != NULL && current != NULL)
	{
		if (prev->n != current->n)
		{
			return (0);
		}
		prev = prev->next;
		current = current->next;
	}

	return (1);
}
