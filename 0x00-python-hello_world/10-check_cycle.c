#include "lists.h"
/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *currnt, *chek;

	if (list == NULL || list->next == NULL)
		return (0);
	currnt = list;
	chek = current->next;

	while (currnt != NULL && chek->next != NULL
		&& chek->next->next != NULL)
	{
		if (currnt == chek)
			return (1);
		currnt = currnt->next;
		chek = chek->next->next;
	}
	return (0);
}
