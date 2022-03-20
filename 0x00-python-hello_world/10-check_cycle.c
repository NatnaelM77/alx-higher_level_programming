#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

int check_cycle(listint_t *list)
{
  listint_t *current, *check;

  if (list == NULL || list->next == NULL)
    return (0);
  current = list;
  check = current->next;

  while (current != NULL && check->next != NULL
	 && check->next->next != NULL)
    {
      if (current == check)
	return (1);
      current = current->next;
      check = check->next->next;
    }
  return (0);
}
