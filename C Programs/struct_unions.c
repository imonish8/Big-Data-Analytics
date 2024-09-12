#include<stdio.h>

struct struct_values
{
	char character;
	int integer;
	double decimal;
};
union union_values
{
	char character;
	int integer;
	double decimal;
};
int main() 
{
	struct struct_values structExample;
	structExample.character = 'S';
	structExample.integer = 22;
	structExample.decimal = 20.22;

	printf("\n Character: %c",structExample.character);
	printf("\n The Model is: %i",structExample.integer);
	printf("\n The price is: %.2f",structExample.decimal);
	// becuase union has same shared memory location.
	union union_values myUni;
	myUni.character = 'U';
	printf("\n Union Character is : %c",myUni.character);
	myUni.integer = 88;
	printf("\n Union Integer is: %i",myUni.integer);
	myUni.decimal = 22.20;
	printf("\n Decimal is : %.2f",myUni.decimal);

	printf("Now Key Diff is here, printing intial character value after assingment of two varibales in the same meomory location is here: %c",myUni.character);



}
// Next Program : bit field is in Virtual Machine
