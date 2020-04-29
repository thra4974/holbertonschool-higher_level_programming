#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to linked list
 * Return: 1 if loop found, 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *DrEggMan = list;
	listint_t *Sonic = list;

	while (DrEggMan && Sonic && Sonic->next)
	{
		DrEggMan = DrEggMan->next;
		Sonic = Sonic->next->next;

		if (DrEggMan == Sonic)
			return (1);
	}
	return (0);
}
