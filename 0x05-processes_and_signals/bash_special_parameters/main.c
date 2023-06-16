#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


extern char **environ;

/**
 * main - a program that ilustrates how to access the environment from
 *        within a process on linux.
 */
int main(void)
{
	int count = 0;
	char *val;

	printf("\n");

	while (environ[count] != NULL)
	{
		printf("[%s] ::\n", environ[count]);
		count++;
	}

	val = getenv("USER");
	printf("\nCurrent value of environment variable USER is [%s]\n", val);

	if (setenv("USER", "Arora", 1))
	{
		printf("\n setenv() failed\n");
		return (1);
	}
	printf("Successfully added a new value to existing environment variable USER\n");
	val = getenv("USER");
	printf("\nNew value of environment variable USER is [%s]\n", val);

	return (0);
}
