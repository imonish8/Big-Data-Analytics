#include<stdio.h>

int main()
{
	// Submitted by/ Monish (DBDA)
	// Program writes and read the output to the terminal.
	
	FILE *file = fopen("DBDA.txt", "w");
	fprintf(file, "Data Matters, Data is everything,Data is Future.");
	fclose(file);
	
	file = fopen("DBDA.txt", "r");
	char c;
	while((c = fgetc(file)) != EOF)
	{
	putchar(c);
	}
	fclose(file);
	return 0;
}
