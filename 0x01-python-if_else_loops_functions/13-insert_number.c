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
	listint_t *ite;
	listint_t *temp;

	counter = malloc(sizeof(listint_t));
	if (counter == NULL)
		return (NULL);
	counter->n = number;
	if (head == NULL)
	{
		*head = counter;
		counter->next = NULL;
		return (counter);
	}
	ite = *head;
	if (counter->n == ite->n)
	{
		*head = counter;
		counter->next = ite;
		return (counter);
	}
	while (ite->next != NULL)
	{
		if (counter->n <= ite->next->n)
		{
			temp = ite;
			ite = ite->next;
			temp->next = counter;
			counter->next = ite;
			return (counter);
		}
		ite = ite->next;
	}
	ite->next = counter;
	counter->next = NULL;
	return (counter);
}
