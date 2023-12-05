#include "hash_tables.h"

/**
 * hash_djb2 - Hash function implementing the djb2 algorithm.
 * @str: The string to hash.
 * Return: The calculated hash.
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int has;
	int j;

	has = 5381;
	while ((j = *str++))
		has = ((has << 5) + has) + j; /* has * 33 + j */

	return (has);
}
