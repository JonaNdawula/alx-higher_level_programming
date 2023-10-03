#include "lists.h"

/**
 *listint_t *insert_node - a function in C that inserts a number in list
 *@head: points to head of linked list
 *@number: number to insert
 *
 *Return: pointer to new node else NULL
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_position;


	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_position = *head;

	while (current_position != NULL && current_position->next->data < number)
	{

		current_position = current_position->next;

	}

	new_node->next = current_position->next;
	current_position->next = new_node;

	return (new_node);

}
