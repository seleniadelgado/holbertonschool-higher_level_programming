#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - insert a number into a sorted singly linked list.
 * @head: head node of linkedlist.
 * @number: number inserted.
 * Return: pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *counter;
	listint_t *item;
	listint_t *temp;

	counter = malloc(sizeof(listint_t));
	if (counter == NULL)
		return (NULL);
	counter->n = number;
	if (head == NULL)
	{
		*head = counter;
		counter->next = NULL;
		return (*head);
	}
	item = *head;
	if (counter->n == item->n)
	{
		*head = counter;
		counter->next = item;
		return (counter);
	}
	while (item->next != NULL)
	{
		if (counter->n <= item->next->n)
		{
			temp = item;
			item = item->next;
			temp->next = counter;
			counter->next = item;
			return (counter);
		}
		item = item->next;
	}
	item->next = counter;
	counter->next = NULL;
	return (counter);
}
