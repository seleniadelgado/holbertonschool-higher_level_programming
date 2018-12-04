#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: parameter for linked list.
 * Return: 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *shoji = list;
	listint_t *athena = list;

	if (list == NULL)
		return (0);
	while (shoji != NULL && shoji->next != NULL)
	{
		shoji = shoji->next->next;
		athena = athena->next;
		if (shoji == athena)
			return (1);
	}
	return (0);
}
