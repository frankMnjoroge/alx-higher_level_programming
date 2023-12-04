#include "hash_tables.h"
/**
 * hash_table_create - create a hash table.
 * @size: size of the array.
 * Return: if an error occurs - NULL.
 *         Otherwise - a pointer to the new hash table.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *ht;
	unsigned long int y;

	ht = malloc(sizeof(hash_table_t));
	if (ht == NULL)
		return (NULL);

	ht->size = size;
	ht->array = malloc(sizeof(hash_node_t *) * size);
	if (ht->array == NULL)
		return (NULL);
	for (y = 0; y < size; y++)
		ht->array[y] = NULL;

	return (ht);
}
