#include<stdio.h>

int main()
{	printf("\n");
	printf("Enter a number to check Positivity, Negativity or Zero");
	int num = 0;
	scanf("%d", &num);
	printf("\n");
	switch((num>0) - (num<0))
	{
		case -1: printf("Number is Negative");
		break;

		case 0: printf("Number is Zero");
		break;
		
		case 1: printf("Number is Positive");
		break;
	}
	return 0;

}
