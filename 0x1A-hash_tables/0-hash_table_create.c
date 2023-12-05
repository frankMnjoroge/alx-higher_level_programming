#include "hash_tables.h"
/**
 * hash_table_create - create a hash table.
 * @size: size of the array.
 * Return: if an error occurs - NULL.
 *         Otherwise - a pointer to the new hash table.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *hat;
	unsigned long int j;

	hat = malloc(sizeof(hash_table_t));
	if (hat == NULL)
		return (NULL);

	hat->size = size;
	hat->array = malloc(sizeof(hash_node_t *) * size);
	if (hat->array == NULL)
		return (NULL);
	for (j = 0; j < size; j++)
		hat->array[j] = NULL;

	return (hat);
}
