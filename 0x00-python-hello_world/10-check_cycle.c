#include "lists.h"

/**
 * check_cycle -> Must check if a linked list contains a cycle or not.
 * @list: The linked list to be checked.
 * Return: Must be 1 if the list contains a cycle,
 * or else 0 if it doesn't contain non.
 */
 
int check_cycle(listint_t *list)
{
        listint_t *slw = list;
        listint_t *fst = list;

        if (list == NULL)
                return (0);

        while (slw && fst && fst->next)
        {
                slw = slw->next;
                fst = fst->next->next;

                if (slw == fst)
                        return (1);

        }

        return (0);
}
