#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * normalSpeed - traverse through list normally
 * @list: pointer to list
 * Return: nothing
 */

listint_t *normalSpeed(listint_t *list)
{
	listint_t *nrmS = list->next;

	return (nrmS);
}

/**
 * twiceSpeed - traverse at twice the pace normal
 * @list: pointer to list
 * Return: nothing
 */

listint_t *twiceSpeed(listint_t *list)
{
	listint_t *twiceS = list->next->next;

	return (twiceS);
}

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: pointer to linked list
 * Return: 1 if loop found, 0 if no loop
 */

int check_cycle(listint_t *list)
{
	/* initialize nodes pointing at the head of list */
	listint_t *DrEggMan = list; /* traverse slowly */
	listint_t *Sonic = list; /* traverse quickly */

	/* Traverse both lists */
	while (DrEggMan != NULL && Sonic != NULL && Sonic->next != NULL)
	{
		DrEggMan = normalSpeed(DrEggMan); /* 0.5xspeed of Sonic */
		Sonic = twiceSpeed(Sonic); /* 2xspeed of DrEggMan */

		if (DrEggMan == Sonic)
		{/* if Sonic at some locationas  DrEggMan then he lapped him */
			return (1);/* not moving backwards, must be loop */
		}
	}
	return (0); /*Dr Eggman never caught Sonic */
}
