#include "hash_tables.h"

/**
 * hash_djb2 - Hash function implementing the djb2 algorithm.
 * @str: The string to hash.
 *
 * Return: The calculated hash.
 */
unsigned long int hash_djb2(const unsigned char *str)
{
	unsigned long int hash;
	int y;

	hash = 5381;
	while ((y = *str++))
		hash = ((hash << 5) + hash) + y; /* hash * 33 + y */

	return (hash);
}
